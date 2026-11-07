#!/usr/bin/env python3
"""Validate shared community files without third-party dependencies."""

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
ACTIVE = {
    ".github", "anime-download", "anime-listing", "application-workflows", "assistant-management",
    "carousel-extractor", "deluge-to-jira", "fleet-catalog", "freepbx-call-api", "github-monitor",
    "github-runner-setup", "governance-canary", "governance-workflows", "immich-album-swipe",
    "integration-mock-lab", "jira-assistant-api", "jira-auto-labeler", "jira-dashboard-filter-progress",
    "jira-immich-auto-album", "jira-issue-detail", "jira-reader", "jira-reader-proxy",
    "jira-reading-commenter-ai", "jira-server-api", "jira-server-xray-feature-file-import",
    "jira-tracker", "jira-ui", "omada-at-home-monitor", "publicholiday-tracker", "ramnode-ops",
    "rapidkl-bus-tracker", "receipt-split", "relationship-ql", "runner-control-plane",
    "security-workflows", "sim-monitor-expiry-update", "SimMonitor", "snoozz-export-masker",
    "tab-snooze", "tiktok-auto", "timeline-diary", "ttrss-to-jira", "youtube-to-jira",
}
ARCHIVED = {"autosms-android", "gmail-actioner", "jira-rag", "jira-ui-proxy", "rapidkl-bus-route", "reminder-steps", "runtime-smoke-python", "workflow-release-lab"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    required = [
        "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "CONTRIBUTOR_ONBOARDING.md", "GOVERNANCE.md",
        "PULL_REQUEST_TEMPLATE.md", "REPOSITORIES.md", "SECURITY.md", "SUPPORT.md", "profile/README.md",
        ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/ISSUE_TEMPLATE/feature_request.yml",
        ".github/ISSUE_TEMPLATE/incident_report.yml", ".github/ISSUE_TEMPLATE/config.yml",
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        fail("missing community files: " + ", ".join(missing))

    directory = (ROOT / "REPOSITORIES.md").read_text(encoding="utf-8")
    listed = set(re.findall(r"^\| `([^`]+)` \|", directory, flags=re.MULTILINE))
    if listed != ACTIVE:
        fail(f"active repository directory mismatch; missing={sorted(ACTIVE-listed)}, extra={sorted(listed-ACTIVE)}")
    leaked = sorted(repo for repo in ARCHIVED if f"`{repo}`" in directory)
    if leaked:
        fail("archived repositories present in active directory: " + ", ".join(leaked))

    config = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")
    contact_targets = {"SECURITY.md": "/security/policy", "SUPPORT.md": "SUPPORT.md", "REPOSITORIES.md": "REPOSITORIES.md"}
    for target, link_marker in contact_targets.items():
        if link_marker not in config or not (ROOT / target).is_file():
            fail(f"contact link is missing or has no local target: {target}")

    bug = (ROOT / ".github/ISSUE_TEMPLATE/bug_report.yml").read_text(encoding="utf-8")
    for field in ("deployed-version", "expected", "reproduce", "reproduction-inputs", "frequency", "redaction"):
        if f"id: {field}" not in bug:
            fail(f"bug report missing field: {field}")
    feature = (ROOT / ".github/ISSUE_TEMPLATE/feature_request.yml").read_text(encoding="utf-8")
    for field in ("problem", "proposal", "alternatives", "frequency", "acceptance"):
        if f"id: {field}" not in feature:
            fail(f"feature request missing field: {field}")
    incident = (ROOT / ".github/ISSUE_TEMPLATE/incident_report.yml").read_text(encoding="utf-8")
    for field in ("impact", "affected-repositories", "started-at", "current-state", "timeline", "redaction"):
        if f"id: {field}" not in incident:
            fail(f"incident report missing field: {field}")

    guidance = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    if "take precedence" not in guidance or "conflict" not in guidance:
        fail("contribution guidance must explain repository-local precedence and conflicts")
    profile = (ROOT / "profile/README.md").read_text(encoding="utf-8")
    for target in ("REPOSITORIES.md", "CONTRIBUTOR_ONBOARDING.md"):
        if target not in profile:
            fail(f"organization profile does not link {target}")
    print(f"Validated {len(required)} community files and {len(listed)} active repository entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
