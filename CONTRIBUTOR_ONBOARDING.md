# Contributor Onboarding

Use this checklist for a first contribution. Repository-local instructions take precedence where they differ.

## Choose and Understand the Repository

- [ ] Find the owning project and maintenance status in `REPOSITORIES.md`.
- [ ] Read the repository README, `AGENTS.md`, `CONTRIBUTING.md`, and security policy when present.
- [ ] Search existing issues and pull requests for the same problem.
- [ ] Use a bug, feature, or incident form to capture broad or unclear work before implementation.

## Prepare the Change

- [ ] Create a focused branch from the repository's current default branch.
- [ ] Keep credentials in local environment files or secret stores; never commit them.
- [ ] Follow existing code, test, and dependency patterns. Do not downgrade dependencies without explicit approval.
- [ ] Update user documentation and examples when behavior changes.

## Verify and Submit

- [ ] Run the repository's documented formatting, lint, test, build, and runtime checks.
- [ ] Review the diff for generated files, credentials, personal data, and unrelated edits.
- [ ] Explain the problem, resulting behavior, and verification evidence in the pull request.
- [ ] Link the relevant issue and identify any follow-up work or operational limitations.
- [ ] Keep the branch current and address every required status check before merge.

If repository-local and shared instructions conflict, call out the exact conflict in the pull request so a maintainer can resolve it explicitly.
