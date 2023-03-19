Feature: interview runs

Scenario: 1 interview runs
  Given I start the interview at "http://localhost/interview?i=docassemble.playground1LocalALKilnInPlayground%3Atest_background.yml"

@2
Scenario: 2 interview runs
  Given I start the interview at "http://localhost/interview?i=docassemble.playground1LocalALKilnInPlayground%3Atest_background.yml"

# Failing with unexpected error
#Scenario: interview runs
#  Given I start the interview at "http://localhost/interview?i=docassemble.playground1LocalALKilnInPlayground%3Abackground.yml"

#Scenario: interview runs
#  Given I start the interview at "background.yml"
#
#@a_tag
#Scenario: interview runs
#  Given I start the interview at "background.yml"