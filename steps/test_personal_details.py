import time

from pytest_bdd import scenario, given, when, then, parsers
from page_objects.page_home import HomePage
# from steps.test_login_steps import *
from steps.test_homepage_steps import *
from page_objects.page_personal_details import PersonalDetailsPage
import pytest_check as check


@scenario("../features/personal_details.feature",
          "Search for a person and update personal details and verify if the details got updated correctly")
def test_personal_details_feature():
    print("this is the end of testing personal detail")


@when(parsers.cfparse('I search for the user with user number "{employee_id}"'))
def enter_user(browser, employee_id: str):
    personal_details_page = PersonalDetailsPage(browser)
    personal_details_page.search_employee(employee_id)


@then(parsers.cfparse('I should see the personal details for "{employee_name}"'))
def verify_user_page(browser, employee_name: str):
    personal_details_page = PersonalDetailsPage(browser)
    result = personal_details_page.verify_employee_page(employee_name)

    assert result, "employee " + employee_name + " is not displayed."


@when("I modify the following Demographic info")
def modify_fields(browser, datatable):
    personal_details_page = PersonalDetailsPage(browser)
    personal_details_page.click_edit_dmg()

    table_values = datatable[1:]
    for table_row in table_values:
        personal_details_page.enter_fields(table_row[0], table_row[1])


@when("I save the Demographic info section")
def save_modified_section(browser):
    personal_details_page = PersonalDetailsPage(browser)
    personal_details_page.save_modified_section()


@then("I should see the demographic information displayed")
def verify_dmg_info(browser, datatable):
    personal_details_page = PersonalDetailsPage(browser)
    # time.sleep(5)
    table_values = datatable[1:]
    for table_row in table_values:
        actual_text: str = personal_details_page.verify_dmg_info(table_row[0], table_row[1])
        check.is_true(actual_text.__eq__(table_row[1]), "Demographic info for " + table_row[0] + \
                      " does not match with expected value. " + \
                      "Expected value is: " + table_row[1] + ", Actual value found is : " + actual_text)
