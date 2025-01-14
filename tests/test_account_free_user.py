from base_classes.qase_integration import QaseMethods
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from locators.base_locators import BaseLocators
from locators.base_locators import PremiumBenefits
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.base_locators import AuthLocators
from selenium.webdriver.remote.webelement import WebElement
from locators.account_locators import AccountLocators
import time


class TestAccountFreeUser:

    def test_account_free_user(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Check for presence of webelements by visually
        """

        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
        go_back_button = base_page.is_present('id', AccountLocators.GoBackButton)
        menu = base_page.is_clickable('id', SidebarMenuLocators.MenuTitle)
        profile = base_page.is_visible('class_name', SidebarMenuLocators.ProfileText)
        login = base_page.is_visible('class_name', SidebarMenuLocators.LogIn)
        plan = base_page.is_visible('class_name', SidebarMenuLocators.PlanText)
        subscription = base_page.is_visible('class_name', SidebarMenuLocators.SubscriptionText)
        get_premium = base_page.is_visible('id', SidebarMenuLocators.GetPremium)
        settings = base_page.is_visible('id', SidebarMenuLocators.SettingsMenu)
        faq_menu = base_page.is_visible('id', SidebarMenuLocators.FaqMenu)
        share_menu = base_page.is_visible('id', SidebarMenuLocators.ShareMenu)
        rate_extension = base_page.is_visible('id', SidebarMenuLocators.RateExtension)
        try:
            assert go_back_button is not None
            assert login is not None
            assert plan is not None
            assert subscription is not None
            assert get_premium is not None
            assert settings is not None
            assert faq_menu is not None
            assert share_menu is not None
            assert rate_extension is not None
            qase.create_passed_result(case=178, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=178, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_goback_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Account button
            5. Click on the Go Back button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', AccountLocators.MenuTitle).click()
            current_location = base_page.is_present('id', SidebarMenuLocators.StatusCountry)
            assert current_location is not None
            qase.create_passed_result(case=180, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=180, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_account_title_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Menu title
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            menu = base_page.is_clickable('id', SidebarMenuLocators.MenuTitle).click()
            current_location = base_page.is_present('id', SidebarMenuLocators.StatusCountry)
            assert current_location is not None
            qase.create_passed_result(case=182, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=182, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_get_premium_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Account button
            5. Click on the Get Premium button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.GetPremium).click()
            premium_benefits_window = base_page.is_present('class_name', SidebarMenuLocators.ModalPremium)
            assert isinstance(premium_benefits_window, WebElement)
            qase.create_passed_result(case=185, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=185, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_button_login_click(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Account button
            5. Click on the Login button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('class_name', SidebarMenuLocators.LogIn).click()
            title_authorization = base_page.is_present('id', SidebarMenuLocators.SignIn)
            assert isinstance(title_authorization, WebElement)
            qase.create_passed_result(case=189, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=189, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")
