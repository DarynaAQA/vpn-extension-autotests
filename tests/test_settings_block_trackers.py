from base_classes.qase_integration import QaseMethods
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.settings_locators import SettingsLocators
from locators.settings_locators import ReloadPopUpLocators
from selenium.webdriver.remote.webelement import WebElement
import time


class TestBlockTrackers:
    def test_block_trackers_switch_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            time.sleep(2)
            block_trackers_switch = base_page.is_visible('xpath', SettingsLocators.TrackersSwitchColor)
            color_activate_switch = 'rgba(135, 171, 73, 1)'
            color_actual = block_trackers_switch.value_of_css_property('background-color')
            assert color_activate_switch == color_actual
            qase.create_passed_result(case=295, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=295, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_blocking_trackers_icon_after_activating_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            time.sleep(3)
            block_trackers_icon = base_page.is_visible('id', SettingsLocators.TrackersIconColor)
            color_icon_actual = 'rgb(135, 171, 73)'
            color_icon = block_trackers_icon.value_of_css_property('fill')
            assert color_icon_actual == color_icon
            qase.create_passed_result(case=296, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=296, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_blocking_trackers_icon_after_deactivating_switch(self, setup_driver, qase_run_id,
                                                                         launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
            6. Click on the Block trackers switch for deactivating it
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            time.sleep(1)
            block_trackers_icon = base_page.is_visible('id', SettingsLocators.TrackersIconColor)
            color_icon_actual = 'rgb(215, 222, 237)'
            color_icon = block_trackers_icon.value_of_css_property('fill')
            assert color_icon_actual == color_icon
            qase.create_passed_result(case=297, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=297, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_pop_up_after_enabling_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            close_button = base_page.is_present('id', ReloadPopUpLocators.CloseNotification)
            notification_text = base_page.is_present('id', ReloadPopUpLocators.TextNotification)
            reload_button = base_page.is_present('id', ReloadPopUpLocators.ReloadButton)
            assert isinstance(close_button, WebElement)
            assert isinstance(notification_text, WebElement)
            assert isinstance(reload_button, WebElement)
            qase.create_passed_result(case=298, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=298, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_displaying_pop_up_after_disabling_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
            6. Click on the Block trackers switch for deactivating it
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            base_page.burger_menu_button_is_present().click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            close_button = base_page.is_present('id', ReloadPopUpLocators.CloseNotification)
            notification_text = base_page.is_present('id', ReloadPopUpLocators.TextNotification)
            reload_button = base_page.is_present('id', ReloadPopUpLocators.ReloadButton)
            assert isinstance(close_button, WebElement)
            assert isinstance(notification_text, WebElement)
            assert isinstance(reload_button, WebElement)
            qase.create_passed_result(case=299, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=299, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_visiting_website_with_tracker_blocking_switch_activated(self, setup_driver, launch_methods, qase_run_id):
        """ ID 300
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
            6.Go to https://ads-blocker.com/ru/test-blokirovshchika-reklamy/
            7.Get logs
            8.Make sure block trackers blocked tracker
            """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_trackers_switch = base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            base_page.open_url('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            logs = setup_driver.get_log('browser')
            block_trackers = False
            for log in logs:
                if 'message' in log and 'ERR_BLOCKED_BY_CLIENT' in log['message']:
                    block_trackers = True
                break
            if block_trackers:
                qase.create_passed_result(case=300, test_run_id=qase_run_id, time=time.time() - base_page.time)
            else:
                raise AssertionError('Block trackers not work')
        except AssertionError as ex:
            qase.create_failed_result(case=300, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Block trackers not block tracker\n {ex}")

    def test_visiting_website_with_tracker_blocking_switch_deactivated(self, setup_driver, launch_methods, qase_run_id):
        """ID 301
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Block trackers switch
            6. Click on the Block trackers switch again and off him
            6.Go to https://ads-blocker.com/ru/test-blokirovshchika-reklamy/
            8.Make sure block trackers  NOT blocked tracker"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_trackers = base_page.is_clickable('id', SettingsLocators.TrackersSwitch)
            block_trackers.click()
            block_trackers.click()
            base_page.open_url('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            logs = setup_driver.get_log('browser')
            block_trackers = False
            for log in logs:
                if 'message' in log and 'ERR_BLOCKED_BY_CLIENT' not in log['message']:
                    block_trackers = True
                break
            if block_trackers:
                qase.create_passed_result(case=301, test_run_id=qase_run_id, time=time.time() - base_page.time)
            else:
                raise AssertionError('Block trackers work')
        except AssertionError as ex:
            qase.create_failed_result(case=301, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Block trackers block the trackers website\n {ex}")
