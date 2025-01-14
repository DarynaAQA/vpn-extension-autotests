from locators.settings_locators import SettingsLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
import time
from zxing import BarCodeReader
from PIL import Image


class TestScanningQRCode:

    def test_scanning_qa_code_android(self, setup_driver, launch_methods, qase_run_id):
        """ID 341
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Get screenshot qr code on the settings page
        6.Decoding screenshot and make sure link is valid
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.refresh_page()
            qr_element = base_page.is_visible('class_name', SettingsLocators.QRCode)
            qr_image_path = 'tests/png/qr_code.png'
            qr_element.screenshot(qr_image_path)
            image = Image.open(qr_image_path)
            reader = BarCodeReader()
            barcode = reader.decode(qr_image_path)
            assert barcode.raw == 'https://me-qr.com/zX3GtJlH'
            qase.create_passed_result(case=341, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=341, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"QR code not scanned\n {ex}")

    def test_scanning_qa_code_ios(self, setup_driver, launch_methods, qase_run_id):
        """ID 342
        1.Go to main page
        2.Click on the burger menu
        4.Click on the "Settings"
        5.Get screenshot qr code on the settings page
        6.Decoding screenshot and make sure link is valid
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            settings = base_page.is_clickable('id', SidebarMenuLocators.SettingsMenu).click()
            base_page.refresh_page()
            qr_element = base_page.is_visible('class_name', SettingsLocators.QRCode)
            qr_image_path = 'tests/png/qr_code.png'
            qr_element.screenshot(qr_image_path)
            image = Image.open(qr_image_path)
            reader = BarCodeReader()
            barcode = reader.decode(qr_image_path)
            assert barcode.raw == 'https://me-qr.com/zX3GtJlH'
            qase.create_passed_result(case=342, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=342, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"QR code not scanned\n {ex}")
