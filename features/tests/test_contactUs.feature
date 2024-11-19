# Created by smypboss at 11/5/24
Feature:"Contact Us" page functionality

  Scenario: User can open the Contact us page

    Given open the main page
    When log in to the page
    And click on setting option
    And click on Contact us option
    Then verify the right page opens
    Then verify there are at least 4 social media icons
    And verify "Connect the company" button is available and clickable