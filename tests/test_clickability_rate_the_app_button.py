from locators.base_locators import BaseLocators
from locators.sidebar_menu_locators import SidebarMenuLocators

import time


class TestClickabilityRateTheAppButton:

    def test_clickability_rate_the_app_button(self, setup_driver, qase_run_id, launch_methods):
        try:
            base_page, privacy_policy, sidebar_menu, qase = launch_methods
            base_page.activate_page()
            privacy_policy.accept_privacy_policy()
            base_page.burger_menu_button_is_present().click()
            rate_app_button = base_page.is_clickable('id', SidebarMenuLocators.RateExtension).click()
            pop_up_rate_app = base_page.is_visible('class_name', BaseLocators.RATE_POP_UP)
            assert pop_up_rate_app.text is not None
            qase.create_passed_result(case=129, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=129, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f"Pop up Do you like our extension? not visible\n {ex}")
