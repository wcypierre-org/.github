#!/usr/bin/env python3
"""Generate a human-readable digest of merged organization pull requests."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import urllib.parse
import urllib.request


def fetch_merged_prs(org: str, since: dt.date, until: dt.date, token: str) -> list[dict]:
    query = f"org:{org} is:pr is:merged merged:{since.isoformat()}..{until.isoformat()}"
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": query, "sort": "updated", "order": "asc", "per_page": 100}
    )
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": f"{org}-release-digest",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("total_count", 0) > 100:
        raise RuntimeError("Digest range contains more than 100 pull requests; use a narrower date range")
    return payload.get("items", [])


def repository_name(item: dict) -> str:
    return item["repository_url"].rstrip("/").rsplit("/", 1)[-1]


def is_dependency_update(item: dict) -> bool:
    author = item.get("user", {}).get("login", "").lower()
    title = item.get("title", "").lower()
    return "dependabot" in author or title.startswith(("chore(deps", "build(deps", "deps:"))


def render_digest(org: str, since: dt.date, until: dt.date, items: list[dict]) -> str:
    substantive = [item for item in items if not is_dependency_update(item)]
    dependencies = [item for item in items if is_dependency_update(item)]
    lines = [
        f"# {org} release digest",
        "",
        f"Merged pull requests from {since.isoformat()} through {until.isoformat()} (UTC).",
        "",
    ]
    if not items:
        return "\n".join(lines + ["No pull requests were merged in this period.", ""])
    grouped: dict[str, list[dict]] = {}
    for item in substantive:
        grouped.setdefault(repository_name(item), []).append(item)
    for repo in sorted(grouped, key=str.casefold):
        lines.extend([f"## {repo}", ""])
        for item in grouped[repo]:
            lines.append(f"- [{item['title']}]({item['html_url']}) by @{item['user']['login']}")
        lines.append("")
    if dependencies:
        lines.extend(["## Dependency maintenance", ""])
        for item in sorted(dependencies, key=lambda value: (repository_name(value).casefold(), value["number"])):
            lines.append(f"- `{repository_name(item)}`: [{item['title']}]({item['html_url']})")
        lines.append("")
    return "\n".join(lines)


def parse_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("expected YYYY-MM-DD") from error


def main() -> int:
    today = dt.datetime.now(dt.timezone.utc).date()
    parser = argparse.ArgumentParser()
    parser.add_argument("--org", default="wcypierre-org")
    parser.add_argument("--since", type=parse_date, default=today - dt.timedelta(days=7))
    parser.add_argument("--until", type=parse_date, default=today)
    parser.add_argument("--output", type=pathlib.Path, default=pathlib.Path("release-digest.md"))
    args = parser.parse_args()
    if args.since > args.until:
        parser.error("--since must not be after --until")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        parser.error("GITHUB_TOKEN is required")
    args.output.write_text(render_digest(args.org, args.since, args.until, fetch_merged_prs(args.org, args.since, args.until, token)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
