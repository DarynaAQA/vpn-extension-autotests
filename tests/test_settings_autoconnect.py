from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.settings_locators import SettingsLocators
import time


class TestSettingsAutoConnect:

    def test_autoconnect_switch_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Connect on startup switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.AutoconnectSwitch).click()
            time.sleep(1)
            autoconnect_switch = base_page.is_visible('xpath', SettingsLocators.AutoconnectSwitchColor)
            color_actual = autoconnect_switch.value_of_css_property('background-color')
            assert color_actual == 'rgba(135, 171, 73, 1)'
            qase.create_passed_result(case=258, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=258, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_autoconnect_icon_after_activating_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Connect on startup switch
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.AutoconnectSwitch).click()
            time.sleep(1)
            autoconnect_icon_svg = base_page.is_present('id', BaseLocators.IndicatorAutoconnect)
            autoconnect_icon_svg_color = autoconnect_icon_svg.value_of_css_property('fill')
            assert autoconnect_icon_svg_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=288, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=288, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")

    def test_displaying_autoconnect_icon_after_deactivating_switch(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the Settings button
            5. Click on the Connect on startup switch
            6. Click on the Connect on startup switch for deactivating it
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.AutoconnectSwitch).click()
            time.sleep(1)
            base_page.is_clickable('id', SettingsLocators.AutoconnectSwitch).click()
            time.sleep(1)
            autoconnect_icon_svg = base_page.is_present('id', BaseLocators.IndicatorAutoconnect)
            autoconnect_icon_svg_color = autoconnect_icon_svg.value_of_css_property('fill')
            assert autoconnect_icon_svg_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=289, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=289, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Colors don't match \n {ex}")
