from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.settings_locators import SettingsLocators
from selenium.webdriver.remote.webelement import WebElement
import time


class TestSettings:
    def test_settings_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on Settings button
            5. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            autoconnect_switcher = base_page.is_present('id', SettingsLocators.AutoconnectSwitch)
            adblocker_switcher = base_page.is_present('id', SettingsLocators.AdBlockerSwitch)
            cookies_switcher = base_page.is_present('id', SettingsLocators.CookiesSwitch)
            trackers_switcher = base_page.is_present('id', SettingsLocators.TrackersSwitch)
            history_switcher = base_page.is_present('id', SettingsLocators.HistorySwitch)
            smart_filters_switcher = base_page.is_present('id', SettingsLocators.SmartFiltersSwitch)
            app_store_button = base_page.is_present('id', SettingsLocators.AppStoreButton)
            play_market_button = base_page.is_present('id', SettingsLocators.PlayMarketButton)
            app_gallery_button = base_page.is_present('id', SettingsLocators.AppGalleryButton)
            amazon_market_button = base_page.is_present('id', SettingsLocators.AmazonMarketButton)
            qr_code = base_page.is_present('class_name', SettingsLocators.QRCode)
            assert isinstance(autoconnect_switcher, WebElement)
            assert isinstance(adblocker_switcher, WebElement)
            assert isinstance(cookies_switcher, WebElement)
            assert isinstance(trackers_switcher, WebElement)
            assert isinstance(history_switcher, WebElement)
            assert isinstance(smart_filters_switcher, WebElement)
            assert isinstance(app_store_button, WebElement)
            assert isinstance(play_market_button, WebElement)
            assert isinstance(app_gallery_button, WebElement)
            assert isinstance(amazon_market_button, WebElement)
            assert isinstance(qr_code, WebElement)
            qase.create_passed_result(case=119, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=119, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Webelements are missing \n {ex}")
