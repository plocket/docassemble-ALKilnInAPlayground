Feature: interview runs

@1
Scenario: 1 interview runs
  Given I start the interview at "test_background.yml"
  And I take a screenshot
  And I take a screenshot
  And I take a screenshot

@2
Scenario: 2 interview runs
  Given I start the interview at "test_background.yml"

@3
Scenario: I cause an error
  Given I start the interview at "test_background.yml"
  And I tap to continue

# Failing with unexpected error
#Scenario: interview runs
#  Given I start the interview at "http://localhost/interview?i=docassemble.playground1LocalALKilnInPlayground%3Abackground.yml"
