from base_classes.qase_integration import QaseMethods
from pages.base_ext_page import BaseExtPage
from pages.privacy_policy_page import PrivacyPolicyPage
from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators
from selenium.webdriver.remote.webelement import WebElement
from locators.share_locators import ShareLocators
import time


class TestShare:
    def test_share_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Check for presence of webelements by visually
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            share_title = base_page.is_present('class_name', ShareLocators.ShareTitle)
            close_button = base_page.is_present('class_name', ShareLocators.CloseButton)
            telegram_icon = base_page.is_present('id', ShareLocators.TelegramIcon)
            telegram_title = base_page.is_present('id', ShareLocators.TelegramTitle)
            whatsapp_icon = base_page.is_present('id', ShareLocators.WhatsAppIcon)
            whatsapp_title = base_page.is_present('id', ShareLocators.WhatsAppTitle)
            facebook_icon = base_page.is_present('id', ShareLocators.FacebookIcon)
            facebook_title = base_page.is_present('id', ShareLocators.FacebookTitle)
            twitter_icon = base_page.is_present('id', ShareLocators.TwitterIcon)
            twitter_title = base_page.is_present('id', ShareLocators.TwitterTitle)
            viber_icon = base_page.is_present('id', ShareLocators.ViberIcon)
            viber_title = base_page.is_present('id', ShareLocators.ViberTitle)
            reddit_icon = base_page.is_present('id', ShareLocators.RedditIcon)
            reddit_title = base_page.is_present('id', ShareLocators.RedditTitle)
            copy_link = base_page.is_present('id', ShareLocators.CopyLink)
            assert isinstance(share_title, WebElement)
            assert isinstance(close_button, WebElement)
            assert isinstance(telegram_icon, WebElement)
            assert isinstance(telegram_title, WebElement)
            assert isinstance(whatsapp_title, WebElement)
            assert isinstance(facebook_title, WebElement)
            assert isinstance(whatsapp_icon, WebElement)
            assert isinstance(whatsapp_title, WebElement)
            assert isinstance(facebook_icon, WebElement)
            assert isinstance(facebook_title, WebElement)
            assert isinstance(twitter_title, WebElement)
            assert isinstance(twitter_icon, WebElement)
            assert isinstance(twitter_title, WebElement)
            assert isinstance(facebook_icon, WebElement)
            assert isinstance(facebook_title, WebElement)
            assert isinstance(twitter_icon, WebElement)
            assert isinstance(twitter_title, WebElement)
            assert isinstance(viber_icon, WebElement)
            assert isinstance(viber_title, WebElement)
            assert isinstance(reddit_icon, WebElement)
            assert isinstance(reddit_title, WebElement)
            assert isinstance(copy_link, WebElement)
            qase.create_passed_result(case=126, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=126, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                      comment=f"Webelements are missing \n {ex}")

    def test_close_button_is_present(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Check for presence of close button
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            close_button = base_page.is_present('class_name', ShareLocators.CloseButton)
            assert isinstance(close_button, WebElement)
            qase.create_passed_result(case=146, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=146, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                  comment=f"Webelements are missing \n {ex}")

    def test_close_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Click on the close button
            6. Check for presence sidebar window
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            base_page.is_clickable('class_name', ShareLocators.CloseButton).click()
            side_bar_window = base_page.is_present('class_name', SidebarMenuLocators.SidebarWindow)
            assert isinstance(side_bar_window, WebElement)
            qase.create_passed_result(case=148, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=148, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                  comment=f"Webelements are missing \n {ex}")

    def test_telegram_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Click on the Telegram button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            base_page.is_clickable('id', ShareLocators.TelegramIcon).click()
            base_page.activate_redirect_page()
            time.sleep(10)
            actual_telegram_url = ("https://t.me/")
            current_telegram_url = base_page.get_current_url()
            assert actual_telegram_url in current_telegram_url
            qase.create_passed_result(case=150, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=150, test_run_id=qase_run_id, time=time.time()-base_page.time,
                        comment=f"The current redirect link on Telegram is different from the actual link:\n {ex}")

    def test_facebook_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Click on the Facebook button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            base_page.is_clickable('id', ShareLocators.FacebookIcon).click()
            base_page.activate_redirect_page()
            time.sleep(10)
            actual_whats_app_url = ("https://www.facebook.com/")
            current_facebook_url = base_page.get_current_url()
            assert actual_whats_app_url in current_facebook_url
            qase.create_passed_result(case=154, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=154, test_run_id=qase_run_id, time=time.time()-base_page.time,
                            comment=f"The current redirect link on Facebook is different from the actual link:\n {ex}")

    def test_twitter_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Click on the Twitter button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            base_page.is_clickable('id', ShareLocators.TwitterIcon).click()
            base_page.activate_redirect_page()
            time.sleep(10)
            actual_twitter_url = ("https://x.com/")
            current_twitter_url = base_page.get_current_url()
            assert actual_twitter_url in current_twitter_url
            qase.create_passed_result(case=156, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=156, test_run_id=qase_run_id, time=time.time()-base_page.time,
                              comment=f"The current redirect link on Twitter is different from the actual link:\n {ex}")

    def test_reddit_button_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Click on the Reddit button
            6. Activate redirect page
            7. Get current url of the webpage
            8. Compare the current url with the required one
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            base_page.is_clickable('id', ShareLocators.RedditIcon).click()
            base_page.activate_redirect_page()
            time.sleep(10)
            actual_reddit_url = ("https://www.reddit.com/")
            current_reddit_url = base_page.get_current_url()
            assert actual_reddit_url in current_reddit_url
            qase.create_passed_result(case=160, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=160, test_run_id=qase_run_id, time=time.time()-base_page.time,
                            comment=f"The current redirect link on Reddit is different from the actual link:\n {ex}")

    def test_copy_link_click(self, setup_driver, qase_run_id, launch_methods):
        """
            STEPS:
            1. Activate page with the extension
            2. Click on the consent button of Privacy Policy
            3. Click on the burger menu button
            4. Click on the share button
            5. Click on the Copy link button
            6. Check for presence of pop up with successful notification
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        try:
            base_page.is_clickable('id', SidebarMenuLocators.ShareMenu).click()
            base_page.is_clickable('id', ShareLocators.CopyLink).click()
            link_copied = base_page.is_present('class_name', ShareLocators.CopySuccess)
            assert isinstance(link_copied, WebElement)
            qase.create_passed_result(case=163, test_run_id=qase_run_id, time=time.time()-base_page.time)
        except Exception as ex:
            qase.create_failed_result(case=163, test_run_id=qase_run_id, time=time.time()-base_page.time,
                                  comment=f"Link could not be copied:\n {ex}")
