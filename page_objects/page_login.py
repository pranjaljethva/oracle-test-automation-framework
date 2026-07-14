from playwright.sync_api import Page

from locators import login_locators
from support.config_reader import ConfigReader
import time


class LoginPage:
    page: Page

    def __init__(self, page):
        self.page = page

    def open_login_page(self):
        site_url = ConfigReader.get_config_value("base_config.yml", "base_url")
        self.page.goto(site_url)
        time.sleep(1)
        print("I want to open a browser and navigate to the login page.")

    def enter_user_name(self, user_name):
        user = ConfigReader.get_config_value("base_config.yml", user_name)
        self.page.locator(login_locators.USERNAME_FIELD).fill(user)
        # time.sleep(1)
        print("I am entering the user name as " + user)

    def enter_password(self, password):
        u_password = ConfigReader.get_config_value("base_config.yml", password)
        self.page.locator(login_locators.PASSWORD_FIELD).fill(u_password)
        # time.sleep(1)

    def click_submit(self):
        self.page.locator(login_locators.LOGIN_BUTTON).click()
        # time.sleep(1)

    def setting_and_actions(self) -> bool:
        time.sleep(1)
        result = self.page.locator(login_locators.SETTING_AND_ACTIONS).is_visible()
        if result:
            self.page.locator(login_locators.SETTING_AND_ACTIONS).click()
        return result

    def sign_out_button(self):
        result = self.page.locator(login_locators.SIGNOUT_BUTTON).is_visible()
        if result:
            self.page.locator(login_locators.SIGNOUT_BUTTON).click()
            time.sleep(1)
        return result

    def get_error_message(self):
        error_message = self.page.locator(login_locators.INVALID_CREDENTIALS_MESSAGE)
        error_message.wait_for(state="visible", timeout=10000)
        if error_message.is_visible():
            return error_message.text_content()
        else:
            return ''
