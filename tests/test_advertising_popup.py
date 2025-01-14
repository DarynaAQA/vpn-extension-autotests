from locators.base_locators import BaseLocators
import time


class TestAdvertisingPopup:

    def test_displaying_popup_advertising_free_user(self, setup_driver, qase_run_id, launch_methods):
        """380
        STEPS:
        1. Open extension
        2. Accept privacy policy
        3. Click to connect
        4. Make sure user can be shaw advertising popup
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton)
            connect.click()
            advertising = base_page.is_visible('class_name', BaseLocators.AdvertisingFreeUser)
            button_white = base_page.is_present('id', BaseLocators.WhiteButton)
            red_button = base_page.is_present('id', BaseLocators.RedButton)
            close_button = base_page.is_visible('class_name', BaseLocators.ClosePopUp)
            assert button_white is not None
            assert red_button is not None
            assert close_button is not None
            assert advertising is not None
            qase.create_passed_result(case=380, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=380, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Advertising not visible\n{ex}')


    def test_clickability_back_to_vpn_button(self, setup_driver, launch_methods, qase_run_id):
        """381
       STEPS:
       1. Open extension
       2. Accept privacy policy
       3. Click to connect
       4. Make sure user can be shaw advertising popup
       5. Click to "Back to VPN" button
       6. Make sure popup is closed
       """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.refresh_page()
            connect = base_page.is_clickable('id', BaseLocators.ConnectButton)
            connect.click()
            advertising = base_page.is_visible('class_name', BaseLocators.AdvertisingFreeUser)
            red_button = base_page.is_clickable('id', BaseLocators.RedButton).click()
            assert base_page.invisibility_of_element_located('class_name', BaseLocators.AdvertisingFreeUser)
            qase.create_passed_result(case=381, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=381, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Advertising not visible\n{ex}')
