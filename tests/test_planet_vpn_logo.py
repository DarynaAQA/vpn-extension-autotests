from locators.base_locators import BaseLocators
import time


class TestPlanetVpnLogo:

    def test_display_planet_vpn_logo(self, setup_driver, qase_run_id, launch_methods):
        """
        ID 70 Display planet icon in the extension
        STEPS:
        1.Open extension
        2.Make sure that the VPN planet logo is present on the page
        """
        base_page, privacy_policy, sidebar_menu, qase = launch_methods
        base_page.activate_page()
        privacy_policy.accept_privacy_policy()
        try:
            planet_vpn_logo = base_page.is_present('class_name', BaseLocators.PlanetIcon)
            assert planet_vpn_logo is not None
            qase.create_passed_result(case=70, test_run_id=qase_run_id, time=time.time() - base_page.time)
        except AssertionError as ex:
            qase.create_failed_result(case=70, test_run_id=qase_run_id, time=time.time() - base_page.time,
                                      comment=f'Planet VPN logo not visible\n{ex}')
