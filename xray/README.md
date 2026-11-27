# Xray acceptance definitions

The scenarios in [acceptance/core.feature](acceptance/core.feature) describe organization release
digest.

Each scenario references an existing automated regression case. The regression tests linked below
contain the automated assertions. These feature files do not add Cucumber step bindings or upload
execution results.

The pinned shared workflow validates scenario identities on pull requests. Reviewed main-branch
changes publish definitions to the XRAY project on Jira Server. A workflow dispatch on main can
resynchronize them. Publishing uses the XRAY_JIRA_TOKEN GitHub secret.

Keep the feature path and each @id:number stable. Xray matches the repository-prefixed feature path
and ID. Other sample features and fixtures are outside the publish directory.

Regression assertions: [source][regression-source]. Exact test-case names are recorded in the feature.

- `@id:1`: Separate dependency maintenance from product changes
- `@id:2`: Explain a period with no merged changes

[regression-source]: ../tests/test_release_digest.py
