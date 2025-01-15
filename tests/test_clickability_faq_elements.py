from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.base_locators import BaseLocators
import time


class TestClickabilityFields:

    span_why_vpn_text = "Using encryption technology as part of the use of a VPN"
    span_its_free_text = "You can use VPN absolutely free"
    span_how_to_use_text = "To use all the features of the application"
    span_where_is_my_password_text = "Account registration takes place automatically"
    span_after_purchase_text = "To access Premium servers, you must be authorized"
    span_how_many_devices_text = "You can connect 10 devices at the same time using one account."
    span_why_does_speed_text = "Speed drops are a common occurrence when using a VPN"
    span_do_you_follow_users_text = "Our company does not store logs of users"

    def test_clickability_why_vpn_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 165 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "Why do I need a VPN?"
        5.Make sure The accordion is opened and the answer to the question is shown
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            burger_menu = base_page.burger_menu_button_is_present()
            burger_menu.click()
            visible_faq_page = base_page.is_visible('id', SidebarMenuLocators.FaqMenu).click()
            why_need_vpn_element = base_page.is_clickable('id', BaseLocators.WHY_DO_I_NEED_A_VPN).click()
            window_why_vpn = base_page.is_visible('id', BaseLocators.SPAN_WHY_DO_I_NEED_A_VPN)
            window_text = window_why_vpn.text
            assert self.span_why_vpn_text in window_text
            qase.create_passed_result(case=165, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=165, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_clickability_is_it_free_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 167 Clickability of the “Is it free?” field.
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "Is it free?"
        5.Make sure The accordion is opened and the answer to the question is shown
        """
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            burger_menu = base_page.burger_menu_button_is_present()
            burger_menu.click()
            visible_faq_page = base_page.is_visible('id', SidebarMenuLocators.FaqMenu)
            visible_faq_page.click()
            its_free_element = base_page.is_clickable('id', BaseLocators.ITS_FREE)
            its_free_element.click()
            window_its_free = base_page.is_visible('id', BaseLocators.SPAN_ITS_FREE)
            window_its_free_text = window_its_free.text
            assert self.span_its_free_text in window_its_free_text
            qase.create_passed_result(case=167, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=167, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_clickability_how_to_use_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 165 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "How to use the application"
        5.Make sure The accordion is opened and the answer to the question is shown"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            burger_menu = base_page.burger_menu_button_is_present()
            burger_menu.click()
            visible_faq_page = base_page.is_visible('id', SidebarMenuLocators.FaqMenu).click()
            how_to_use_element = base_page.is_clickable('id', BaseLocators.HOW_TO_USE).click()
            window_how_to_use = base_page.is_visible('id', BaseLocators.SPAN_HOW_TO_USE)
            window_how_to_use_text = window_how_to_use.text
            assert self.span_how_to_use_text in window_how_to_use_text
            qase.create_passed_result(case=169, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=169, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_were_is_my_password_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 165 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "Where is my password"
        5.Make sure The accordion is opened and the answer to the question is shown"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            visible_faq_page = base_page.is_visible('id', SidebarMenuLocators.FaqMenu).click()
            where_is_my_password_element = base_page.is_clickable('id', BaseLocators.WHERE_IS_MY_PASSWORD).click()
            window_where_is_my_password = base_page.is_visible('id', BaseLocators.SPAN_WHERE_IS_MY_PASSWORD)
            window_text = window_where_is_my_password.text
            assert self.span_where_is_my_password_text in window_text
            qase.create_passed_result(case=171, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=171, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_after_the_purchase_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 165 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "After the purchase"
        5.Make sure The accordion is opened and the answer to the question is shown"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            burger_menu = base_page.burger_menu_button_is_present()
            burger_menu.click()
            visible_faq_page = base_page.is_visible('id', SidebarMenuLocators.FaqMenu)
            visible_faq_page.click()
            after_the_purchase_element = base_page.is_clickable('id', BaseLocators.AFTER_THE_PURCHASE)
            after_the_purchase_element.click()
            window_purchase = base_page.is_visible('id', BaseLocators.SPAN_AFTER_THE_PURCHASE)
            window_purchase_text = window_purchase.text
            assert self.span_after_purchase_text in window_purchase_text
            qase.create_passed_result(case=173, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=173, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_how_many_devicy_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 175 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "How many devices can I connect?"
        5.Make sure The accordion is opened and the answer to the question is shown"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            burger_menu = base_page.burger_menu_button_is_present()
            burger_menu.click()
            visible_faq_page = base_page.is_visible('id', SidebarMenuLocators.FaqMenu)
            visible_faq_page.click()
            how_many_devices_element = base_page.is_clickable('id', BaseLocators.HOW_MANY_DEVICES)
            how_many_devices_element.click()
            window_how_many_devices = base_page.is_visible('id', BaseLocators.SPAN_HOW_MANY_DEVICES)
            window_how_many_devices_text = window_how_many_devices.text
            assert self.span_how_many_devices_text in window_how_many_devices_text
            qase.create_passed_result(case=175, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=175, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_why_does_the_speed_drop_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 230 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "Why does the speed drop when connecting?"
        5.Make sure The accordion is opened and the answer to the question is shown"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            base_page.is_visible('id', SidebarMenuLocators.FaqMenu).click()
            why_does_speed_element = base_page.is_clickable('id', BaseLocators.WHY_DOES_SPEED).click()
            window_why_does_speed = base_page.is_visible('id', BaseLocators.SPAN_WHY_DOES_SPEED)
            window_why_does_speed_text = window_why_does_speed.text
            assert self.span_why_does_speed_text in window_why_does_speed_text
            qase.create_passed_result(case=230, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=230, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_clickability_do_you_follow_users_field(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 253 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Click "Do you follow users?"
        5.Make sure The accordion is opened and the answer to the question is shown"""
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            base_page.is_visible('id', SidebarMenuLocators.FaqMenu).click()
            do_you_follow_users_element = base_page.is_visible('id', BaseLocators.DO_YOU_FOLLOW_USERS).click()
            window_follow_users = base_page.is_visible('id', BaseLocators.SPAN_DO_YOU_FOLLOW_USERS)
            window_follow_users_text = window_follow_users.text
            assert self.span_do_you_follow_users_text in window_follow_users_text
            qase.create_passed_result(case=253, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=253, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'The accordion is not opened and the answer to the question is not shown\n{ex}')

    def test_displayed_have_any_questions_window(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 243 Clickability of the field “Why do I need a VPN?”
        STEPS:
        1.Open extension
        2.Click burger menu button
        3.Click FAQ menu button
        4.Find Do you have any questions element
        5.Find Your name input
        6.Fiend Your email input
        7.Find Textarea input
        8.Find Green submit button
        8.Make sure all elements visible
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        base_page.burger_menu_button_is_present().click()
        base_page.is_visible('id', SidebarMenuLocators.FaqMenu).click()
        try:
            do_you_have_any_questions = base_page.is_visible('id', BaseLocators.DO_YOU_HAVE_ANY_QUESTIONS)
            name_field = base_page.is_visible('id', BaseLocators.INPUT_YOUR_NAME)
            assert name_field is not None
            email_field = base_page.is_visible('id', BaseLocators.INPUT_YOUR_EMAIL)
            assert email_field is not None
            how_we_can_help_you_field = base_page.is_visible('id', BaseLocators.TEXT_AREA_CAN_WE_HELP_YOU)
            assert how_we_can_help_you_field is not None
            green_button = base_page.is_visible('id', BaseLocators.SUBMIT_BUTTON_GREEN)
            green_button_text = green_button.text
            assert green_button_text == 'Send'
            qase.create_passed_result(case=243, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=243, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'FAQ form is not visible\n{ex}')
