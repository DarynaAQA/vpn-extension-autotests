import os
from dotenv import load_dotenv
load_dotenv()
from locators.settings_locators import SettingsLocators, ReloadPopUpLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.base_locators import BaseLocators, PremiumBenefits
from pages.auth_ext_page import AuthExtPage
from locators.account_locators import AccountLocators
import time


class TestSmartFilters:

    def test_clickability_smart_filters_switch(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 309
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on the smart filters checkbox
        6.Make sure icon filter checkbox changed color on green"""
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
        smart_filter_switch = base_page.is_clickable('id', SettingsLocators.SmartFiltersSwitch)
        smart_filter_switch.click()
        time.sleep(1)
        smart_filter_switch = base_page.is_visible('xpath', ReloadPopUpLocators.SMART_FILTERS_SWITCH)
        smart_filter_color = smart_filter_switch.value_of_css_property('background-color')
        try:
            assert smart_filter_color == 'rgba(135, 171, 73, 1)'
            qase.create_passed_result(case=309, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=309, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Smart filter checkbox not clickable\n {ex}")

    def test_displaying_smart_filters_icon_after_activating_switch(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 310
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on the smart filters checkbox
        6.Make sure icon changed color on green"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            smart_filter_switch = base_page.is_clickable('id', SettingsLocators.SmartFiltersSwitch)
            smart_filter_switch.click()
            time.sleep(1)
            icon_smart_filter = base_page.is_visible('id', BaseLocators.IndicatorSmartFilters)
            color_icon_smart_filter = icon_smart_filter.value_of_css_property('fill')
            assert color_icon_smart_filter == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=310, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=310, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Icon color not changed\n {ex}")

    def test_displaying_smart_filters_icon_after_deactivating_switch(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 311
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on the smart filters checkbox
        6.Click on the smart filters checkbox again
        7.Color icon smart filters checkbox must be changed to default color"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            smart_filter_switch = base_page.is_clickable('id', SettingsLocators.SmartFiltersSwitch)
            smart_filter_switch.click()
            smart_filter_switch.click()
            time.sleep(1)
            icon_smart_filter = base_page.is_visible('id', BaseLocators.IndicatorSmartFilters)
            color_icon_smart_filter = icon_smart_filter.value_of_css_property('fill')
            assert color_icon_smart_filter == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=311, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=311, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Icon color not changed\n {ex}")

    def test_clickability_smart_filters_websites_header(self, setup_driver, launch_methods, qase_run_id):
        """ID 318
           1.Go to main page
           2.Click on the burger menu
           3.Click on the "Settings"
           4.Click on the "Manage" button near smart filters checkbox
           5.Click on the Title "Smart filters for websites"
           5.Make sure user has been redirected to back page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            title = base_page.is_clickable('id', ReloadPopUpLocators.SMART_FILTERS_FOR_WEBSITE_TITLE)
            title.click()
            settings = base_page.is_visible('id', ReloadPopUpLocators.SETTINGS_TITLE)
            assert settings.text == 'Settings'
            qase.create_passed_result(case=318, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=318, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Title 'Smart filters for websites' not is clickable\n {ex}")

    def test_clickability_back_arrow(self, setup_driver, launch_methods, qase_run_id):
        """ID 319
           1.Go to main page
           2.Click on the burger menu
           3.Click on the "Settings"
           4.Click on the "Manage" button near smart filters checkbox
           5.Click on the back arrow button"
           5.Make sure user has been redirected to back page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            back_arrow_button = base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            settings = base_page.is_visible('id', ReloadPopUpLocators.SETTINGS_TITLE)
            assert settings.text == 'Settings'
            qase.create_passed_result(case=319, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=319, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Back arrow button not is clickable\n {ex}")

    def test_clickability_add_website_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 320
           1.Go to main page
           2.Click on the burger menu
           3.Click on the "Settings"
           4.Click on the "Manage" button near smart filters checkbox
           5.Click on the "Add website" button
           5.Make sure all elements on the page is visible"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://example.com')
            add_web_site_button = base_page.is_clickable('id',
                                                         ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            example_site = base_page.is_visible('xpath', ReloadPopUpLocators.ITEM_SITE)
            assert example_site is not None
            qase.create_passed_result(case=320, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=320, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements are displayed on page\n {ex}")

    def test_available_quantity_added_websites_premium_user(self, setup_driver, launch_methods, qase_run_id):
        """ID 322
           1.Go to main page
           2.Click on the burger menu
           3.Click on the "Settings"
           4.Click on the "Manage" button near smart filters checkbox
           5.Add 4 websites
           5.Make sure user can add more 3 websites"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            authx = AuthExtPage(setup_driver)
            authx.login_premium_user()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()

            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://example.com')
            add_website_button = base_page.is_clickable('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            first_website = base_page.is_visible('xpath', ReloadPopUpLocators.ITEM_SITE)
            assert first_website is not None
            delete_button = base_page.is_clickable('class_name', ReloadPopUpLocators.BUTTON_REMOVE).click()
            qase.create_passed_result(case=322, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=322, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"The user cannot add more than three websites\n {ex}")


    def test_under_add_website_button_field_searching_website_displayed(self, setup_driver, launch_methods,
                                                                        qase_run_id):
        """
        ID 323
        1.Go to main page
        2.Click to burger menu
        3.Click to settings
        4.Click on the "Manage" button near smart filters checkbox
        5.Make sure search website is visible"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            authx = AuthExtPage(setup_driver)
            authx.login_premium_user()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            website_search = base_page.is_visible('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            assert website_search.is_displayed()
            qase.create_passed_result(case=323, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=323, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Search website not visible\n {ex}")

    def test_successful_addition_of_thee_sites_for_free_user(self, setup_driver, launch_methods, qase_run_id):
        """ID 344
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click to Settings
        4.Click on the "Manage" button near smart filters checkbox
        5.Added 3 websites
        6.Make sure user can add 3 websites on the list"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://example.com')
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()

            """add second website"""

            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://example2.com')
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()

            """add third website"""

            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://example3.com')
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()

            first_website = base_page.is_visible('xpath', ReloadPopUpLocators.ITEM_SITE)
            second_website = base_page.is_visible('xpath', ReloadPopUpLocators.ITEM_SITE_2)
            third_website = base_page.is_present('xpath', ReloadPopUpLocators.ITEM_SITE_3)
            assert first_website.is_displayed()
            assert second_website.is_displayed()
            assert third_website.is_displayed()
            qase.create_passed_result(case=344, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=344, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"User cant add three websites on the list\n {ex}")

    def test_button_add_isnt_available_when_field_input_url_empty(self, setup_driver, launch_methods, qase_run_id):
        """ID 327
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Field for add websites must be cleared
           6.If input field is empty,'Save' button must be not clickable and has grey color"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()

            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.clear()
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS)
            add_button_color = add_website_button.value_of_css_property('background-color')
            assert add_button_color == 'rgba(215, 222, 237, 1)'
            qase.create_passed_result(case=327, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=327, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Save button is not grey color\n {ex}")

    def test_button_add_is_available_when_field_input_url_empty(self, setup_driver, launch_methods, qase_run_id):
        """ID 328
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Enter some text in input field
           6.If input field not empty,'Save' button must be clickable and has green color"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('test')
            time.sleep(1)
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS)
            add_button_color = add_website_button.value_of_css_property('background-color')
            assert add_button_color == 'rgba(135, 171, 73, 1)'
            qase.create_passed_result(case=328, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=328, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Save button is not green color\n {ex}")

    def test_clickability_add_button_when_entering_incorrect_url(self, setup_driver, launch_methods, qase_run_id):
        """ID 326
          STEPS:
          1.Go to main page
          2.Click on the burger menu
          3.Click to Settings
          4.Click on the "Manage" button near smart filters checkbox
          5.Enter incorrect url in the input field
          6.If input field has incorrect url,'Save' button must be clickable and has green color"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('1234')
            time.sleep(1)
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS)
            add_website_button.click()
            add_button_color = add_website_button.value_of_css_property('background-color')
            assert add_button_color == 'rgba(135, 171, 73, 1)'
            qase.create_passed_result(case=326, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=326, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Save button is not green color\n {ex}")

    def test_clickability_add_button_when_entering_correct_url(self, setup_driver, launch_methods, qase_run_id):
        """ID 329
          STEPS:
          1.Go to main page
          2.Click on the burger menu
          3.Click to Settings
          4.Click on the "Manage" button near smart filters checkbox
          5.Enter valid url in input field
          6.If input field has correct url,'Save' button must be clickable and has green color"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://google.com')
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS)
            time.sleep(1)
            save_button_color = add_website_button.value_of_css_property('background-color')
            assert save_button_color == 'rgba(135, 171, 73, 1)'
            qase.create_passed_result(case=329, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=329, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Save button is not green color\n {ex}")

    def test_clickability_add_button_when_already_added_website(self, setup_driver, launch_methods, qase_run_id):
        """ID 330
          STEPS:
          1.Go to main page
          2.Click on the burger menu
          3.Click to Settings
          4.Click on the "Manage" button near smart filters checkbox
          5.Add website
          6.Add mirror website
          7.Make sure after click Save button user can see pop up with error text"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://google.com')
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            input_website = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input_website.click()
            input_website.send_keys('https://google.com')
            add_website_button = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            error_pop_up = base_page.is_visible('class_name', ReloadPopUpLocators.ERROR_TEXT_ALERT)
            assert error_pop_up.text == 'This domain has already been added to the list'
            qase.create_passed_result(case=330, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=330, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Error pop up not visible\n {ex}")

    def test_displaying_pop_up_enabling_smart_filters_switch(self, setup_driver, launch_methods, qase_run_id):
        """ID 312
         STEPS:
         1.Go to main page
         2.Click on the burger menu
         3.Click to Settings
         4.Click on the "smart filters for website" switch
         5.Find pop-up
         6.Make sure user can see pop-up with text "Reload now", notification text & X button"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            smart_filters_switch = base_page.is_clickable('xpath', ReloadPopUpLocators.SMART_FILTERS_SWITCH).click()
            reload_now_element = base_page.is_visible('id', ReloadPopUpLocators.ReloadButton)
            notification_text = base_page.is_visible('id', ReloadPopUpLocators.NOTIFICATION_TEXT)
            button_x = base_page.is_visible('id', ReloadPopUpLocators.CLOSE_X_BUTTON)
            assert reload_now_element.text == 'Reload Now'
            assert notification_text.text == 'Reload the website page to apply the changes'
            assert button_x.is_displayed()
            qase.create_passed_result(case=312, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=312, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements of pop-up is visible\n {ex}")

    def test_displaying_pop_up_turning_off_smart_filters_switch(self, setup_driver, launch_methods, qase_run_id):
        """ID 313
         STEPS:
         1.Go to main page
         2.Click on the burger menu
         3.Click to Settings
         4.Click on the "smart filters for website" switch
         5.Click on the "smart filters for website" switch again
         6.Find pop-up
         7.Make sure user can see pop-up with text "Reload now", notification text & X button"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            smart_filters_switch = base_page.is_clickable('xpath', ReloadPopUpLocators.SMART_FILTERS_SWITCH)
            smart_filters_switch.click()
            smart_filters_switch.click()
            reload_now_element = base_page.is_visible('id', ReloadPopUpLocators.ReloadButton)
            notification_text = base_page.is_visible('id', ReloadPopUpLocators.NOTIFICATION_TEXT)
            button_x = base_page.is_visible('id', ReloadPopUpLocators.CLOSE_X_BUTTON)
            assert reload_now_element.text == 'Reload Now'
            assert notification_text.text == 'Reload the website page to apply the changes'
            assert button_x.is_displayed()
            qase.create_passed_result(case=313, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=313, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements of pop-up is visible\n {ex}")

    def test_clickability_manage_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 316
            STEPS:
            1.Go to main page
            2.Click on the burger menu
            3.Click to Settings
            4.Click on the "Manage" button near smart filters checkbox
            6.Make sure after click user go to next page
            7.User can see smart filters title, back arrow, 'add website' button, text “No sites to filter yet”, text "Create VPN rules for selected websites" """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            title = base_page.is_visible('id', ReloadPopUpLocators.SMART_FILTERS_FOR_WEBSITE_TITLE)
            add_website = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS)
            information_block_text = base_page.is_visible('id', ReloadPopUpLocators.INFORMATION_TEXT)
            assert title is not None
            assert add_website is not None
            assert information_block_text.text == 'Create exceptions for selected websites'
            qase.create_passed_result(case=316, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=316, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements on page is visible\n {ex}")

    def test_display_correct_number_websites_after_adding_new_site(self, setup_driver, launch_methods, qase_run_id):
        """ID 314
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           6.Add new website
           7.Make sure that the number of sites that can be added has decreased"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://example.com')
            add_web_site = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            title = base_page.is_visible('id', ReloadPopUpLocators.SMART_FILTERS_FOR_WEBSITE_TITLE).click()
            quantity = base_page.is_visible('xpath', ReloadPopUpLocators.QuantitySites)
            assert quantity.text == 'Exceptions: 1'
            qase.create_passed_result(case=314, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=314, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Quantity web sites no changed or changed with incorrect\n {ex}")

    def test_displaying_correct_number_sites_after_deleting_site(self, setup_driver, launch_methods, qase_run_id):
        """ID 315
          STEPS:
          1.Go to main page
          2.Click on the burger menu
          3.Click to Settings
          4.Click on the "Manage" button near smart filters checkbox
          6.Add new website
          7.Delete added website
          7.Make sure that the number of sites matches the default number of 3"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://example.com')
            add_web_site = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://example2.com')
            add_web_site = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            delete = base_page.is_clickable('class_name', ReloadPopUpLocators.BUTTON_REMOVE).click()
            title = base_page.is_visible('id', ReloadPopUpLocators.SMART_FILTERS_FOR_WEBSITE_TITLE).click()
            quantity = base_page.is_visible('xpath', ReloadPopUpLocators.QuantitySites)
            assert quantity.text == 'Exceptions: 1'
            qase.create_passed_result(case=315, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=315, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Quantity web sites no changed or changed with incorrect\n {ex}")

    def test_clickability_delete_button(self, setup_driver, launch_methods, qase_run_id):
        """ID 347
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Add website
           6.Click on the website button
           7.Click delete button
           8.Make sure user can see pop up with web elements"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            manage = base_page.is_clickable('id', ReloadPopUpLocators.MANAGE_BUTTON_SMART_FILTERS).click()
            input = base_page.is_clickable('id', ReloadPopUpLocators.ENTER_WEB_SITE_INPUT)
            input.click()
            input.send_keys('https://example.com')
            add_web_site = base_page.is_visible('id', ReloadPopUpLocators.ADD_WEB_SITE_BUTTON_SMART_FILTERS).click()
            website = base_page.is_visible('xpath', ReloadPopUpLocators.ITEM_SITE)
            delete = base_page.is_clickable('class_name', ReloadPopUpLocators.BUTTON_REMOVE).click()
            assert base_page.invisibility_of_element_located('xpath', ReloadPopUpLocators.ITEM_SITE)
            qase.create_passed_result(case=347, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=347, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Not all elements is visible\n {ex}")

    def test_сlickability_button_selecting_connection_free_user(self, setup_driver, launch_methods, qase_run_id):
        """ID 360
        STEPS:
        1.Go to main page
        2.Click on the burger menu
        3.Click to Settings
        4.Click on the "Manage" button near smart filters checkbox
        5.Add website
        6.Click on the website button
        7.Click on the "By default" button
        8.Make sure the server selection for Smart filter screen is displayed"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            server = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            input = base_page.is_visible('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            server_active = base_page.is_visible('class_name', ReloadPopUpLocators.ServerActive)
            servers = base_page.is_visible('id', ReloadPopUpLocators.Servers)
            favorites = base_page.is_visible('id', ReloadPopUpLocators.FavoritesServers)
            unlock_button = base_page.is_visible('id', ReloadPopUpLocators.UnlockButton)
            title = base_page.is_visible('id', BaseLocators.AvailableLocations)
            back_arrow = base_page.is_visible('id', AccountLocators.GoBackButton)
            assert input.is_displayed()
            assert servers.is_displayed()
            assert server_active.is_displayed()
            assert favorites.is_displayed()
            assert unlock_button.is_displayed()
            assert title.is_displayed()
            assert back_arrow.is_displayed()
            qase.create_passed_result(case=360, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=360, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"The server selection for Smart filter screen not is displayed\n {ex}")

    def test_сlickability_button_selecting_connection_premium_user(self, setup_driver, launch_methods, qase_run_id):
        """ID 361
        STEPS:
        1.Go to main page with premium user
        2.Click on the burger menu
        3.Click to Settings
        4.Click on the "Manage" button near smart filters checkbox
        5.Add website
        6.Click on the website button
        7.Click on the "By default" button
        8.Make sure the server selection for Smart filter screen is displayed"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            auth_methods = AuthExtPage(setup_driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            server = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            input = base_page.is_visible('id', ReloadPopUpLocators.WEB_SITE_INPUT)
            server_active = base_page.is_visible('class_name', ReloadPopUpLocators.ServerActive)
            servers = base_page.is_visible('id', ReloadPopUpLocators.Servers)
            favorites = base_page.is_visible('id', ReloadPopUpLocators.FavoritesServers)
            title = base_page.is_visible('id', BaseLocators.AvailableLocations)
            back_arrow = base_page.is_visible('id', AccountLocators.GoBackButton)
            assert back_arrow.is_displayed()
            assert input.is_displayed()
            assert servers.is_displayed()
            assert server_active.is_displayed()
            assert favorites.is_displayed()
            assert title.is_displayed()
            qase.create_passed_result(case=361, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=361, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"The server selection for Smart filter screen not is displayed\n {ex}")

    def test_clickability_premium_button_premium_server_user_free(self, setup_driver, launch_methods, qase_run_id):
        """ID 364
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Add website
           6.Click on the website button
           7.Click on the "By default" button
           8.Click on the premium server button
           8.Make sure user go to /order page """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            auth_methods = AuthExtPage(setup_driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            server = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            unlock_button = base_page.is_visible('id', ReloadPopUpLocators.UnlockButton).click()
            proceed_to_order = base_page.is_clickable('id', PremiumBenefits.StartOrdering).click()
            base_page.activate_redirect_page()
            url = base_page.get_current_url()
            assert url == os.getenv("ORDER_LINK")
            qase.create_passed_result(case=364, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=364, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Redirect on /order did not originate\n {ex}")

    def test_clickability_free_server_free_user(self, setup_driver, launch_methods, qase_run_id):
        """ID 364
           STEPS:
           1.Go to main page
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Add website
           6.Click on the website button
           7.Click on the "By default" button
           8.Click on the free server button
           8.Make sure user go to /order page"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            location = base_page.is_visible('id', SidebarMenuLocators.StatusCountry).text
            server = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            server_active = base_page.is_clickable('class_name', ReloadPopUpLocators.ServerActive).click()
            base_page.close_advertising_pop_up()
            time.sleep(2)
            button_red = base_page.is_clickable('class_name', BaseLocators.BUTTON_CONNECTED_RED)
            new_location = base_page.is_visible('id', SidebarMenuLocators.StatusCountry).text
            print(new_location)
            assert location != new_location
            qase.create_passed_result(case=365, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=365, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Displaying of Smart filter for website window and the selected free server is not displayed in the VPN field\n {ex}")

    def test_clickability_premium_server_premium_user(self, setup_driver, launch_methods, qase_run_id):
        """ID 366
           STEPS:
           1.Go to main page with premium user
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Add website
           6.Click on the website button
           7.Click on the "By default" button
           8.Click on the premium server button
           8.Make sure user go to /order page """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            auth_methods = AuthExtPage(setup_driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            server = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            albania_server = base_page.is_clickable('xpath', ReloadPopUpLocators.ALBANIA_SERVER_PREMIUM).click()
            button_red = base_page.is_clickable('class_name', BaseLocators.BUTTON_CONNECTED_RED)
            location = base_page.is_visible('id', SidebarMenuLocators.StatusCountry).text
            print(location)
            assert location == 'Your location:\nTirana #5'
            qase.create_passed_result(case=366, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=366, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Displaying of Smart filter for website window and the selected free server is not displayed in the VPN field\n {ex}")

    def test_clickability_back_arrow_select_servers(self, setup_driver, launch_methods, qase_run_id):
        """ID 368
           STEPS:
           1.Go to main page with premium user
           2.Click on the burger menu
           3.Click to Settings
           4.Click on the "Manage" button near smart filters checkbox
           5.Add website
           6.Click on the website button
           7.Click on the "By default" button
           8.Click on the Back arrow button
           8.Make sure the Smart Filter for WebSite window opens"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            server = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            back_arrow = base_page.is_visible('class_name', SettingsLocators.GoBackButton).click()
            title = base_page.is_visible('class_name', BaseLocators.LogoVpn)
            assert title.is_displayed()
            qase.create_passed_result(case=368, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=368, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"The Smart Filter for Web Site window don't opens\n {ex}")
