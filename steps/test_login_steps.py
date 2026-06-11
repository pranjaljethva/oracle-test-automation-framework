import time

from pytest_bdd import scenario, given, when, then, step, parsers
import pytest
from playwright.sync_api import sync_playwright
from support.config_reader import ConfigReader
from locators import login_locators


@scenario("../features/login.feature",
          "Check login activity by various combination of user name and password")
def test_login_feature():
    print("This is the end of login feature file.")


@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page


@step('I am on the login page')
def open_login_page(browser):
    site_url = ConfigReader.get_config_value("base_config.yml", "base_url")
    browser.goto(site_url)
    time.sleep(2)
    print("I want to open a browser and navigate to the login page.")


@when(parsers.cfparse('I enter user name as "{user_name}"'))
def enter_user_name(browser, user_name):
    user = ConfigReader.get_config_value("base_config.yml", user_name)
    browser.locator(login_locators.USERNAME_FIELD).fill(user)
    time.sleep(2)
    print("I am entering the user name as " + user)


@when(parsers.cfparse('I enter password as "{password}"'))
def enter_password(browser, password):
    u_password = ConfigReader.get_config_value("base_config.yml", password)
    browser.locator(login_locators.PASSWORD_FIELD).fill(u_password)
    time.sleep(2)


@when('I press submit button')
def click_submit(browser):
    browser.locator(login_locators.LOGIN_BUTTON).click()
    time.sleep(1)

@then(parsers.cfparse('I should be able to login "{login_success}"'))
def login_check(browser, login_success):
    time.sleep(3)
    if str(login_success).__eq__("successful"):
        result1 = browser.locator(login_locators.SETTING_AND_ACTIONS).is_visible()
        result2 = False
        if result1:
            browser.locator(login_locators.SETTING_AND_ACTIONS).click()
            time.sleep(3)
            result2 = browser.locator(login_locators.SIGNOUT_BUTTON).is_visible()
            if result2:
                browser.locator(login_locators.SIGNOUT_BUTTON).click()
        assert (result1 and result2, "Seems incorrect login as you are not on the home page or logout link is not visible.")

    else:
        error_message = browser.locator(login_locators.INVALID_CREDENTIALS_MESSAGE)

        displayed_message = ''
        expected_msg = "Invalid username or password."
        if error_message.is_visible():
            displayed_message = error_message.text_content()
        print("Expected Message: " + expected_msg)
        print("Displayed Message: " + displayed_message)

        assert (expected_msg.__contains__(displayed_message),
                "Checking if expected invalid login message is displayed or not. " +
                "Expected message: " + expected_msg + ". Displayed message is: " + displayed_message)

#
# @scenario("../features/login.feature",
#           "User should see invalid credentials message with incorrect username or password")
# def test_invalid_login():
#     print("This is the end of login feature file.")


# @then('I should see invalid credentials message')
# def verify_invalid_credentials_message(browser):
#     error_message = browser.locator(login_locators.INVALID_CREDENTIALS_MESSAGE)
#
#     displayed_message = ''
#     expected_msg = "Invalid username or password."
#     if error_message.is_visible():
#         displayed_message = error_message.text_content()
#     print("Expected Message: " + expected_msg)
#     print("Displayed Message: " + displayed_message)
#
#     assert (expected_msg.__contains__(displayed_message),
#             "Checking if expected invalid login message is displayed or not. " +
#             "Expected message: " + expected_msg + ". Displayed message is: " + displayed_message)

#
# @when('I press submit button')
#
# @then('I should be able to login "unsuccessful"')
