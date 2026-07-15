import time

from pytest_bdd import when, then, step, parsers
from page_objects.page_login import LoginPage
from support.config_reader import ConfigReader


@step('I am on the login page')
def open_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()


@when(parsers.cfparse('I enter user name as "{user_name}"'))
def enter_user_name(browser, user_name):
    login_page = LoginPage(browser)
    login_page.enter_user_name(user_name)


@when(parsers.cfparse('I enter password as "{password}"'))
def enter_password(browser, password):
    login_page = LoginPage(browser)
    login_page.enter_password(password)


@when('I press submit button')
def click_submit(browser):
    login_page = LoginPage(browser)
    login_page.click_submit()


@then(parsers.cfparse('I should be able to login "{login_success}"'))
def login_check(browser, login_success):
    login_page = LoginPage(browser)
    if str(login_success).__eq__("successful"):
        result1 = login_page.setting_and_actions()
        assert (result1, "Seems incorrect login as you are not on the home page or logout link is not visible.")
        time.sleep(2)
        if result1:
            login_page.sign_out_button()

    else:
        displayed_message = login_page.get_error_message()
        expected_msg = "Invalid username or password."

        print("Expected Message: " + expected_msg)
        print("Displayed Message: " + displayed_message)

        assert (expected_msg.__contains__(displayed_message),
                "Checking if expected invalid login message is displayed or not. " +
                "Expected message: " + expected_msg + ". Displayed message is: " + displayed_message)


@when('I perform login with valid user')
def perform_login_with_valid_user(browser):
    config_reader = ConfigReader()
    login_page = LoginPage(browser)

    login_page.enter_user_name(user_name="valid_user")
    login_page.enter_password(password="valid_password")
    login_page.click_submit()

