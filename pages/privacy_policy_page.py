from base_classes.driver import Driver
from locators.privacy_policy_locators import PrivacyPolicyLocators


class PrivacyPolicyPage(Driver):
    def accept_privacy_policy(self):
        """
            Accepts privacy policy.
        """
        self.is_clickable('id', PrivacyPolicyLocators.AcceptButton).click()

