Feature: User Signup

  Scenario: Successfully create a new user
    Given I am on the signup page
    When I enter a valid email "newuser@example.com"
    And I enter a valid password "password123"
    And I enter the confirmation password "password123"
    And I enter the verification code "ABC123"
    And I click the "Sign Up" button
    Then I should see "Registration successful!"
    And I should be redirected to the login page
    And the new user should be added to the users list