# language: en
@fleet @regression
Feature: Organization release digest

  # Regression source: tests/test_release_digest.py
  # Regression case: test_groups_substantive_changes_and_separates_dependencies
  @id:1
  Scenario: Separate dependency maintenance from product changes
    Given a period contains a jira-tracker feature and an anime-listing Dependabot update
    When the organization release digest is rendered
    Then the feature is grouped under jira-tracker and the update under Dependency maintenance

  # Regression source: tests/test_release_digest.py
  # Regression case: test_empty_period_is_explicit
  @id:2
  Scenario: Explain a period with no merged changes
    Given no pull requests were merged during the reporting period
    When the organization release digest is rendered
    Then the digest explicitly states that no pull requests were merged
