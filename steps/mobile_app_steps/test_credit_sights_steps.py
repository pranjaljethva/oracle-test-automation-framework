from pytest_bdd import scenario, step, then, parsers
from appium import webdriver
from support.config_reader import ConfigReader
from page_objects.mobile_pages.cs_login_page import CSLoginPage
from page_objects.mobile_pages.cs_home_page import CSHomePage
import pytest_check as check


@scenario("../features/mobile_features/credit_sights.feature",
          "Login to credit sights with valid CR user")
def test_login_to_CSCR_user():
    print("This is the end of login to credit sights with valid CR user.")


@step("I login to credit sights application with valid CR user")
def login_CSCR_user(mbl_application: webdriver):
    config_reader = ConfigReader()
    user_email = config_reader.get_base_config_value("credit_sights > cr_email")
    user_password = config_reader.get_base_config_value("credit_sights > cr_password")
    cs_login_page = CSLoginPage(mbl_application)
    cs_login_page.perform_login(username=user_email, password=user_password)


@then("I should be able to see the credit sights home page")
def verify_homepage(mbl_application: webdriver):
    cs_home_page = CSHomePage(mbl_application)
    is_displayed = cs_home_page.verify_home_page_displayed()
    assert is_displayed, "Credit Sights home page can not be found"


@then(parsers.cfparse('I should see "{tab_name}" tab "{presence}" lock icon'))
def verify_lock_icon(mbl_application: webdriver, tab_name: str, presence):
    cs_home_page = CSHomePage(mbl_application)
    has_lock = cs_home_page.has_lock_icon(tab_name)

    if presence.strip().lower() == "with":
        assert has_lock, f'Expected lock icon on "{tab_name}" tab, but none found'
    else:
        assert not has_lock, f'Expected NO lock icon on "{tab_name}" tab, but one was found'


@scenario("../features/mobile_features/credit_sights.feature",
          "Checking that tabs on Homepage are having appropriate reports.")
def test_reports():
    print("this is the end of reports")


@step("I am on the Home page")
def verify_homepage(mbl_application: webdriver):
    cs_home_page = CSHomePage(mbl_application)
    cs_home_page.open_global_feed()


@step(parsers.cfparse('I should see following report_types under "{tab_name}" tab'))
def verify_report_types_under_tab(mbl_application: webdriver, tab_name: str, datatable):
    cs_home_page = CSHomePage(mbl_application)
    cs_home_page.open_tab(tab_name)

    table_rows = datatable[1:]
    for table_row in table_rows:
        expected_type = table_row[0]
        result = cs_home_page.verify_report_type_found(expected_type)
        check.is_true(result, "No report found with report_type: " + expected_type)


@step(parsers.cfparse('I should see only following report_types under "{tab_name}" tab'))
def verify_one_report(mbl_application: webdriver, tab_name: str, datatable):
    cs_home_page = CSHomePage(mbl_application)
    cs_home_page.open_tab(tab_name)

    table_rows = datatable[1:]
    for table_row in table_rows:
        expected_type = table_row[0]
        result = cs_home_page.verify_one_report_type(expected_type)
        check.is_true(result, "At least one or more element found which has different report_type then: " +
                      expected_type)


@step(parsers.cfparse('I should not see following report_types under "{tab_name}" tab'))
def verify_one_report(mbl_application: webdriver, tab_name: str, datatable):
    cs_home_page = CSHomePage(mbl_application)
    cs_home_page.open_tab(tab_name)

    table_rows = datatable[1:]
    for table_row in table_rows:
        expected_type = table_row[0]
        result = cs_home_page.verify_one_report_type(expected_type)
        check.is_false(result, "At least one or more element found which has different report_type then: " +
                       expected_type)
