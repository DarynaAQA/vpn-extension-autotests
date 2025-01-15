import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv, set_key
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.sidebar_menu_page import SidebarMenuExtPage
from base_classes.qase_integration import QaseMethods
import datetime
import os

load_dotenv()

extension_paths = {
    'chrome': 'extension/{name}.zip',
    'firefox': 'extension/{name}.zip'
}

extension_paths = {
    'chrome': 'extension/{name}.zip',
    'firefox': 'extension/{name}.zip'
}


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on (chrome or firefox)")

    parser.addoption("--slack-channel", action="store", default="qa-qase-results-release",
                     help="Slack channel to send test run reports to")


@pytest.fixture(scope='function')
def setup_driver(request):
    """
        Steps:
        1. Installs the specified browser
        2. Installs a test build of the extension
        3. Opens tab in maximize size in the browser
        4. Returns browser driver
        5. After execute every test function it closes browser session.
    """
    browser = request.config.getoption("--browser")
    gh_token = os.getenv("GH_TOKEN")
    if not gh_token:
        raise ValueError("GH_TOKEN is not set in the environment variables")
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless=new')
        options.add_argument('--lang=en-US')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-features=VizDisplayCompositor')
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
        options.add_extension(extension_paths['chrome'])
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == 'firefox':
        os.environ['GH_TOKEN'] = gh_token
        service = FirefoxService(GeckoDriverManager().install(), log_path="geckodriver.log")
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.set_preference('intl.accept_languages', 'en-US')
        options.set_preference('gfx.webrender.all', False)
        options.set_preference('layers.acceleration.disabled', True)
        options.set_preference('browser.tabs.remote.autostart', False)
        driver = webdriver.Firefox(service=service, options=options)
        driver.install_addon(extension_paths['firefox'], temporary=True)
    else:
        raise ValueError(f"Browser {browser} is not supported. Choose 'chrome' or 'firefox'.")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def qase_run_id():
    qase_run = QaseMethods()
    test_run = qase_run.create_test_run(test_plan_id=2)
    return test_run


@pytest.fixture(scope='session', autouse=False)
def send_test_run(qase_run_id, request):
    qase_run = QaseMethods()
    start_hours = datetime.datetime.now()
    yield
    url = qase_run.update_publicity_test_run(qase_run_id)
    end_hours = datetime.datetime.now()
    result = end_hours - start_hours
    trimmed_time = str(result).split('.')[0]

    slack_channel = request.config.getoption("--slack-channel", default="qa-qase-results-release")
    qase_run.send_test_run_url_to_slack(url, test_time=trimmed_time, slack_channel=slack_channel)


@pytest.fixture(scope='session', autouse=True)
def save_ip_to_env():
    response = requests.get('https://api.ipify.org?format=json')
    ip_address = response.json()['ip']
    response = requests.get('https://ipinfo.io')
    country_code = response.json()['country']

    load_dotenv()
    env_path = '.env'
    set_key(env_path, 'MY_IP_ADDRESS', ip_address)
    set_key(env_path, 'MY_COUNTRY_CODE', country_code)


@pytest.fixture()
def emulate_network_conditions(setup_driver):
    driver = setup_driver

    def go_offline():
        print("Going offline")
        driver.execute_cdp_cmd('Network.enable', {})
        driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
            'offline': True,
            'latency': 0,
            'downloadThroughput': 0,
            'uploadThroughput': 0
        })
        print("Offline command executed")

    def go_online():
        print("Going online")
        driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
            'offline': False,
            'latency': 20,  # ms
            'downloadThroughput': 500 * 1024,  # 500 kb/s
            'uploadThroughput': 500 * 1024  # 500 kb/s
        })
        print("Online command executed")

    yield driver, go_offline, go_online
    driver.quit()


@pytest.fixture(autouse=True)
def launch_methods(setup_driver):
    base_page = BaseExtPage(setup_driver)
    privacy_policy = PrivacyPolicyPage(setup_driver)
    sidebar_menu = SidebarMenuExtPage(setup_driver)
    qase = QaseMethods()
    return base_page, privacy_policy, sidebar_menu, qase

