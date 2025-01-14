from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from locators.base_locators import BaseLocators
from dotenv import load_dotenv

import os
import time


class TestLocations:
    IP_INFO = 'https://ipinfo.io/'

    def test_display_users_location_while_connecting(self, setup_driver, qase_run_id, save_ip_to_env, launch_methods):
        """
        ID 66 Test Display the user's location while connecting to the VPN
        STEPS:
        1.Open extension
        2.Click to connect button but not connecting to the VPN
        3.Open new tab with IP_INFO
        4.Assert your location with IP_INFO your location must be not changed
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        load_dotenv()
        my_ip = os.getenv('MY_IP_ADDRESS')
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton)
            connect.click()
            base_page.open_url(TestLocations.IP_INFO)
            base_page.refresh_page()
            time.sleep(1)
            ip_address_ip_info = base_page.is_present('class_name', BaseLocators.IP_INFO_IP)
            ip_address_info_ip = ip_address_ip_info.text
            base_page.open_url(self.IP_INFO)
            assert my_ip == ip_address_info_ip
            qase.create_passed_result(case=66, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=66, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Your location changed\n{ex}')

    def test_display_current_location_connected(self, setup_driver, save_ip_to_env, qase_run_id, launch_methods):
        """
        ID 67 Test Display the user's location while connecting to the VPN
        STEPS:
        1.Open extension
        2.Get user IP and country code
        3.Click to connect button but not connecting to the VPN
        4.Open new tab with IP_INFO
        5.Assert user IP and country code and ip must be changed
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        load_dotenv()
        my_ip = os.getenv('MY_IP_ADDRESS')
        my_country_code = os.getenv('MY_COUNTRY_CODE')
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton)
            connect.click()
            # base_page.close_advertising_pop_up()
            # status_connection = base_page.is_visible('xpath', BaseLocators.ConnectStatus)
            base_page.open_url(TestLocations.IP_INFO)
            base_page.refresh_page()
            time.sleep(1)
            ip_address_ip_info = base_page.is_present('class_name', BaseLocators.IP_INFO_IP)
            ip_address_info_ip = ip_address_ip_info.text
            country_code = base_page.is_present('xpath', BaseLocators.IP_COUNTRY_CODE)
            country_code_ip_info = country_code.text
            assert my_ip != ip_address_info_ip
            assert my_country_code != country_code_ip_info
            qase.create_passed_result(case=67, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=67, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Your location should not change\n{ex}')

    def test_display_location_when_connection_off(self, emulate_network_conditions, qase_run_id, launch_methods):
        """
        ID 68  Display user's current location when internet connection is OFF
        STEPS:
        1.Open browser without internet connection
        2.Open extension
        3.Make sure the user location must be shown when internet connection is OFF
        """
        try:
            driver, go_offline, go_online = emulate_network_conditions
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            go_offline()
            base_page = BaseExtPage(driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            time.sleep(1)
            location_element = base_page.get_element_text('id', BaseLocators.CurrentLocation)
            assert location_element is not None
            qase.create_passed_result(case=68, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=67, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Your location no visible\n{ex}')
