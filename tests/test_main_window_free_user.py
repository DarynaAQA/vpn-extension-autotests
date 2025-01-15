from base_classes.api_requests import ApiRequests
from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.site_locators import SiteLocators
from locators.settings_locators import SettingsLocators
from locators.base_locators import PremiumBenefits
from selenium.webdriver.remote.webelement import WebElement
import time



class TestMainWindowFreeUser:

    def test_free_user_main_window(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Refresh page  with the extension
            4. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            burger_menu_button = base_page.burger_menu_button_is_present()
            logo_vpn = base_page.logo_vpn_is_present()
            login_icon = base_page.login_icon_is_present()
            button_select_country = base_page.select_country_button_is_present()
            current_location = base_page.current_location_is_present()
            connection_protection = base_page.connection_protection_is_present()
            indicator_autoconnect = base_page.indicator_autoconnect_is_present()
            indicator_adblocker = base_page.indicator_adblocker_is_present()
            indicator_cookies = base_page.indicator_cookies_is_present()
            indicator_trackers = base_page.indicator_trackers_is_present()
            indicator_history = base_page.indicator_history_is_present()
            indicator_smart_filter = base_page.indicator_smart_filters_is_present()
            assert isinstance(burger_menu_button, WebElement)
            assert isinstance(logo_vpn, WebElement)
            assert isinstance(login_icon, WebElement)
            assert isinstance(button_select_country, WebElement)
            assert isinstance(current_location, WebElement)
            assert isinstance(connection_protection, WebElement)
            assert isinstance(indicator_autoconnect, WebElement)
            assert isinstance(indicator_adblocker, WebElement)
            assert isinstance(indicator_cookies, WebElement)
            assert isinstance(indicator_trackers, WebElement)
            assert isinstance(indicator_history, WebElement)
            assert isinstance(indicator_history, WebElement)
            assert isinstance(indicator_smart_filter, WebElement)
            qase.create_passed_result(case=38, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=38, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_click_burger_menu(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Check for presence of sidebar menu window
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.find_element('class_name', BaseLocators.BurgerMenuButton).click()
            side_bar_window = base_page.side_bar_window_is_present()
            assert isinstance(side_bar_window, WebElement)
            qase.create_passed_result(case=42, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=42, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_current_location(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Refresh page with the extension
            4. Get the current city by sending an API request GET ip
            5. Get the text of the current city from a web element
            6. Compare city names with each other
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            req_api = ApiRequests()
            current_location_backend = req_api.get_current_city()
            base_page.is_visible('id', BaseLocators.CurrentLocation)
            current_location_extension_full = base_page.get_element_text('id', BaseLocators.CurrentLocation)
            current_location_extension = current_location_extension_full.split(":")[1].strip()
            assert current_location_extension == current_location_backend
            qase.create_passed_result(case=57, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=57, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    # def test_load_indicator(self, setup_driver, qase_run_id, launch_methods):
    #     """
    #         STEPS:
    #
    #     """
    #     base_page, privacy_policy, sidebar_menu, qase = launch_methods
    #     base_page.activate_page()
    #     privacy_policy.accept_privacy_policy()
    #     base_page.refresh_page()
    #     base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
    #
    #     req_api = ApiRequests()
    #     req_api.url = f"https://ygowyj8u.ohzavie2.xyz/v1/network/info/leading?type=public"
    #     servers_data = req_api.parse_free_servers()
    #     print(servers_data)
    #
    #     img_parse = ImageParser()
    #     file_name = os.path.join('tests', 'png', 'connection-status.png')
    #     full_path = os.path.join(os.getcwd(), file_name)
    #     png_to_compare = img_parse.read_png_content(full_path)
    #
    #     i = 2
    #     while i <= len(servers_data):
    #         img_elem = base_page.is_present('xpath',
    #         f'//*[@id="qa-main"]/div/div[8]/div[3]/div/div[{i}]/div[3]/div')
    #         time.sleep(1)
    #         server_load_screenshot = img_elem.screenshot_as_png
    #         server_id = servers_data[f"{i}"][0]
    #         load = servers_data[f"{i}"][2]
    #         try:
    #             assert img_parse.compare_elem_png(server_load_screenshot, png_to_compare), (f"Server is overloaded. "
    #                                         f"ID={server_id}, Load= {servers_data[f'{i}'][2]}")
    #             assert float(servers_data[f'{i}'][2]) <= 70.01, 'Icon is green but server is overloaded'
    #             qase.create_passed_result(case=58, test_run_id=qase_run_id, time=time.time()-base_page.time)
    #         except Exception as ex:
    #             folder = 'tests/images'
    #             if not os.path.exists(folder):
    #                 os.makedirs(folder)
    #             img_parse.save_as_png(os.path.join(folder, f'Try{i}.png'), server_load_screenshot)
    #             qase.create_failed_result(case=58, test_run_id=qase_run_id, time=time.time()-base_page.time,
    #                                       comment=f"Server name= {servers_data[f'{i}'][1]}, Server id= {server_id}: "
    #                                               f",Load: {load}. TEST FAILED\n REASON: {ex}\n")
    #         i += 1

    def test_click_button_select_country(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Select country button
            4. Check for presence the Available servers header
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.find_element('class_name', BaseLocators.SelectServer).click()
            title = base_page.title_available_servers_is_present()
            assert isinstance(title, WebElement)
            qase.create_passed_result(case=60, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=60, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_panel_indicators_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Refresh page with the extension
            4. Check for presence of indicators panel
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            panel_indicators = base_page.panel_indicators_is_present()
            assert isinstance(panel_indicators, WebElement)
            qase.create_passed_result(case=83, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=83, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Panel indicators are missing \n {ex}")

    def test_indicator_autoconnect_activated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Settings button
            5. Click on the autoconnect switcher
            6. Click on the go back button
            7. Hover the cursor over the auto-connect indicator
            8. Check for presence pop up with autoconnect status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.AutoconnectSwitch).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            time.sleep(1)
            indicator = base_page.is_visible('id', BaseLocators.IndicatorAutoconnect)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=85, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=85, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_autoconnect_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Hover the cursor over the auto-connect indicator
            4. Check for presence pop up with autoconnect status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorAutoconnect)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=86, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=86, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_adblocker_activated(self, setup_driver, qase_run_id, launch_methods):
        """
           STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Settings button
            5. Click on the adblocker switcher
            6. Refresh page with the extension
            7. Click on the go back button
            8. Hover the cursor over the adblocker indicator
            9. Check for presence pop up with adblocker status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.AdBlockerSwitch).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            time.sleep(1)
            indicator = base_page.is_visible('id', BaseLocators.IndicatorAdblocker)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=88, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=88, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_adblocker_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Hover the cursor over the adblocker indicator
            4. Check for presence pop up with adblocker status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorAdblocker)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=89, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=89, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_cookies_activated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Settings button
            5. Click on the cookies switcher
            6. Refresh page with the extension
            7. Click on the go back button
            8. Hover the cursor over the cookies indicator
            9. Check for presence pop up with cookies status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.CookiesSwitch).click()
            x_button = base_page.is_clickable('xpath', BaseLocators.CLOSE_BUTTON).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorCookies)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=94, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=94, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_cookies_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Hover the cursor over the cookies indicator
            4. Check for presence pop up with cookies status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorCookies)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=95, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=95, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_trackers_activated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Settings button
            5. Click on the trackers switcher
            6. Refresh page with the extension
            7. Click on the go back button
            8. Hover the cursor over the trackers indicator
            9. Check for presence pop up with trackers status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.TrackersSwitch).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            time.sleep(1)
            indicator = base_page.is_visible('id', BaseLocators.IndicatorTrackers)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=97, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=97, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_trackers_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Hover the cursor over the trackers indicator
            4. Check for presence pop up with trackers status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorTrackers)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=98, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=98, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_history_activated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Settings button
            5. Click on the history switcher
            6. Refresh page with the extension
            7. Click on the go back button
            8. Hover the cursor over the history indicator
            9. Check for presence pop up with history status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.HistorySwitch).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            time.sleep(1)
            indicator = base_page.is_visible('id', BaseLocators.IndicatorHistory)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=100, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=100, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_history_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Hover the cursor over the history indicator
            4. Check for presence pop up with history status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorHistory)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=101, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=101, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_smart_filters_activated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the Burger menu button
            4. Click on the Settings button
            5. Click on the Smart filters switcher
            6. Refresh page with the extension
            7. Click on the go back button
            8. Hover the cursor over the Smart filters indicator
            9. Check for presence pop up with Smart filters status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.is_clickable('id', SettingsLocators.SmartFiltersSwitch).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            time.sleep(1)
            indicator = base_page.is_visible('id', BaseLocators.IndicatorSmartFilters)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(135, 171, 73)'
            qase.create_passed_result(case=103, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=103, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_indicator_smart_filters_deactivated(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Hover the cursor over the Smart filters indicator
            4. Check for presence pop up with Smart filters status
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            indicator = base_page.is_visible('id', BaseLocators.IndicatorSmartFilters)
            indicator_color = indicator.value_of_css_property('fill')
            assert indicator_color == 'rgb(215, 222, 237)'
            qase.create_passed_result(case=104, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=104, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_banner_premium_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Check for presence of banner "More options with Premium"
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            banner_premium = base_page.is_present('id', BaseLocators.BannerPremium)
            assert banner_premium is not None
            qase.create_passed_result(case=105, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=105, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_banner_premium_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the banner "More options with Premium"
            4. Check for presence of window with Premium benefits
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_present('id', BaseLocators.BannerPremium).click()
            window_premium_benefits = base_page.is_present('class_name', PremiumBenefits.WindowPremiumBenefits)
            assert isinstance(window_premium_benefits, WebElement)
            qase.create_passed_result(case=106, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=106, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_close_button_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the banner "More options with Premium"
            4. Click on the close button
            5. Check for presence of VPN logo
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('id', BaseLocators.BannerPremium).click()
            close_button = base_page.is_clickable('class_name', PremiumBenefits.CloseButton)
            close_button.click()
            logo_vpn = base_page.is_present('class_name', BaseLocators.LogoVpn)
            assert isinstance(logo_vpn, WebElement)
            qase.create_passed_result(case=107, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=107, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_button_start_ordering_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the banner "More options with Premium"
            4. Click on the "Proceed to order" button
            5. Activate redirect page
            6. Check for presence of VPN logo on the website
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('id', BaseLocators.BannerPremium).click()
            base_page.is_clickable('id', PremiumBenefits.StartOrdering).click()
            base_page.activate_redirect_page()
            logo_vpn = base_page.is_present('xpath', SiteLocators.LogoVpn)
            assert isinstance(logo_vpn, WebElement)
            qase.create_passed_result(case=109, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=109, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")
