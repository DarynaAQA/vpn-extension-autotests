from locators.base_locators import BaseLocators
from pages.auth_ext_page import AuthExtPage
import time


class TestConnectButton:

    def test_process_of_connecting(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 76 Button behavior in the process of connecting to the VPN
        STEPS:
        1.1.Go to main page
        2.Click connect button
        3.Button must be changed color to grey-blue and text to 'Cancel'
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods = AuthExtPage(setup_driver)
            auth_methods.login_premium_user()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton)
            connect.click()
            time.sleep(1)
            button_connecting = base_page.is_visible('class_name', BaseLocators.CONNECTING_BUTTON_BLUE_GRAY)
            button_connecting_text = button_connecting.text
            button_connecting_color = button_connecting.value_of_css_property('background-color')
            assert button_connecting_text == 'Cancel'
            assert button_connecting_color == 'rgba(215, 222, 237, 1)'
            qase.create_passed_result(case=76, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=76, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Text or background color button is not correct \n {ex}")

    def test_displaying_when_vpn_enable(self, setup_driver, qase_run_id, launch_methods):
        """
         ID 78 Displaying the button when the VPN is enabled
         STEPS:
         1.1.Go to main page
         2.Click connect button
         3.Wait until button change color and tex
         4.Button must be changed color to red and text to 'Disconnect'"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods = AuthExtPage(setup_driver)
            auth_methods.login_premium_user()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton).click()
            red_button = base_page.is_clickable('class_name', BaseLocators.BUTTON_CONNECTED_RED)
            assert red_button.value_of_css_property('background-color') == 'rgba(233, 11, 50, 1)'
            assert red_button.text == 'Disconnect'
            qase.create_passed_result(case=78, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=78, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Text or background color button is not correct \n {ex}")

    def test_clickability_cancel_button(self, setup_driver, qase_run_id, launch_methods):
        """ ID 252 Clickability of the "Cancel" button
            STEPS:
            1.Go to main page
            2.Click connect button
            3.Wait until connect button must be a "Cancel" button
            4.Click "Cancel" button
            5.Make sure that Cancel button must be a changed on "Connect to VPN" button"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            time.sleep(2)
            base_page.refresh_page()
            connect = base_page.is_clickable('class_name', BaseLocators.CONNECT_BUTTON_GREEN)
            connect.click()
            base_page.close_advertising_pop_up()
            button_connecting = base_page.is_visible('class_name', BaseLocators.CONNECTING_BUTTON_BLUE_GRAY)
            button_connecting.click()
            connect = base_page.is_clickable('class_name', BaseLocators.CONNECT_BUTTON_GREEN)
            assert connect is not None
            qase.create_passed_result(case=252, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=252, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Cancel button is not clickable \n {ex}")
