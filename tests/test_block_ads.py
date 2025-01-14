from locators.settings_locators import SettingsLocators, ReloadPopUpLocators
from locators.sidebar_menu_locators import SidebarMenuLocators

import time


class TestBlockAds:

    def test_displaying_ad_blocking_icon_after_activating_switch(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 290
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on the Block ads checkbox
        6.Make sure icon Block ads changed color on green"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_ads_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            time.sleep(1)
            icon = base_page.is_visible('id', ReloadPopUpLocators.ICON_ADD_BLOCKER)
            icon_color = icon.value_of_css_property('fill')
            assert icon_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=290, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=290, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Icon 'Block ads' is not change color to green\n {ex}")

    def test_displaying_ad_blocking_icon_after_deactivating_switch(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 291
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on the Block ads checkbox twice
        6.Make sure icon Block ads changed color on grey"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_ads_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch)
            block_ads_switch.click()
            time.sleep(1)
            block_ads_switch.click()
            time.sleep(1)
            icon = base_page.is_visible('id', ReloadPopUpLocators.ICON_ADD_BLOCKER)
            icon_color = icon.value_of_css_property('fill')
            assert icon_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=291, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=291, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Icon 'Block ads' is not change color to grey\n {ex}")

    def test_displaying_pop_up_window_turning_ad_blocking_switch(self, setup_driver, launch_methods, qase_run_id):
        """ID 285
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click to Settings
        4.Click on the "Block ads" switch
        5.Find pop-up
        6.Make sure user can see pop-up with text "Reload now", notification text & X button"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_ads_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            reload_now_element = base_page.is_visible('class_name', ReloadPopUpLocators.RELOAD_NOW_POP_UP)
            notification_text = base_page.is_visible('id', ReloadPopUpLocators.NOTIFICATION_TEXT)
            button_x = base_page.is_visible('class_name', ReloadPopUpLocators.X_BUTTON)
            assert reload_now_element.text == 'Reload Now'
            assert notification_text.text == 'Reload the website page to apply the changes'
            assert button_x.is_displayed()
            qase.create_passed_result(case=285, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=285, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements of pop-up is visible\n {ex}")

    def test_clickability_manage_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 262
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click to Settings
        4.Click on the "Manage" button near smart block ads
        6.Make sure after click user go to next page
        7.User can see title, back arrow button, input field, information text """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            title = base_page.is_visible('id', ReloadPopUpLocators.AddBlockingTitle)
            back_arrow = base_page.is_visible('class_name', SettingsLocators.GoBackButton)
            website_input = base_page.is_visible('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON)
            information_text = base_page.is_visible('class_name', ReloadPopUpLocators.INFORMATION_TEXT_AD_BLOCK)
            assert title.is_displayed()
            assert back_arrow.is_displayed()
            assert website_input.is_displayed()
            assert add_website_button.is_displayed()
            assert information_text.is_displayed()
            qase.create_passed_result(case=262, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=262, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements on page is visible\n {ex}")

    def test_clickability_add_website_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 265
            STEPS:
            1.Go to main page
            2.Click on the burger menu
            3.Click to Settings
            4.Click on the "Manage" button near block ads checkbox
            6.Enter exemple website in input field
            7.Click "add website" button"
            8.Make sure last added website is displayed on the page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            website_input = base_page.is_visible('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            website_input.click()
            website_input.send_keys('https://example.com')
            add_website_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            web_site_user = base_page.is_visible('xpath', ReloadPopUpLocators.ITEM_SITE)
            assert web_site_user.is_displayed()
            qase.create_passed_result(case=265, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=265, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Add website buton is not clickable\n {ex}")

    def test_visiting_website_with_ad_blocking_enabled(self, setup_driver, launch_methods, qase_run_id):
        """ID 275
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "block ads" switch
           6.Go to https://ads-blocker.com/ru/test-blokirovshchika-reklamy/
           7.Get data from console
           8.Make sure advertising banner blocked"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_ads_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            base_page.refresh_page()
            base_page.open_url('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            logs = setup_driver.get_log('browser')
            ad_blocked = False
            for log in logs:
                if 'message' in log and 'ERR_BLOCKED_BY_CLIENT' in log['message']:
                    ad_blocked = True
                    break
            if ad_blocked:
                qase.create_passed_result(case=275, test_run_id=qase_run_id, time=time.time() - base_page.time)
            else:
                raise AssertionError("Advertising is blocked, exception not work")
        except AssertionError as ex:
            qase.create_failed_result(case=275, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Advertising is not blocked, exception not work\n {ex}")

    def test_visiting_website_added_exceptions_ad_blocking_enabled(self, setup_driver, launch_methods, qase_run_id):
        """ID 273
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Add website https://ads-blocker.com/ru/test-blokirovshchika-reklamy/ to exception
           5.Click on the "block ads" switch
           6.Go to https://ads-blocker.com/ru/test-blokirovshchika-reklamy/
           7.Get data from console
           8.Make sure advertising banner not blocked"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            add_website = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            back_button = base_page.is_clickable('id', ReloadPopUpLocators.AddBlockingTitle).click()
            block_ads_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            base_page.open_url('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            logs = setup_driver.get_log('browser')
            ad_blocked = False
            for log in logs:
                if 'message' in log and 'ERR_BLOCKED_BY_CLIENT' not in log['message']:
                    ad_blocked = True
                    break
            if ad_blocked:
                qase.create_passed_result(case=273, test_run_id=qase_run_id, time=time.time() - base_page.time)
            else:
                raise AssertionError("Advertising is blocked, exception not work")
        except AssertionError as ex:
            qase.create_failed_result(case=273, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Advertising is blocked, exception not work\n {ex}")

    def test_visiting_website_added_exceptions_ad_blocking_disabled(self, setup_driver, launch_methods, qase_run_id):
        """ID 274
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Add website to exception
           5."Block ads" switch is off
           6.Go to https://ads-blocker.com/ru/test-blokirovshchika-reklamy/
           7.Get data from console
           8.Make sure advertising banner not blocked"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            block_ads_switch = base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            add_website = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            base_page.open_url('https://ads-blocker.com/ru/test-blokirovshchika-reklamy/')
            logs = setup_driver.get_log('browser')
            ad_blocked = False
            for log in logs:
                if 'message' in log and 'ERR_BLOCKED_BY_CLIENT' not in log['message']:
                    ad_blocked = True
                    break
            if ad_blocked:
                qase.create_passed_result(case=274, test_run_id=qase_run_id, time=time.time() - base_page.time)
            else:
                raise AssertionError("Advertising is blocked, exception not work")
        except AssertionError as ex:
            qase.create_failed_result(case=274, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Advertising is blocked, exception not work\n {ex}")
