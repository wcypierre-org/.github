# Xray acceptance definitions

The scenarios in [acceptance/core.feature](acceptance/core.feature) describe organization release
digest.

Each scenario references an existing automated regression case. The regression tests linked below
contain the automated assertions. These feature files do not add Cucumber step bindings or upload
execution results.

Public Community health CI validates scenario identities on pull requests. The private
application-workflows repository publishes these definitions through its Xray public repository sync
workflow every hour and on explicit dispatch. The relay resolves an immutable main-branch commit,
validates it again, and uses the repository-prefixed identities. Jira credentials remain in the
private workflow. Public repositories cannot call the private reusable workflow directly.

Keep the feature path and each @id:number stable. Xray matches the repository-prefixed feature path
and ID. Other sample features and fixtures are outside the publish directory.

Regression assertions: [source][regression-source]. Exact test-case names are recorded in the feature.

- `@id:1`: Separate dependency maintenance from product changes
- `@id:2`: Explain a period with no merged changes

[regression-source]: ../tests/test_release_digest.py
