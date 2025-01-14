from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.support import expected_conditions as ec
import time


class Driver:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20, 1)
        self.time = time.time()

    def get_logs_browser(self, url: str):
        """
            This method get logs from console of browser.
        """
        self.driver.get(url)
        self.driver.execute_script("console.log('Hello from Selenium!');")
        logs = self.driver.get_log('browser')
        return logs

    def get_last_visited_website(self):
        """
            This method get last visited website from browsing history.
        """
        self.driver.execute_script("localStorage.setItem('lastVisited', window.location.href);")
        last_visited = self.driver.execute_script("return localStorage.getItem('lastVisited');")
        return last_visited

    def quit_browser(self):
        """
            This method close browser session.
        """
        self.driver.quit()

    def open_url(self, url: str):
        """
            This method open url. It accepts url, that you want to open.
        """
        self.driver.get(url)

    def get_current_url(self):
        """
            This method get current url on the web page, where you are at the moment.
        """
        return self.driver.current_url

    @staticmethod
    def get_driver_by(find_by: str):
        find_by = find_by.lower()
        locating_elements = {
            'id': By.ID,
            'name': By.NAME,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'css': By.CSS_SELECTOR,
            'tag-name': By.TAG_NAME
        }
        return locating_elements[find_by]

    def get_element_text(self, find_by: str, locator: str):
        """
            This method get text from web element on the page.
        """
        return self.driver.find_element(self.get_driver_by(find_by), locator).text

    def find_element(self, find_by: str, locator: str):
        """
            This method find web element by specific locator.
        """
        return self.driver.find_element(self.get_driver_by(find_by), locator)

    def are_visible(self, find_by: str, locator: str) -> List[WebElement]:
        """
            This method wait visibility of all elements located and after that find these elements.
        """
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_driver_by(find_by), locator)))

    def is_visible(self, find_by: str, locator: str) -> WebElement:
        """
            This method wait visibility of element located and after that find this element.
        """
        return self.wait.until(ec.visibility_of_element_located((self.get_driver_by(find_by), locator)))

    @staticmethod
    def get_text_from_webelements(elements: List[WebElement]):
        """
            This method get text from the list of web elements on the page.
        """
        return [element.text for element in elements]

    def is_present(self, find_by: str, locator: str) -> WebElement:
        """
            This method wait presence of element located, after that find it.
        """

        return self.wait.until(ec.presence_of_element_located((self.get_driver_by(find_by), locator)))

    def is_clickable(self, find_by: str, locator: str) -> WebElement:
        """
            This method wait clickable of element located, after that find it.
        """

        return self.wait.until(ec.element_to_be_clickable((self.get_driver_by(find_by), locator)))

    def refresh_page(self):
        """
            This method refresh the current web page.
        """
        return self.driver.refresh()

    def implicitly_wait(self, interval: int):
        """
            This method implicitly wait for element to appear.
        """
        return self.driver.implicitly_wait(interval)

    def invisibility_of_element_located(self, find_by: str, locator: str):
        """
            Waits for an element to become invisible or not present on the page.

            """
        return self.wait.until(ec.invisibility_of_element_located((self.get_driver_by(find_by), locator)))

    def get_page_title(self):
        """ Get page  title """
        return self.driver.title

    def get_browser_history(self):
        """ Get browser history """
        history = self.driver.execute_script("return window.history.length")
        return history



