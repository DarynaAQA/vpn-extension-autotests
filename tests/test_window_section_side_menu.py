from base_classes.qase_integration import QaseMethods
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from locators.base_locators import PremiumBenefits
from locators.sidebar_menu_locators import SidebarMenuLocators
from pages.auth_ext_page import AuthExtPage
import time


class TestWindowSectionSideMenu:

    def test_clickability_button_get_premium(self, setup_driver, qase_run_id, launch_methods):
        """ID 256 Clickability of button 'Get premium'
           STEPS:
           1.Go to main page
           2.Click burrger menu
           3.Click 'Get Premium' button
           4.Make sure the 'Get Premium' button is clickable"""
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        get_premium_button = base_page.is_clickable('id', SidebarMenuLocators.GetPremiumButton)
        get_premium_button.click()
        proceed_to_order_button = base_page.is_present('id', PremiumBenefits.StartOrdering)
        try:
            assert proceed_to_order_button is not None
            qase.create_passed_result(case=256, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=256, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'"Get Premium Button" is not clickable\n{ex}')

    def test_elements_burger_menu_for_premium_user(self, setup_driver, qase_run_id, launch_methods):
        """ID 257 Displaying the side menu for Premium user
          STEPS:
          1.Go to main page
          2.Login to Premium
          3.Click Burger menu
          4.Make sure all burger menu elements are visible"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            auth_methods = AuthExtPage(setup_driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            base_page.burger_menu_button_is_present().click()
            li_settings = base_page.is_visible('id', SidebarMenuLocators.SettingsMenu)
            li_faq = base_page.is_visible('id', SidebarMenuLocators.FaqMenu)
            li_rate = base_page.is_visible('id', SidebarMenuLocators.RateExtension)
            li_share = base_page.is_visible('id', SidebarMenuLocators.ShareMenu)
            assert li_settings is not None
            assert li_faq is not None
            assert li_rate is not None
            assert li_share is not None
            qase.create_passed_result(case=257, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=257, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Not all burger menus is visible\n{ex}')
