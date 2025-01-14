from base_classes.qase_integration import QaseMethods
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.auth_ext_page import AuthExtPage
from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from selenium.webdriver.remote.webelement import WebElement
from pages.sidebar_menu_page import SidebarMenuExtPage
import time


class TestSidebarMenu:

    def test_sidebar_menu_webelements_for_unauthorized_user(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        sidebar_menu_methods = SidebarMenuExtPage(setup_driver)
        try:
            settings_button = sidebar_menu_methods.settings_button_is_present()
            faq_button = sidebar_menu_methods.faq_button_is_present()
            rate_extension = sidebar_menu_methods.rate_button_is_present()
            share_button = sidebar_menu_methods.share_button_is_present()
            get_premium_button = sidebar_menu_methods.get_premium_button_is_present()
            assert isinstance(settings_button, WebElement)
            assert isinstance(faq_button, WebElement)
            assert isinstance(rate_extension, WebElement)
            assert isinstance(share_button, WebElement)
            assert isinstance(get_premium_button, WebElement)
            qase.create_passed_result(case=113, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=113, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_sidebar_menu_webelements_for_free_user(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
            4. Click on the burger menu button
            5. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        sidebar_menu_methods = SidebarMenuExtPage(setup_driver)
        auth_methods = AuthExtPage(setup_driver)
        try:
            auth_methods.login_free_user()
            base_page.burger_menu_button_is_present().click()
            settings_button = sidebar_menu_methods.settings_button_is_present()
            faq_button = sidebar_menu_methods.faq_button_is_present()
            rate_extension = sidebar_menu_methods.rate_button_is_present()
            share_button = sidebar_menu_methods.share_button_is_present()
            get_premium_button = sidebar_menu_methods.get_premium_button_is_present()
            assert isinstance(settings_button, WebElement)
            assert isinstance(faq_button, WebElement)
            assert isinstance(rate_extension, WebElement)
            assert isinstance(share_button, WebElement)
            assert isinstance(get_premium_button, WebElement)
            qase.create_passed_result(case=115, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=115, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")
