import os

from locators.settings_locators import SettingsLocators, ReloadPopUpLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.base_locators import BaseLocators

import time


class TestChecksAddBlockSection:

    def test_button_add_website_isnt_aviable_when_input_url_empty(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 263
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        4.Click on the settings menu
        5.Click on the manage button
        6.Make sure if input field is empty, button must be not clickable"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            add_web_site_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON)
            if web_site_input.get_attribute('value') == '':
                assert not add_web_site_button.is_enabled()
                qase.create_passed_result(case=263, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=263, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Add website button is clickable\n {ex}")

    def test_button_add_website_aviable_when_input_url_empty(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 264
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        4.Click on the settings menu
        5.Click on the manage button
        6.Make sure if input field is not empty, button must be clickable"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input.click()
            web_site_input.send_keys('some_text')
            add_web_site_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON)
            if web_site_input.get_attribute('value') != '':
                assert add_web_site_button.is_enabled()
                qase.create_passed_result(case=264, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=264, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Add website button is not clickable\n {ex}")

    def test_clickability_ad_blocking_header(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 269
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        4.Click on the settings menu
        5.Click on the manage button
        6.Click on the "Add blocking" header
        7.Make sure user goin to back page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            add_blocking_header = base_page.is_clickable('id', ReloadPopUpLocators.AddBlockingTitle).click()
            settings_header = base_page.is_visible('id', ReloadPopUpLocators.SETTINGS_TITLE)
            assert settings_header.text == 'Settings'
            qase.create_passed_result(case=269, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=269, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"After click for 'Add blocking' redirect to back not done\n {ex}")

    def test_clickability_back_arrow_button(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 270
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        4.Click on the settings menu
        5.Click on the manage button
        6.Click on the "Add blocking" header
        7.Make sure user goin to back page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            back_arrow = base_page.is_clickable('id', ReloadPopUpLocators.AddBlockingTitle).click()
            settings_header = base_page.is_visible('id', ReloadPopUpLocators.SETTINGS_TITLE)
            assert settings_header.text == 'Settings'
            qase.create_passed_result(case=270, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=270, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f"After click for 'Back arrow' redirect to back not done\n {ex}")

    def test_website_when_entering_incorrect_ulr(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 271
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        4.Click on the settings menu
        5.Click on the manage button
        6.Enter not valid website address in url input
        7.Click on the add website button
        8.Make sure user must be look alert for invalid website address"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input.click()
            web_site_input.send_keys('g1g')
            add_web_site_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            web_site_incorrect_text = base_page.is_visible('class_name', ReloadPopUpLocators.INCORRECT_SITE_TEXT).text
            assert web_site_incorrect_text == 'Website address is incorrect'
            qase.create_passed_result(case=271, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=271, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f"User not see alert pop-up for incorrect website url\n {ex}")

    def test_website_when_entering_correct_ulr(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 272
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        4.Click on the settings menu
        5.Click on the manage button
        6.Enter valid website address in url input
        7.Click on the add website button
        8.Make sure website address must be added"""
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
            web_site_input_value = web_site_input.get_attribute('value').strip().split('//')
            user_website = web_site_input_value[1]
            add_web_site_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON)
            add_web_site_button.click()
            my_site_input = base_page.is_visible('xpath', f'//input[contains(@value, {user_website})]')
            assert my_site_input is not None
            qase.create_passed_result(case=272, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=272, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f"User web site not added to list\n {ex}")

    def test_checking_website_search(self, setup_driver, qase_run_id, launch_methods):
        """
          ID 276
          STEPS:
          1.Go to main page
          2.Click on the burger menu
          3.Click on the settings menu
          4.Click on the manage button
          5.Enter valid website address in url input
          6.Click on the add website button
          7.Enter second valid website address in url input
          8.Click on the add website button
          9.Enter 'google.com' on the search field
          10.Make sure only 'google.com' website are present in the list"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            # add google site
            web_site_input_search = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input_search.click()
            web_site_input_search.send_keys('https://google.com')
            google_site = web_site_input_search.get_attribute('value').strip().split('//')
            user_google_site = google_site[1]
            add_site_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            div_google_site = base_page.is_clickable('xpath', f'//div[contains(@value, {user_google_site})]')

            # add vpn site
            web_site_input_search = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input_search.click()
            web_site_input_search.send_keys(os.getenv("WEBSITE_LINK"))
            vpn_site = web_site_input_search.get_attribute('value').strip().split('//')
            user_vpn_site = vpn_site[1]
            add_site_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON)
            add_site_button.click()
            div_vpn_site = base_page.is_clickable('xpath', f'//div[contains(@value, {user_vpn_site})]')

            # search google site on the list
            search_input = base_page.is_clickable('xpath', ReloadPopUpLocators.INPUT_SEARCH_SITE)
            search_input.click()
            search_input.send_keys('google.com')
            assert user_google_site in div_google_site.text
            assert user_vpn_site not in div_vpn_site.text
            qase.create_passed_result(case=276, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=276, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f"User web site not found on the list\n {ex}")

    def test_adding_website_when_already_added_website(self, setup_driver, qase_run_id, launch_methods):
        """ID 292
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click on the settings menu
           4.Click on the manage button
           5.Enter valid website address in url input
           6.Enter previous website address in url input
           7.Make sure information alert message is visible, user can't be added identical sites"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input_search = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input_search.click()
            web_site_input_search.send_keys('https://google.com')
            add_site_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            web_site_input_search = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input_search.click()
            web_site_input_search.send_keys('https://google.com')
            add_site_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            error_text_alert = base_page.is_visible('class_name', ReloadPopUpLocators.ERROR_TEXT_ALERT)
            assert error_text_alert.text == 'This domain has already been added to the list'
            qase.create_passed_result(case=292, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=292, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f"Error alert not visible, the user cannot add a previously added site\n {ex}")

    def test_clickability_button_x_when_removing_site(self, setup_driver, qase_run_id, launch_methods):
        """ID 277
            STEPS:
            1.Go to main page
            2.Click on the burger menu
            3.Click on the settings menu
            4.Click on the manage button
            5.Enter valid website address in url input
            6.Find delete button "X" and click to delete site on the list
            7.Make sure site deleted on the list """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage_button = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON).click()
            web_site_input_search = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            web_site_input_search.click()
            web_site_input_search.send_keys('https://google.com')
            web_site_google = web_site_input_search.get_attribute('value').strip().split('//')
            web_site_google_text = web_site_google[1]
            add_site_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON).click()
            user_google_site_in_list = base_page.is_clickable('xpath',
                                                              f'//div[contains(@value, {web_site_google_text})]')
            delete_website = base_page.is_clickable('class_name', ReloadPopUpLocators.DELETE_WEBSITE_BUTTON_X).click()
            assert web_site_google_text not in user_google_site_in_list.text
            qase.create_passed_result(case=277, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=277, test_run_id=qase_run_id,
                                      time=time.time() - base_page.time,
                                      comment=f"Web site not deleted on the list\n {ex}")
