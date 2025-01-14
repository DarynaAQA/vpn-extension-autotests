from base_classes.driver import Driver
from locators.sidebar_menu_locators import SidebarMenuLocators
from locators.base_locators import BaseLocators


class SidebarMenuExtPage(Driver):



    def settings_button_is_present(self):
        """
            This method check for presence of settings button.
        """
        return self.is_present('id', SidebarMenuLocators.SettingsMenu)

    def faq_button_is_present(self):
        """
            This method check for presence of FAQ button.
        """
        return self.is_present('id', SidebarMenuLocators.FaqMenu)

    def rate_button_is_present(self):
        """
            This method check for presence of Rate button.
        """
        return self.is_present('id',  SidebarMenuLocators.RateExtension)

    def share_button_is_present(self):
        """
            This method check for presence of Share button.
        """
        return self.is_present('id', SidebarMenuLocators.ShareMenu)

    def get_premium_button_is_present(self):
        """
            This method check for presence of Get Premium button.
        """
        return self.is_present('id', SidebarMenuLocators.GetPremiumButton)




