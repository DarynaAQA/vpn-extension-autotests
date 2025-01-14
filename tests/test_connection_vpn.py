from locators.base_locators import BaseLocators
from pages.auth_ext_page import AuthExtPage

import time


class TestConnectionVpn:

    def test_field_behavior_in_connecting(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 62 Test the field behavior in the process of connecting
        STEPS:
        1.Go to main page
        2.Click connect button
        3.Assert behavior field and background
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods = AuthExtPage(setup_driver)
            auth_methods.login_premium_user()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton)
            connect.click()
            text_status = base_page.is_visible('id', BaseLocators.CONNECT_STATUS).text
            background = base_page.is_visible('id', BaseLocators.CONNECT_STATUS)
            background_color = background.value_of_css_property('background-color')
            assert text_status == 'Connection is not secure'

            qase.create_passed_result(case=62, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=62, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Text or background color is not correct \n {ex}")

    def test_behavior_security_field_after_successful_connection(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 63 Test the behavior of the security field after successful connection to the VPN
        STEPS:
        1.Go to main page
        2.Click Connect button
        3.Wait until the 'Connection is secure' div
        4.Assert that the 'Connection is secure' div tex
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods = AuthExtPage(setup_driver)
            auth_methods.login_premium_user()
            base_page.is_clickable('id', BaseLocators.ConnectButton).click()
            text_status = base_page.is_visible('xpath', BaseLocators.ConnectSecure)
            assert text_status.text == 'Connection is secure'
            qase.create_passed_result(case=63, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=63, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Text or background is incorrect\n{ex}')

    def test_behavior_security_after_disconnection(self, setup_driver, qase_run_id, launch_methods):
        """ Behavior of the security field after disconnection from the VPN
            Test the behavior of the security field after successful connection to the VPN
            STEPS:
            1.Go to main page
            2.Click Connect button
            3.Click disconnect button
            3.Wait until the 'Connection is secure' div
            4.Assert that the 'Connection is secure' div tex
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
            connect.click()
            text_status = base_page.is_visible('id', BaseLocators.CONNECT_STATUS).text
            assert text_status == 'Connection is not secure'
            qase.create_passed_result(case=64, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=64, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Text or background is inccorrect\n{ex}')
