# Repository and Maintenance Directory

This directory covers repositories whose GitHub lifecycle is active. “Active” means the repository is not archived; it does not guarantee a deployed service or a particular maintenance cadence.

The default maintainer and escalation contact is [@wcypierre](https://github.com/wcypierre). For application failures, open an issue in the owning repository. For failures spanning repositories, use the cross-repository incident form in this repository. Security reports follow `SECURITY.md`.

## Jira and Content Workflows

| Repository | Purpose | Lifecycle and support |
| --- | --- | --- |
| `jira-assistant-api` | Jira Server wrapper using the assistant PAT. | Active API; issues in repository. |
| `jira-auto-labeler` | Question-driven Jira classification with Ollama. | Active automation; issues in repository. |
| `jira-dashboard-filter-progress` | Searchable Jira filter progress cards. | Active application; issues in repository. |
| `jira-immich-auto-album` | Builds Immich albums from Jira date ranges. | Active automation; issues in repository. |
| `jira-issue-detail` | Focused issue, filter, and done-today views. | Active application; issues in repository. |
| `jira-reader` | Keyboard-oriented reading of Jira-linked content. | Active application; issues in repository. |
| `jira-reader-proxy` | Fetches and rewrites reader content. | Active supporting service; issues in repository. |
| `jira-reading-commenter-ai` | Generates article summaries as Jira comments. | Active automation; issues in repository. |
| `jira-server-api` | Jira operations, statistics, caching, and event processing. | Active API; issues in repository. |
| `jira-server-xray-feature-file-import` | Imports Gherkin feature files into Xray. | Active CLI; issues in repository. |
| `jira-tracker` | Personal habits, work, reminders, and context dashboard. | Active application; issues in repository. |
| `jira-ui` | Sprint board, statistics, issue details, and transcription. | Active application; issues in repository. |
| `ttrss-to-jira` | Converts TT-RSS articles into Jira work. | Active automation; issues in repository. |
| `youtube-to-jira` | Synchronizes YouTube playlists with Jira. | Active automation; issues in repository. |
| `deluge-to-jira` | Connects torrent lifecycle events to Jira. | Active integration; issues in repository. |

## Media and Personal Tools

| Repository | Purpose | Lifecycle and support |
| --- | --- | --- |
| `anime-download` | Discovers releases and submits downloads to Deluge. | Active application; issues in repository. |
| `anime-listing` | Browses and plays a media directory with subtitles. | Active application; issues in repository. |
| `carousel-extractor` | Collects and evaluates Carousell listings. | Active application; issues in repository. |
| `immich-album-swipe` | Reviews album photos with keep/remove actions. | Active application; issues in repository. |
| `receipt-split` | Captures and parses receipts on Android. | Active Android application; issues in repository. |
| `relationship-ql` | Locally analyzes WhatsApp and Instagram exports. | Active analysis application; issues in repository. |
| `timeline-diary` | Private diary with media, search, and backups. | Active application; issues in repository. |
| `tab-snooze` | Reopens scheduled and recurring browser tabs. | Active extension; owns maintained export masking. |
| `snoozz-export-masker` | Historical standalone export masker. | Migration repository; new masker work belongs in `tab-snooze`. |
| `tiktok-auto` | Browser, dashboard, host CRM, agent, and Android automation. | Active automation suite; issues in repository. |

## Monitoring, Calls, and Operations

| Repository | Purpose | Lifecycle and support |
| --- | --- | --- |
| `assistant-management` | Assistant reports, timing, sharing, and accounts. | Active application; issues in repository. |
| `freepbx-call-api` | TTS calls, schedules, queues, and escalation. | Active API; issues in repository. |
| `omada-at-home-monitor` | Derives presence from Omada traffic observations. | Active monitoring application; issues in repository. |
| `publicholiday-tracker` | Tracks Malaysian holidays and sends reminders. | Active scheduled application; issues in repository. |
| `ramnode-ops` | Reconciles a VPS with its operating schedule. | Active infrastructure application; issues in repository. |
| `rapidkl-bus-tracker` | Presents nearby buses, routes, and arrival estimates. | Active application; issues in repository. |
| `sim-monitor-expiry-update` | Updates SIM expiry and serves due reminders. | Active API; issues in repository. |
| `SimMonitor` | Displays SIM inventory and sends expiry notifications. | Active application; issues in repository. |

## Engineering Platform

| Repository | Purpose | Lifecycle and support |
| --- | --- | --- |
| `.github` | Organization profile and shared community health files. | Active organization policy; issues here. |
| `application-workflows` | Reusable application build, smoke, and deployment workflows. | Active workflow library; issues in repository. |
| `fleet-catalog` | Collects repository inventory and policy drift. | Active read-only policy tool; issues in repository. |
| `github-monitor` | Monitors pull requests, workflows, and runners. | Active application; issues in repository. |
| `github-runner-setup` | Builds shared runner images and host tooling. | Active runner infrastructure; issues in repository. |
| `governance-canary` | Rehearses workflow and policy compatibility. | Active fixture repository; issues in repository. |
| `governance-workflows` | Enforces organization policy and fleet adoption. | Active policy library; issues in repository. |
| `integration-mock-lab` | Provides strict integration fixtures and request verification. | Active testing infrastructure; issues in repository. |
| `runner-control-plane` | Declares runner trust and placement policy. | Active policy-only repository; no executable controller. |
| `security-workflows` | Reusable scanning and normalized security evidence. | Active workflow library; issues in repository. |

## Repository Lifecycle Changes

Archived repositories are intentionally absent from the active directory. Before archiving or replacing a project, update this file, the organization profile, and the replacement repository’s migration guidance in the same change.
