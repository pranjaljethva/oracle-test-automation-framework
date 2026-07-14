import time

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from support.config_reader import ConfigReader
from locators.mobile_locators import cs_login_locators as csll


class CSLoginPage:
    driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def perform_login(self, username, password):
        self.driver.find_element(AppiumBy.XPATH, csll.EMAIL_INPUT).send_keys(username)
        self.driver.find_element(AppiumBy.XPATH, csll.PASSWORD_INPUT).send_keys(password)

        self.driver.find_element(AppiumBy.XPATH, csll.LOGIN_BUTTON).click()
        time.sleep(10)


