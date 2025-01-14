from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.settings_locators import SettingsLocators
from selenium.webdriver.remote.webelement import WebElement
from locators.faq_support_locators import FAQLocators
from locators.account_locators import AccountLocators
import time


class TestFaqSupport:
    def test_faq_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
             STEPS:
             1. Activate page with the extension
             2. Click on the consent button of Privacy Policy
             3. Click on the burger menu button
             4. Click on the FAQ button
             5. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
        base_page.is_clickable('id', SidebarMenuLocators.FaqMenu).click()
        try:
            go_back_button = base_page.is_present('class_name', SettingsLocators.GoBackButton)
            title_faq = base_page.is_present('id', BaseLocators.FaqTitle)
            more_information = base_page.is_visible('id', BaseLocators.MoreInformationText)
            do_you_have_any_questions = base_page.is_visible('id', BaseLocators.DO_YOU_HAVE_ANY_QUESTIONS)
            name_field = base_page.is_visible('id', BaseLocators.INPUT_YOUR_NAME)
            email_field = base_page.is_visible('id', BaseLocators.INPUT_YOUR_EMAIL)
            how_we_can_help_you_field = base_page.is_visible('id', BaseLocators.TEXT_AREA_CAN_WE_HELP_YOU)
            green_button = base_page.is_visible('id', BaseLocators.SUBMIT_BUTTON_GREEN)
            telegram = base_page.is_visible('id', AccountLocators.TelegramButton)
            facebook = base_page.is_visible('id', AccountLocators.FacebookButton)
            assert go_back_button is not None
            assert title_faq is not None
            assert do_you_have_any_questions is not None
            assert name_field is not None
            assert email_field is not None
            assert more_information is not None
            assert how_we_can_help_you_field is not None
            assert green_button is not None
            assert telegram is not None
            assert facebook is not None
            qase.create_passed_result(case=122, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=122, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_go_back_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
             STEPS:
             1. Activate page with the extension
             2. Click on the consent button of Privacy Policy
             3. Click on the burger menu button
             4. Click on the FAQ button
             5. Click on the go back button
             6. Check for presence of current location web element
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.FaqMenu).click()
            base_page.is_clickable('class_name', SettingsLocators.GoBackButton).click()
            current_location = base_page.is_clickable('id', BaseLocators.CurrentLocation)
            assert isinstance(current_location, WebElement)
            qase.create_passed_result(case=235, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=235, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")



    def test_show_all_instructions_button(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the FAQ button
            5. Click on the "Show All instructions" button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.FaqMenu).click()
            base_page.is_clickable('id', SidebarMenuLocators.FaqButtonInstruction).click()
            base_page.activate_redirect_page()
            time.sleep(10)
            actual_url = "https://freevpnplanet.com/contact-us/"
            current_url = base_page.get_current_url()
            assert current_url == actual_url
            qase.create_passed_result(case=238, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=238, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_facebook_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the FAQ button
            5. Click on the Facebook button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.FaqMenu).click()
            base_page.is_clickable('id', AccountLocators.FacebookButton).click()
            actual_url_facebook = "https://www.facebook.com/freevpnplanet"
            base_page.activate_redirect_page()
            time.sleep(10)
            current_url_facebook = base_page.get_current_url()
            assert current_url_facebook == actual_url_facebook
            qase.create_passed_result(case=240, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=240, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_telegram_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the FAQ button
            5. Click on the Telegram button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        try:
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.is_clickable('class_name', BaseLocators.BurgerMenuButton).click()
            base_page.is_clickable('id', SidebarMenuLocators.FaqMenu).click()
            base_page.is_clickable('id', AccountLocators.TelegramButton).click()
            actual_url_telegram = "https://t.me/FreeVPNPlanet"
            base_page.activate_redirect_page()
            time.sleep(10)
            current_url_telegram = base_page.get_current_url()
            assert current_url_telegram == actual_url_telegram
            qase.create_passed_result(case=242, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=242, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")