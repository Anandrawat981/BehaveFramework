Feature: Login in to oranageHRM home page

  Scenario: Login in to oranageHRM home page with valid parameters
    Given Launch the chrome browser
    When user on oranageHRM home page
    And enter username "Admin" and password "admin123"
    And click on Login button
    Then User should able to verify dasboard page with login succesfully

  Scenario Outline: Login in to oranageHRM home page with mutiple parameters
    Given Launch the chrome browser
    When user on oranageHRM home page
    And Enter username "<username>" and password "<password>"
    And click on Login button
    Then User should able to verify dasboard page with login succesfully

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminx   | admin123 |
      | admin    | adminx24 |