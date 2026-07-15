from pytest_bdd import scenario
from test_login_steps import *
from test_homepage_steps import *
from test_personal_details import *

@scenario("../features/login.feature",
          "Check login activity by various combination of user name and password")
def test_login_feature():
    print("This is the end of login feature file.")


@scenario("../features/personal_details.feature",
          "Search for a person and update personal details and verify if the details got updated correctly")
def test_personal_details_feature():
    print("this is the end of testing personal detail")


@scenario("../features/homepage_tests.feature",
          "Login with valid user and check menu items")
def test_homepage_feature():
    print("This is the end of homepage feature file.")


