from page_objects.page_home import HomePage
from steps.test_login_steps import *


@scenario("../features/homepage_tests.feature",
          "Login with valid user and check menu items")
def test_homepage_feature():
    print("This is the end of homepage feature file.")


@then('I should see the home page is displayed')
def verify_home_page_displayed(browser):
    login_page = LoginPage(browser)
    result = login_page.setting_and_actions()
    assert (result, "Login successful - Home page is displayed")


@when('I click the navmenu')
def open_navmenu(browser):
    home_page = HomePage(browser)
    home_page.open_navmenu()


@when(parsers.cfparse('I expand the parent menu "{menu_name}"'))
def expand_parent_menu(browser, menu_name):
    home_page = HomePage(browser)
    home_page.expand_parent_menu(menu_name)
    print("Expanded the parent menu: " + menu_name)


# @then(parsers.cfparse('I should see the submenu tabs "{submenu_name}"'))
# def display_submenu(browser, submenu_name):
#     home_page = HomePage(browser)
#     submenu_list = [item.strip() for item in submenu_name.split(",")]
#     for submenu in submenu_list:
#         result = home_page.display_submenu(submenu)
#         assert result, "submenu " + submenu + " is not displayed"


@then("I should see the following sub-menu tabs are displayed")
def verify_submenu_tabs_displayed(browser, datatable):
    home_page = HomePage(browser)
    print("Your datatable values are : " + str(datatable))
    table_values = datatable[1:]

    for item in table_values:
        result = home_page.display_submenu(item[0])
        assert result, "submenu " + item[0] + " is not displayed"


@when(parsers.cfparse('I open the "{sub_title}" page under "{main_title}" menu'))
def open_main_menu_tabs(browser, sub_title: str, main_title: str):
    home_page = HomePage(browser)
    home_page.open_menu_tab(sub_title, main_title)


@then(parsers.cfparse('I should see the "{page_name}" page is displayed'))
def verify_page_displayed(browser, page_name: str):
    home_page = HomePage(browser)
    result = home_page.is_page_displayed(page_name)
    assert result, "page " + page_name + " is not found"
