# Contributing

Thanks for your interest in contributing.

## Before You Start

- Follow the guided checklist in `CONTRIBUTOR_ONBOARDING.md` for a first contribution.
- Use `REPOSITORIES.md` to find the owning repository and its maintenance status.
- Read the repository README.
- Follow any repo-local instructions, including `AGENTS.md` when present.
- Keep changes small and focused.
- Open an issue first for broad behavior changes, new features, or unclear scope.

## Pull Requests

Pull requests should include:

- A clear summary of the change
- The reason for the change
- Verification commands or checks run
- Updated docs or examples when behavior changes

## Development Expectations

- Do not commit secrets, tokens, credentials, or local-only configuration.
- Avoid unrelated refactors.
- Prefer existing project patterns.
- Do not downgrade dependencies unless the maintainer explicitly approves it.
- Use repo-specific verification commands when available.

## Review and Merge

Maintainers review contributions on a best-effort basis. A repository may have its own branch, review, or release process that overrides this default guidance.

Shared guidance is the baseline. Repository-local `AGENTS.md`, `CONTRIBUTING.md`, test commands, and branch rules take precedence for that repository. If two applicable instructions conflict, identify the conflict in the pull request instead of silently choosing one.
