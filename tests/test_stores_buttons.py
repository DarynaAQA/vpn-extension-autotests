from locators.settings_locators import SettingsLocators
from locators.sidebar_menu_locators import SidebarMenuLocators

import time


class TestStoresButtons:

    def test_clickability_of_app_store_button(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 339
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on app store button
        6.Make sure app store button is clickable"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.refresh_page()
            appstore_button = base_page.is_clickable('id', SettingsLocators.AppStoreButton).click()
            base_page.activate_redirect_page()
            store_url = base_page.get_current_url()
            assert store_url == 'https://apps.apple.com/us/app/free-vpn-proxy-by-planet-vpn/id1410235921'
            qase.create_passed_result(case=339, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=339, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"App store button is not clickable\n {ex}")

    def test_clickability_of_google_market_button(self, setup_driver, launch_methods, qase_run_id):
        """
        ID 340
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on Google play button
        6.Make sure app store button is clickable"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.refresh_page()
            google_play = base_page.is_clickable('id', SettingsLocators.PlayMarketButton).click()
            base_page.activate_redirect_page()
            store_url = base_page.get_current_url()
            assert store_url == 'https://play.google.com/store/apps/details?hl=en&id=com.freevpnplanet'
            qase.create_passed_result(case=340, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=340, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Google play button is not clickable\n {ex}")


    def test_app_gallery_button(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 378
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on AppGallery button
        6.Make sure AppGallery button is clickable"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.refresh_page()
            app_gallery = base_page.is_clickable('id', SettingsLocators.AppGalleryButton).click()
            base_page.activate_redirect_page()
            store_url = base_page.get_current_url()
            assert store_url == 'https://appgallery.huawei.com/app/C108022601'
            qase.create_passed_result(case=378, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=378, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"App Gallery button is not clickable\n {ex}")

    def test_app_amazon_button(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 379
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Click on Amazon button
        6.Make sure Amazon button is clickable"""
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
        base_page.refresh_page()
        amazon = base_page.is_clickable('id', SettingsLocators.AmazonMarketButton).click()
        base_page.activate_redirect_page()
        store_url = base_page.get_current_url()
        try:
            assert store_url == 'https://www.amazon.com/Free-VPN-Proxy-Planet/dp/B0C2QRHLHL/ref=sr_1_1?crid=3HVJ6FNGSUWJL&keywords=Planet+vpn&qid=1691159683&sprefix=planet+vpn%2Caps%2C268&sr=8-1'
            qase.create_passed_result(case=379, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=379, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Amazon button is not clickable\n {ex}")

