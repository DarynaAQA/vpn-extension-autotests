from base_classes.qase_integration import QaseMethods
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.settings_locators import SettingsLocators
from pages.settings_dont_save_history_page import DontSaveHistoryPage
from locators.settings_locators import ReloadPopUpLocators
from selenium.webdriver.remote.webelement import WebElement
import time


class TestSaveHistory:

    def test_dont_save_history_switch_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Don't save history switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            time.sleep(1)
            history_switch = base_page.is_visible('xpath', SettingsLocators.HistorySwitchColor)
            color_activate_switch = 'rgba(135, 171, 73, 1)'
            color_actual = history_switch.value_of_css_property('background-color')
            assert color_activate_switch == color_actual
            qase.create_passed_result(case=302, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=302, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_history_icon_after_activating_switch(self, setup_driver, qase_run_id, launch_methods):
        """
             STEPS:
             1. Activate page with the extension
             2. Click on the consent button of Privacy Policy
             3. Click on the burger menu button
             4. Click on the Settings button
             5. Click on the Don't save history switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            time.sleep(1)
            history_icon = base_page.is_present('id', SettingsLocators.HistoryIconSVG)
            history_icon_color = history_icon.value_of_css_property('fill')
            assert history_icon_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=303, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=303, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_history_icon_after_deactivating_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Don't save history switch
            6. Click on the Don't save history switch for deactivating it
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            time.sleep(1)
            history_icon = base_page.is_present('id', SettingsLocators.HistoryIconSVG)
            history_icon_color = history_icon.value_of_css_property('fill')
            assert history_icon_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=304, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=304, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_pop_up_after_enabling_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Don't save history switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            close_button = base_page.is_present('id', ReloadPopUpLocators.CloseNotification)
            notification_text = base_page.is_present('id', ReloadPopUpLocators.TextNotification)
            reload_button = base_page.is_present('id', ReloadPopUpLocators.ReloadButton)
            assert isinstance(close_button, WebElement)
            assert isinstance(notification_text, WebElement)
            assert isinstance(reload_button, WebElement)
            qase.create_passed_result(case=305, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=305, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_displaying_pop_up_after_disabling_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Don't save history switch
            6. Click on the Don't save history switch for disabling it
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            close_button = base_page.is_present('id', ReloadPopUpLocators.CloseNotification)
            notification_text = base_page.is_present('id', ReloadPopUpLocators.TextNotification)
            reload_button = base_page.is_present('id', ReloadPopUpLocators.ReloadButton)
            assert isinstance(close_button, WebElement)
            assert isinstance(notification_text, WebElement)
            assert isinstance(reload_button, WebElement)
            qase.create_passed_result(case=306, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=306, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_visiting_websites_with_history_switch_activated(self, setup_driver, launch_methods, qase_run_id):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Don't save history switch
            6. Open google.com four times
            7.Make sure browser history must be a 3 quantity pages
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
        dont_save_history = base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
        base_page.refresh_page()
        base_page.open_url('https://google.com')
        base_page.open_url('https://google.com')
        base_page.open_url('https://google.com')
        base_page.open_url('https://google.com')
        history = base_page.get_browser_history()
        try:
            assert history == 3
            qase.create_passed_result(case=307, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except  AssertionError as ex:
            qase.create_failed_result(case=307, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_visiting_websites_after_history_switch_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Don't save history switch
            6. Open the website in a new tab
            7. Click on the Don't save history switch for disabling it
            8. Open the website https://ipinfo.io/ in a new tab
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            time.sleep(1)
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            base_page.open_url('https://amazon.com')
            base_page.open_url('https://apple.com')
            base_page.open_url('https://youtube.com')
            history = base_page.get_browser_history()
            assert history == 5
            qase.create_passed_result(case=308, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=308, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"The last visited site is missing from the browser history \n {ex}")
