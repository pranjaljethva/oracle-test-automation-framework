Feature: As a Oracle HCM user, I want to test login scenarios
So that I can confirm the login is varified

#Scenario: Check login activity by valid user name and password
#    Given I am on the login page
#    When I enter user name as "valid_user"
#    And  I enter password as "valid_password"
#    And  I press submit button
#    Then I should be able to login successful
#
#Scenario: User should see invalid credentials message with incorrect username or password
#    Given I am on the login page
#    When I enter user name as "invalid_user"
#    And  I enter password as "invalid_password"
#    And  I press submit button
#    Then I should see invalid credentials message

    @web_ui
    Scenario Outline: Check login activity by various combination of user name and password
        Given I am on the login page
        When I enter user name as "<user_name>"
        And  I enter password as "<password>"
        And  I press submit button
        Then I should be able to login "<login_success>"

        Examples:
        | user_name    | password         | login_success  |
        | valid_user   | valid_password   | successful     |
        | invalid_user | invalid_password | unsuccessful   |


