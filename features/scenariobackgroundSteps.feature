Feature: OrnageHRM login

  Background: common steps to orangeHRM
    Given Launch the chrome browser
    When user on oranageHRM home page
    And enter username "Admin" and password "admin123"
    And click on Login button

  Scenario: Login to oranageHRM application
    Then User should able to verify dasboard page with login succesfully

  Scenario: Login to oranageHRM application
    Then User should able to verify Time at Work on dasboard page

  Scenario: Login to oranageHRM application
    Then User should able to verify My Actions on dasboard page