Feature: As an HR admin user, I want to test the personal details page,
  so that I can verify the personal details are working as expected

  @web_ui
  Scenario: Search for a person and update personal details and verify if the details got updated correctly
    Given I am on the login page
    When  I perform login with valid user
    Then  I should see the home page is displayed
    When  I open the "Personal Details" page under "My Client Groups" menu
    Then  I should see the "Personal Details" page is displayed
    When  I search for the user with user number "47039"
    Then  I should see the personal details for "Joseph Stephens"
    When  I modify the following Demographic info
      | info_title                        | info_value                      |
      | Marital Status                    | Single                        |
      | Place of Birth-Alternate Language | Gujarati                        |
      | Highest Education Level           | Agricultural preparatory degree |
      | Ethnicity                         | South Asian                     |
    And   I save the Demographic info section
    Then  I should see the demographic information displayed
      | info_title                        | info_value                      |
      | Marital Status                    | Single                          |
      | Place of Birth-Alternate Language | Gujarati                        |
      | Highest Education Level           | Agricultural preparatory degree |
      | Ethnicity                         | South Asian                     |
#    And I should see the demographic information displayed before date "01-Jun-2026"
#      | info_title                        | info_value |
#      | Marital Status                    | Married    |
#      | Place of Birth-Alternate Language |            |
#      | Highest Education Level           |            |
#      | Ethnicity                         |            |
#    And I logout from the application

