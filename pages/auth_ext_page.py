from base_classes.driver import Driver
from locators.account_locators import AccountLocators
from dotenv import load_dotenv
import os


class AuthExtPage(Driver):
    def login_free_user(self):
        """
            This method will auth free user.
        """
        load_dotenv()
        self.is_clickable('id', AccountLocators.LoginButtonNew).click()
        self.is_clickable('xpath', AccountLocators.EmailInput).click()
        self.is_clickable('xpath', AccountLocators.EmailInput).send_keys(os.getenv("FREE_EMAIL"))
        self.is_clickable('xpath', AccountLocators.PasswordInput).click()
        self.is_clickable('xpath', AccountLocators.PasswordInput).send_keys(os.getenv("FREE_PASSWORD"))
        self.is_clickable('xpath', AccountLocators.SendAuthForm).click()

    def login_premium_user(self):
        """
            This method will auth premium user.
        """
        load_dotenv()
        self.is_clickable('id', AccountLocators.LoginButtonNew).click()
        self.is_clickable('xpath', AccountLocators.EmailInput).click()
        self.find_element('xpath', AccountLocators.EmailInput).send_keys(os.getenv("PREMIUM_EMAIL"))
        self.is_clickable('xpath', AccountLocators.PasswordInput).click()
        self.find_element('xpath', AccountLocators.PasswordInput).send_keys(os.getenv("PREMIUM_PASSWORD"))
        self.is_clickable('xpath', AccountLocators.SendAuthForm).click()

    def title_account_is_present(self):
        """
            This method will check for presence of account title.
        """
        return self.is_present('id', AccountLocators.MenuTitle)








