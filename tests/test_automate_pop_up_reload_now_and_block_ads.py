from locators.settings_locators import SettingsLocators, ReloadPopUpLocators
from locators.sidebar_menu_locators import SidebarMenuLocators

import time


class TestAutomatePopUpAndBlockAds:

    def test_reload_now_pop_up_after_adding_site_to_exceptions(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 293
        STEPS:
        1.Open app
        2.Click manage button
        3.Enter google.com on the input field
        4.Click add website button
        5.Make sure pop up with "Reload Now" text is visible
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input.click()
            web_site_input.send_keys('https://google.com')
            add_web_site_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            reload_now_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            assert reload_now_pop_up.text == 'Reload Now'
            qase.create_passed_result(case=293, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=293, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Reload Now pop up not visible\n{ex}')

    def test_reload_now_pop_up_after_deleting_site_to_exceptions(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 294
        STEPS:
        1.Open app
        2.Click manage button
        3.Enter google.com on the input field
        4.Click add website button
        5.Delete  website on the list
        6.Make sure pop up with "Reload Now" text is visible"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input.click()
            web_site_input.send_keys('https://google.com')
            add_web_site_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            delete_web_site_button = base_page.is_visible('class_name', ReloadPopUpLocators.DELETE_WEBSITE_BUTTON_X).click()
            reload_now_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            assert reload_now_pop_up.text == 'Reload Now'
            qase.create_passed_result(case=294, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=294, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Reload Now pop up not visible\n{ex}')

    def test_displaying_pop_up_after_enabling_blocking_switch(self, setup_driver, qase_run_id, launch_methods):
        """ID 266
        STEPS:
        1.Open app
        2.Click manage button
        3.Find and click blocking switch button
        4.Make sure pop up with "Reload Now" text is visible"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            blocking_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            reload_now_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            assert reload_now_pop_up.text == 'Reload Now'
            qase.create_passed_result(case=266, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=266, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Reload Now pop up not visible\n{ex}')

    def test_clickability_button_x(self, setup_driver, qase_run_id, launch_methods):
        """ID 267
            STEPS:
            1.Open app
            2.Click manage button
            3.Find and click blocking switch button
            4.Find "Reload Now" pop-up and lick X button
            5.Make sure pop up not visible after"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            blocking_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            reload_now_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            x_button = base_page.is_clickable('class_name', ReloadPopUpLocators.X_BUTTON).click()
            assert base_page.invisibility_of_element_located('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            qase.create_passed_result(case=267, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=267, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Close pop up button "X" not clickable\n{ex}')

    def test_clickability_reload_now_button(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 268
        STEPS:
         1.Open app
         2.Click manage button
         3.Find and click blocking switch button
         4.Find "Reload Now" pop-up and click "Reload Now"
         5.Make sure pop up not visible after"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            blocking_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            reload_now_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            reload_now_pop_up.click()
            assert base_page.invisibility_of_element_located('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            qase.create_passed_result(case=268, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=268, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Close pop up button "X" not clickable\n{ex}')

    def test_displaying_pop_up_after_disable_blocking_switch(self, setup_driver, launch_methods, qase_run_id):
        """ID 285
            STEPS:
            1.Open app
            2.Click manage button
            3.Find and click blocking switch button
            4.Find and click blocking switch button again
            5.Make sure pop up "Reload Now" visible after"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            blocking_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            x_button = base_page.is_clickable('class_name', ReloadPopUpLocators.X_BUTTON).click()
            blocking_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            reload_now_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            assert reload_now_pop_up.text == 'Reload Now'
            qase.create_passed_result(case=285, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=285, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Pop-up is not present\n{ex}')

    def test_clickability_block_ads_switch_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 261
            1.Open app
            2.Find and click blocking switch button
            4.Make sure radio button changed color on green"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            blocking_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch)
            blocking_switch.click()
            time.sleep(1)
            switcher = base_page.is_visible('xpath', SettingsLocators.AdBlockerSwitchColorGreen)
            switcher_color = switcher.value_of_css_property('background-color')
            assert switcher_color == 'rgba(135, 171, 73, 1)'
            qase.create_passed_result(case=261, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=261, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f'Button color not changed\n{ex}')
