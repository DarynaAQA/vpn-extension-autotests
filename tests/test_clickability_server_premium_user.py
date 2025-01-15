from locators.base_locators import BaseLocators
from pages.auth_ext_page import AuthExtPage


import time


class TestClickabilityServerPremiumUser:

    def test_clickability_server_premium_user(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 248 Clickability of the server string for Premium user
        STEPS:
        1.1.Go to main page
        2.Click on the login button
        3.Enter username and password & click on the login button
        4.Click on the server line
        5.Make sure The "Available Locations" page is displayed"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            auth_methods = AuthExtPage(setup_driver)
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            auth_methods.login_premium_user()
            servers = base_page.is_clickable('class_name', BaseLocators.SelectServer).click()
            available_locations = base_page.is_visible('id', BaseLocators.AvailableLocations)
            available_locations_text = available_locations.text
            assert available_locations_text == 'Available locations'
            qase.create_passed_result(case=248, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=248, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Aviable locations is not diplayed \n {ex}")
