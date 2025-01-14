from locators.privacy_policy_locators import PrivacyPolicyLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.remote.webelement import WebElement
import time


class TestExtensionLaunch:
    def test_first_launch_after_install(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Check for presence a window with the terms of the Privacy Policy
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            consent_window = base_page.is_present('class_name', PrivacyPolicyLocators.ConsentWindow)
            assert isinstance(consent_window, WebElement)
            qase.create_passed_result(case=20, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=20, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Window of consent isn`t present \n {ex}")

    def test_button_close_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Check for presence a close button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            close_button = base_page.is_present('class_name', PrivacyPolicyLocators.CloseButton)
            assert isinstance(close_button, WebElement)
            qase.create_passed_result(case=22, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=22, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Close button isn`t present \n {ex}")

    def test_link_of_privacy_policy_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Check for presence of the link of Privacy Policy
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            link_privacy_policy = base_page.is_present('class_name', PrivacyPolicyLocators.LinkPrivacyPolicy)
            assert isinstance(link_privacy_policy, WebElement)
            qase.create_passed_result(case=24, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=24, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Link of privacy policy isn`t present \n {ex}")

    def test_launch_after_accept_privacy_policy(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Check for presence of main window
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            main_window = base_page.is_present('id', BaseLocators.MainWindow)
            assert isinstance(main_window, WebElement)
            qase.create_passed_result(case=25, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=25, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Main window isn`t present \n {ex}")
