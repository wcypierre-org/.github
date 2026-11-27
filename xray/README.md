# Xray acceptance definitions

The scenarios in [acceptance/core.feature](acceptance/core.feature) describe organization release digest. Each scenario references an existing automated regression case. The regression tests linked below contain the automated assertions; these feature files do not add Cucumber step bindings or upload execution results.

The pinned shared workflow validates scenario identities on pull requests. After review and merge, changes to the acceptance directory publish test definitions to the `XRAY` project on Jira Server. An explicit workflow dispatch on `main` can resynchronize them. Publishing uses the `XRAY_JIRA_TOKEN` GitHub secret.

Keep the feature path and each `@id:number` stable: Xray matches scenarios using the repository-prefixed feature path and ID. Other sample features and fixtures are outside the publish directory.

| Scenario ID | Regression source | Regression case |
| --- | --- | --- |
| 1 | [tests/test_release_digest.py](../tests/test_release_digest.py) | test_groups_substantive_changes_and_separates_dependencies |
| 2 | [tests/test_release_digest.py](../tests/test_release_digest.py) | test_empty_period_is_explicit |
