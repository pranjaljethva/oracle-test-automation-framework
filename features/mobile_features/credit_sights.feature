Feature: As a credit sights mobile application user, I want to test general scenarios
So that I can confirm that the sight is working correctly

  @mobile_ui
  Scenario: Login to credit sights with valid CR user
    Given I login to credit sights application with valid CR user
    Then  I should be able to see the credit sights home page
    And   I should see "All" tab "without" lock icon
    And   I should see "Research" tab "with" lock icon
    And   I should see "Covenants" tab "without" lock icon
    And   I should see "News" tab "with" lock icon
    And   I should see "Top Read" tab "without" lock icon


  @mobile_ui
  Scenario: Checking that tabs on Homepage are having appropriate reports.
    Given I login to credit sights application with valid CR user
    Then  I should be able to see the credit sights home page
#    And   I am on the Home page
    Then  I should see following report_types under "All" tab
            | report_types    |
            | News            |
            | NEWS            |
            | Research        |
            | Covenants       |
    And   I should see only following report_types under "News" tab
            | report_types    |
            | News            |
    And   I should not see following report_types under "News" tab
            | report_types    |
            | Covenants       |
            | Research        |
    And   I should see only following report_types under "Research" tab
            | report_types    |
            | Research        |
    And   I should not see following report_types under "Research" tab
            | report_types    |
            | Covenants       |
            | News            |
    And   I should see only following report_types under "Covenants" tab
            | report_types    |
            | Covenants       |
    And   I should not see following report_types under "Covenants" tab
            | report_types    |
            | News            |
            | Research        |


