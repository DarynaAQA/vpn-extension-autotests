from pages.auth_ext_page import AuthExtPage
from selenium.webdriver.remote.webelement import WebElement
import time


class TestMainWindowPremiumUser:
    def test_premium_user_main_window(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Authorize a user with a premium subscription
            4. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        auth_methods = AuthExtPage(setup_driver)
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            burger_menu_button = base_page.burger_menu_button_is_present()
            logo_vpn = base_page.logo_vpn_is_present()
            logout_icon = base_page.log_out_is_present()
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
            assert isinstance(logout_icon, WebElement)
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
            qase.create_passed_result(case=110, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=110, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                  comment=f"Webelements are missing \n {ex}")




