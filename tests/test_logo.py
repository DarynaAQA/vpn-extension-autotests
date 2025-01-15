from locators.base_locators import BaseLocators
from locators.site_locators import SiteLocators
from selenium.webdriver.remote.webelement import WebElement
import time


class TestLogo:

    def test_click_logo(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the VPN logo
            4. Activate redirect page
            5. Check for presence VPN logo on the website
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.find_element('class_name', BaseLocators.LogoVpn).click()
            base_page.activate_redirect_page()
            logo_vpn = base_page.is_visible('xpath', SiteLocators.LogoVpn)
            assert isinstance(logo_vpn, WebElement)
            qase.create_passed_result(case=44, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=44, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")
