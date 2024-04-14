Feature: OrangeHRMLogo
  Scenario: Logo presence on OrangeHRM Home page
    Given launch the chrome browser
    When open orangeHRM home page
    Then verify that logo present on the home page
    And close browser
