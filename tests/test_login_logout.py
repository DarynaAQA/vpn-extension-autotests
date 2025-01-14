from pages.auth_ext_page import AuthExtPage
from locators.base_locators import BaseLocators
from locators.account_locators import AccountLocators
from selenium.webdriver.remote.webelement import WebElement
import time


class TestLoginLogout:

    def test_click_login_icon(self, setup_driver, qase_run_id, launch_methods):
        """STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the login icon
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            login_icon = base_page.is_visible('id', AccountLocators.LoginButtonNew)
            get_premium_icon = base_page.is_visible('id', BaseLocators.GetPremiumButton)
            assert login_icon is not None
            assert get_premium_icon is not None
            qase.create_passed_result(case=47, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=47, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_button_logout_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_free_user()
            logout = base_page.is_visible('id', AccountLocators.LogOut)
            assert logout is not None
            qase.create_passed_result(case=48, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=48, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_click_logout_button(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
            4. Click on the login icon
            5. Click on the logout button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_free_user()
            base_page.is_visible('id', AccountLocators.LogOut).click()
            confirm_logout = base_page.is_present('id', AccountLocators.WindowConfirmLogout)
            assert confirm_logout is not None
            qase.create_passed_result(case=50, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=50, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_confirm_window_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
            4. Click on the login icon
            5. Click on the logout button
            6. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_free_user()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            confirm_action_text = base_page.is_present('id', AccountLocators.WindowConfirmLogout)
            confirm_action_text_body = base_page.is_present('id', AccountLocators.DoYouWantLogout)
            yes_button = base_page.is_present('xpath', AccountLocators.SpanYes)
            no_button = base_page.is_present('xpath', AccountLocators.SpanNo)
            close_button = base_page.is_clickable('xpath', AccountLocators.CloseModalWindow)
            assert confirm_action_text is not None
            assert confirm_action_text_body is not None
            assert yes_button is not None
            assert no_button is not None
            assert close_button is not None
            qase.create_passed_result(case=51, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=51, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")


    def test_click_close_button(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
            4. Click on the login icon
            5. Click on the logout button
            6. Click on the close button
            7. Check for presence the Account header
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_free_user()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            base_page.is_clickable('xpath', AccountLocators.CloseModalWindow).click()
            title_account = auth_methods.title_account_is_present()
            assert isinstance(title_account, WebElement)
            qase.create_passed_result(case=54, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=54, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_click_cancel_button(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
            4. Click on the login icon
            5. Click on the logout button
            6. Click on the No button
            7. Check for presence the Account header
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_free_user()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            base_page.is_clickable('xpath', AccountLocators.SpanNo).click()
            title_account = auth_methods.title_account_is_present()
            assert isinstance(title_account, WebElement)
            qase.create_passed_result(case=55, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=55, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_click_confirm_button(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a free user
            4. Click on the login icon
            5. Click on the logout button
            6. Click on the Yes button
            7. Check for presence the Planet VPN logo
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_free_user()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            base_page.is_clickable('xpath', AccountLocators.SpanYes).click()
            logo_planet = base_page.is_present('class_name', BaseLocators.LogoPlanetVpn)
            assert isinstance(logo_planet, WebElement)
            qase.create_passed_result(case=56, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=56, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")















