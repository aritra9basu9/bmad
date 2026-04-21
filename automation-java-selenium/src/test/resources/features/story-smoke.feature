@S3_04 @TS-S3-04-001 @TS-S3-04-002
Feature: Basic UI smoke navigation
  As a QA automation engineer
  I want a starter selenium+cucumber test
  So that generated scripts can execute in CI

  Scenario: Open home page and verify title contains Selenium
    Given I open the application home page
    Then the page title should contain "Selenium"
