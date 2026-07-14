Feature: I want to test home page functionality including menu navigations

  @web_ui
  Scenario: Login with valid user and check menu items
    Given I am on the login page
    When  I perform login with valid user
    Then  I should see the home page is displayed
    When  I click the navmenu
    And   I expand the parent menu "Me"
    Then  I should see the following sub-menu tabs are displayed
      | sub_menu_tab       |
      | My Activity Center |
    When  I expand the parent menu "My Team"
    Then  I should see the following sub-menu tabs are displayed
      | sub_menu_tab           |
      | Talent Review          |
      | Users and Roles        |
      | Workforce Compensation |
    When  I expand the parent menu "Academics"
    Then  I should see the following sub-menu tabs are displayed
      | sub_menu_tab  |
      | Person Search |
      | Curriculum    |
    When  I expand the parent menu "Others"
    Then  I should see the following sub-menu tabs are displayed
      | sub_menu_tab       |
      | Resource Directory |
      | Getting Started         |
      | Marketplace             |
      | Cloud Customer Connect  |





