import time
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.settings_locators import SettingsLocators, ReloadPopUpLocators
from locators.share_locators import ShareLocators
from locators.base_locators import BaseLocators


class TestCookiesPopUp:

    def test_display_pop_up_after_enabling_cookie_blocking_switch(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 280
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click on the settings menu
        4.Click on the "Deny cookies" tugle
        5.Make sure after click user can see pop up with information"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            cookies_switch = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            pop_up = base_page.is_present('class_name', ShareLocators.ShareWindow)
            assert pop_up is not None
            qase.create_passed_result(case=280, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=280, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Pop-up not is displayed\n {ex}")

    def test_clickability_ok_button(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 282
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click on the settings menu
        4.Click on the "Deny cookies" toggle
        5.Make sure after click user can see pop up with information
        6.Click on the OK button make sure pop up is closed and user can see Settings page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            cookies_checkbox = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            ok_button = base_page.is_clickable('xpath', SettingsLocators.ConsentCookies)
            ok_button.click()
            title_settings = base_page.is_visible('id', ReloadPopUpLocators.SETTINGS_TITLE)
            assert title_settings.text == 'Settings'
            qase.create_passed_result(case=282, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=282, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Ok button is bot clickable\n {ex}")

    def test_clickability_don_show_again_button(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 283
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click on the settings menu
        4.Click on the "Deny cookies" tugle
        5.Make sure after click user can see pop up with information
        6.Click on the "Don't show again" """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            cookies_checkbox = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            dont_show_again_button = base_page.is_clickable('class_name', BaseLocators.DONT_SHOW_AGAIN_BUTTON)
            dont_show_again_button.click()
            qase.create_passed_result(case=283, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=283, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"'Don't show again' button is bot clickable\n {ex}")

    def test_pop_up_after_use_dont_show_again_button(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 284
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click on the settings menu
        4.Click on the "Deny cookies" button
        5.Make sure after click user can see pop up with information
        6.Click on the "Don't show again"
        7.Click on the "Deny cookies" button
        8.Make sure after click user can't see pop-up"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            cookies_checkbox = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            pop_up = base_page.is_present('class_name', ShareLocators.ShareWindow)
            dont_show_again_button = base_page.is_clickable('class_name', BaseLocators.DONT_SHOW_AGAIN_BUTTON).click()
            ok_button = base_page.is_clickable('xpath', SettingsLocators.ConsentCookies).click()
            cookies_checkbox = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            base_page.refresh_page()
            cookies_checkbox = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            assert base_page.invisibility_of_element_located('id', ShareLocators.ShareWindow)
            qase.create_passed_result(case=284, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=284, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"The user should not see the pop-up after clicking the Don't show again button\n {ex}")

    def test_clickability_x_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 281
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click on the settings menu
        4.Click on the "Deny cookies" toggle
        5.Make sure after click user can see pop up with information
        6.Click on the "X" button pop up must be closed """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            cookies_checkbox = base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            pop_up = base_page.is_present('class_name', ShareLocators.ShareWindow)
            x_button = base_page.is_clickable('xpath', BaseLocators.CLOSE_BUTTON).click()
            assert base_page.invisibility_of_element_located('id', ShareLocators.ShareWindow)
            qase.create_passed_result(case=281, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=281, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Button 'X' not clickable\n {ex}")
