from pages.auth_ext_page import AuthExtPage
from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.account_locators import AccountLocators
import time


class TestAccountPremiumUser:
    def test_account_premium_user(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger Menu
            5. Check for presence of webelements by visually
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            auth_methods = AuthExtPage(setup_driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            menu = base_page.is_visible('id', AccountLocators.MenuTitle)
            back_button = base_page.is_present('id', AccountLocators.GoBackButton)
            premium_title = base_page.is_visible('class_name', AccountLocators.PremiumTitle)
            plan = base_page.is_visible('id', AccountLocators.Plan)
            logout = base_page.is_visible('id', AccountLocators.LogOut)
            email = base_page.is_visible('id', AccountLocators.EmailPremium)
            numbers_of_days = base_page.is_visible('id', AccountLocators.NumbersOfDays)
            expirations_days = base_page.is_visible('id', AccountLocators.ExpirationDays)
            renew_button = base_page.is_visible('id', AccountLocators.RenewButton)
            applications = base_page.is_visible('class_name', AccountLocators.Applications)
            settings = base_page.is_visible('id', SidebarMenuLocators.SettingsMenu)
            faq = base_page.is_visible('id', SidebarMenuLocators.FaqMenu)
            share = base_page.is_visible('id', SidebarMenuLocators.ShareMenu)
            rate_extension = base_page.is_visible('id', SidebarMenuLocators.RateExtension)
            assert menu.is_displayed()
            assert numbers_of_days.is_displayed()
            assert expirations_days.is_displayed()
            assert applications.is_displayed()
            assert settings.is_displayed()
            assert share.is_displayed()
            assert rate_extension.is_displayed()
            assert renew_button.is_displayed()
            assert faq.is_displayed()
            assert expirations_days.is_displayed()
            assert email.is_displayed()
            assert plan.is_displayed()
            assert back_button is not None
            assert premium_title.is_displayed()
            assert logout.is_displayed()
            qase.create_passed_result(case=201, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=201, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_goback_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the Go Back button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.MenuTitle).click()
            current_location = base_page.is_present('id', SidebarMenuLocators.StatusCountry)
            assert current_location is not None
            qase.create_passed_result(case=204, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=204, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_account_title_click(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            6. Click on the Account title
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.MenuTitle).click()
            current_location = base_page.is_present('id', SidebarMenuLocators.StatusCountry)
            assert current_location is not None
            qase.create_passed_result(case=206, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=206, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_prolong_premium_link_click(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the "Renew" link
            6. Activate redirect page
            7. Get current url on the web page
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.RenewButton).click()
            base_page.activate_redirect_page()
            time.sleep(10)
            actual_link_order = "https://freevpnplanet.com/order/"
            current_link_order = base_page.get_current_url()
            assert current_link_order == actual_link_order
            qase.create_passed_result(case=209, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=209, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_logout_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the Logout button
         """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            do_you_want_log_out = base_page.is_present('id', AccountLocators.DoYouWantLogout)
            no_button = base_page.is_present('xpath', AccountLocators.SpanNo)
            yes_button = base_page.is_present('xpath', AccountLocators.SpanYes)
            assert do_you_want_log_out is not None
            assert no_button is not None
            assert yes_button is not None
            qase.create_passed_result(case=212, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=212, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_confirm_button_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the Logout button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            logout = base_page.is_clickable('id', AccountLocators.LogOut).click()
            confirm_button = base_page.is_present('xpath', AccountLocators.SpanYes)
            assert confirm_button is not None
            qase.create_passed_result(case=213, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=213, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_confirm_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the Logout button
            6. Click on the Yes button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            logout = base_page.is_clickable('id', AccountLocators.LogOut).click()
            button = base_page.is_visible('xpath', AccountLocators.SpanYes)
            button.click()
            current_location = base_page.is_present('id', SidebarMenuLocators.StatusCountry)
            assert current_location is not None
            qase.create_passed_result(case=215, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=215, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_cancel_button_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the Account button
            6. Click on the Logout button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            cancel_button = base_page.is_present('xpath', AccountLocators.SpanNo)
            assert cancel_button is not None
            qase.create_passed_result(case=216, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=216, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_cancel_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Click on the Burger menu button
            5. Click on the Account button
            6. Click on the Logout button
            7. Click on the No button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.LogOut).click()
            cancel_button = base_page.is_clickable('xpath', AccountLocators.SpanNo).click()
            assert base_page.is_visible('id', AccountLocators.LogOut).is_displayed()
            qase.create_passed_result(case=218, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=218, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

