"""Generate a repository-local GitHub star-history SVG."""

import argparse
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from html import escape
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def parse_timestamp(value):
    if not isinstance(value, str):
        raise ValueError("starred_at must be a string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"invalid starred_at timestamp: {value!r}") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"starred_at timestamp must include a timezone: {value!r}")
    return parsed.astimezone(timezone.utc)


def build_daily_series(stars, today=None):
    if not stars:
        return []

    counts = Counter(star.astimezone(timezone.utc).date() for star in stars)
    current = min(counts)
    end = today or datetime.now(timezone.utc).date()
    if end < current:
        raise ValueError("today cannot be earlier than the first star")

    series = []
    cumulative = 0
    while current <= end:
        cumulative += counts[current]
        series.append((current, cumulative))
        current += timedelta(days=1)
    return series


def render_svg(series, repository, width=800, height=450):
    safe_repository = escape(repository)
    title = f"{safe_repository} Star History"
    header = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
        f'height="{height}" viewBox="0 0 {width} {height}" '
        f'role="img" aria-labelledby="title desc">\n'
        f"  <title id=\"title\">{title}</title>\n"
    )
    style = """  <style>
    .background { fill: #ffffff; }
    .title { fill: #1f2328; font: 700 22px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .summary { fill: #0969da; font: 700 18px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .axis-label { fill: #57606a; font: 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .grid { stroke: #d8dee4; stroke-width: 1; }
    .star-area { fill: url(#area-gradient); }
    .star-line { fill: none; stroke: #0969da; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }
    @media (prefers-color-scheme: dark) {
      .background { fill: #0d1117; }
      .title { fill: #f0f6fc; }
      .axis-label { fill: #8b949e; }
      .grid { stroke: #30363d; }
      .summary { fill: #58a6ff; }
      .star-line { stroke: #58a6ff; }
    }
  </style>
  <defs>
    <linearGradient id="area-gradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#2f81f7" stop-opacity="0.40"/>
      <stop offset="100%" stop-color="#2f81f7" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
"""
    background = (
        f'  <rect class="background" width="{width}" height="{height}" rx="12"/>\n'
        f'  <text class="title" x="32" y="42">{title}</text>\n'
    )

    if not series:
        return (
            header
            + '  <desc id="desc">This repository has no recorded stars yet.</desc>\n'
            + style
            + background
            + '  <text class="summary" x="32" y="76">0 Stars</text>\n'
            + f'  <text class="axis-label" x="{width / 2:.1f}" y="{height / 2:.1f}" '
            + 'text-anchor="middle">No stars yet</text>\n'
            + "</svg>\n"
        )

    left, right, top, bottom = 70, 25, 90, 60
    plot_width = width - left - right
    plot_height = height - top - bottom
    baseline = top + plot_height
    max_count = series[-1][1]
    point_count = len(series)

    def point(index, count):
        x = left if point_count == 1 else left + plot_width * index / (point_count - 1)
        y = baseline - plot_height * count / max_count
        return x, y

    points = [point(index, count) for index, (_, count) in enumerate(series)]
    line_path = " ".join(
        ("M" if index == 0 else "L") + f" {x:.2f} {y:.2f}"
        for index, (x, y) in enumerate(points)
    )
    first_x, _ = points[0]
    last_x, _ = points[-1]
    area_path = (
        f"M {first_x:.2f} {baseline:.2f} "
        + " ".join(f"L {x:.2f} {y:.2f}" for x, y in points)
        + f" L {last_x:.2f} {baseline:.2f} Z"
    )

    grid_parts = []
    tick_values = sorted({round(max_count * index / 4) for index in range(5)})
    for tick in tick_values:
        y = baseline - plot_height * tick / max_count
        grid_parts.append(
            f'  <line class="grid" x1="{left}" y1="{y:.2f}" '
            f'x2="{width - right}" y2="{y:.2f}"/>\n'
        )
        grid_parts.append(
            f'  <text class="axis-label" x="{left - 12}" y="{y + 4:.2f}" '
            f'text-anchor="end">{tick}</text>\n'
        )

    label_indexes = sorted({0, point_count // 2, point_count - 1})
    for index in label_indexes:
        x, _ = points[index]
        anchor = "start" if index == 0 else "end" if index == point_count - 1 else "middle"
        grid_parts.append(
            f'  <text class="axis-label" x="{x:.2f}" y="{baseline + 28}" '
            f'text-anchor="{anchor}">{series[index][0].isoformat()}</text>\n'
        )

    description = (
        f"{repository} has {max_count} stars recorded from "
        f"{series[0][0].isoformat()} through {series[-1][0].isoformat()}."
    )
    return (
        header
        + f'  <desc id="desc">{escape(description)}</desc>\n'
        + style
        + background
        + f'  <text class="summary" x="32" y="76">{max_count} Stars</text>\n'
        + "".join(grid_parts)
        + f'  <path class="star-area" d="{area_path}"/>\n'
        + f'  <path class="star-line" d="{line_path}"/>\n'
        + "</svg>\n"
    )


def fetch_stargazers(repository, token, opener=None):
    if repository.count("/") != 1 or not all(repository.split("/")):
        raise ValueError("repository must use owner/name format")
    if not token:
        raise ValueError("GitHub token is required")

    owner, name = repository.split("/")
    open_url = opener or urlopen
    stars = []
    page = 1

    while True:
        url = (
            f"https://api.github.com/repos/{quote(owner)}/{quote(name)}/stargazers"
            f"?per_page=100&page={page}"
        )
        request = Request(
            url,
            headers={
                "Accept": "application/vnd.github.star+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "AI-paper-reviewer-star-history",
            },
        )
        try:
            with open_url(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"GitHub stargazers API returned HTTP {exc.code}: {detail}"
            ) from exc
        except URLError as exc:
            raise RuntimeError(f"GitHub stargazers API request failed: {exc.reason}") from exc

        if not isinstance(payload, list):
            raise ValueError("GitHub stargazers API returned a non-list response")
        for item in payload:
            if not isinstance(item, dict) or "starred_at" not in item:
                raise ValueError("GitHub stargazer entry is missing starred_at")
            stars.append(parse_timestamp(item["starred_at"]))

        if len(payload) < 100:
            break
        page += 1

    return stars


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate a repository-local GitHub star-history SVG."
    )
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPOSITORY"),
        help="GitHub repository in owner/name format (default: GITHUB_REPOSITORY)",
    )
    parser.add_argument(
        "--output",
        default="assets/star-history.svg",
        help="SVG output path",
    )
    args = parser.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN")
    if not args.repo:
        parser.error("--repo or GITHUB_REPOSITORY is required")
    if not token:
        parser.error("GITHUB_TOKEN is required")

    stars = fetch_stargazers(args.repo, token)
    series = build_daily_series(stars)
    svg = render_svg(series, args.repo)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    temporary.write_text(svg, encoding="utf-8")
    temporary.replace(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
