import os
from dotenv import load_dotenv
load_dotenv()

from base_classes.driver import Driver
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.site_locators import IpInfoSiteLocators
from selenium.webdriver.support import expected_conditions as ec
from locators.base_locators import BaseLocators
from locators.account_locators import AccountLocators
import time


class BaseExtPage(Driver):

    def activate_page(self):
        """
            This method activates specific web page.
        """
        original_window = self.driver.current_window_handle
        self.wait.until(ec.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def activate_page_with_extension(self):
        """
            This method activates page with extension.
        """
        extension_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(extension_tab)
        time.sleep(2)
        return self.driver.switch_to.window(extension_tab)

    def activate_redirect_page(self):
        """
            This method activates redirect web page.
        """
        redirect_page = self.driver.window_handles[2]
        self.driver.switch_to.window(redirect_page)

    def open_new_tab_ip_info(self):
        """
            This method open website https://ipinfo.io/ in new tab.
        """
        self.driver.execute_script("window.open('https://ipinfo.io/', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def open_new_tab_free_vpn(self):
        """
            This method open website https://ipinfo.io/ in new tab.
        """
        self.driver.execute_script("window.open('{link_site}', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def burger_menu_button_is_present(self):
        """
            This method will check for presence of button burger menu.
        """
        return self.is_present('class_name', BaseLocators.BurgerMenuButton)

    def login_icon_is_present(self):
        """
            This method will check for presence of login icon.
        """
        return self.is_present('id', AccountLocators.LoginButtonNew)

    def log_out_is_present(self):
        """
            This method will check for presence of logout icon.
        """
        return self.is_present('id', BaseLocators.LogoutButton)

    def logo_vpn_is_present(self):
        """
            This method will check for presence of logo VPN.
        """
        return self.is_present('class_name', BaseLocators.LogoVpn)

    def select_country_button_is_present(self):
        """
            This method will check for presence of select country button.
        """
        return self.is_present('class_name', BaseLocators.SelectServer)

    def current_location_is_present(self):
        """
            This method will check for presence of current location.
        """
        return self.is_present('id', BaseLocators.CurrentLocation)

    def connection_protection_is_present(self):
        """
            This method will check for presence of connection protection.
        """
        return self.is_present('id', BaseLocators.CONNECT_STATUS)

    def vpn_icon_is_present(self):
        """
            This method will check for presence of VPN icon.
        """
        return self.is_present('class_name', BaseLocators.Icon)

    def connect_button_is_present(self):
        """
            This method will check for presence of connect button.
        """
        return self.is_present('class_name', BaseLocators.CONNECT_BUTTON_GREEN)

    def indicator_autoconnect_is_present(self):
        """
            This method will check for presence of indicator autoconnect.
        """
        return self.is_present('id', BaseLocators.IndicatorAutoconnect)

    def indicator_adblocker_is_present(self):
        """
            This method will check for presence of indicator add blocker.
        """
        return self.is_visible('id', BaseLocators.IndicatorAdblocker)

    def indicator_cookies_is_present(self):
        """
            This method will check for presence of indicator cookies.
        """
        return self.is_present('id', BaseLocators.IndicatorCookies)

    def indicator_trackers_is_present(self):
        """
            This method will check for presence of indicator trackers.
        """
        return self.is_present('id', BaseLocators.IndicatorTrackers)

    def indicator_history_is_present(self):
        """
            This method will check for presence of indicator history.
        """
        return self.is_present('id', BaseLocators.IndicatorHistory)

    def indicator_smart_filters_is_present(self):
        """
            This method will check for presence of indicator Smart filters.
        """
        return self.is_present('id', BaseLocators.IndicatorSmartFilters)

    def side_bar_window_is_present(self):
        """
            This method will check for presence of sidebar menu window.
        """
        return self.is_present('class_name', SidebarMenuLocators.SidebarWindow)

    def title_available_servers_is_present(self):
        """
            This method will check for presence of header of available servers.
        """
        return self.is_present('id', BaseLocators.AvailableLocations)

    def panel_indicators_is_present(self):
        """
            This method will check for presence of indicators panel.
        """
        return self.is_present('class_name', BaseLocators.PanelIndicators)

    def get_current_location_ipinfo(self):
        """
            This method will get the current city name of your location from ipinfo.io site.
        """
        current_location = self.get_element_text('xpath', IpInfoSiteLocators.CurrentLocation)
        return current_location

    def faq_is_present(self):
        return self.is_present('id', SidebarMenuLocators.FaqMenu)

    def close_advertising_pop_up(self):

        return self.is_clickable('id', BaseLocators.RedButton).click()
