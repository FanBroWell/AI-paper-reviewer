# Self-hosted Star History Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate and display a self-hosted GitHub star-history SVG that updates automatically without a personal access token.

**Architecture:** A dependency-free Python module fetches authenticated stargazer timestamps, builds a cumulative daily series, and renders an SVG. GitHub Actions supplies its repository-scoped token, runs unit tests, generates the asset, and commits only changed output.

**Tech Stack:** Python 3.12 standard library, `unittest`, GitHub Actions, SVG, Markdown.

---

## File map

- Create `scripts/generate_star_history.py`: data fetching, aggregation, SVG rendering, CLI.
- Create `tests/test_generate_star_history.py`: deterministic behavior and API pagination tests.
- Create `.github/workflows/update-star-history.yml`: scheduled/manual test and refresh automation.
- Generate `assets/star-history.svg`: README-visible artifact.
- Modify `README.md`: embed the local chart and keep the live total badge.

### Task 1: Specify star aggregation and SVG behavior

**Files:**
- Create: `tests/test_generate_star_history.py`
- Create: `scripts/generate_star_history.py`

- [ ] **Step 1: Write failing aggregation tests**

Create tests that pass unsorted timezone-aware datetimes into
`build_daily_series()` and assert cumulative points for every date through a
fixed `today`. Add tests asserting empty histories stay empty and invalid
timestamps raise `ValueError`.

- [ ] **Step 2: Run tests and verify RED**

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected: import failure because `scripts.generate_star_history` does not yet
exist.

- [ ] **Step 3: Implement the minimal aggregation API**

Implement:

```python
def parse_timestamp(value: str) -> datetime: ...
def build_daily_series(stars: Sequence[datetime], today: date | None = None) -> list[tuple[date, int]]: ...
```

Sort timestamps, count stars per UTC date, fill missing dates, and return a
cumulative count through `today`.

- [ ] **Step 4: Add and verify SVG tests**

Assert that `render_svg()` returns an XML SVG containing the escaped repository
name, accessible title, axis labels, and a plotted path for non-empty data.
Assert that empty data renders a readable zero-star state.

- [ ] **Step 5: Implement deterministic SVG rendering**

Implement:

```python
def render_svg(series: Sequence[tuple[date, int]], repository: str, width: int = 800, height: int = 450) -> str: ...
```

Use fixed margins, grid lines, date/count labels, an area path, and a line path.
Do not include a generation timestamp so unchanged data produces unchanged SVG.

### Task 2: Fetch authenticated stargazer history

**Files:**
- Modify: `tests/test_generate_star_history.py`
- Modify: `scripts/generate_star_history.py`

- [ ] **Step 1: Write a failing paginated-fetch test**

Use a local fake opener returning two response pages. Assert that
`fetch_stargazers()` sends the timestamp media type and Bearer token, follows
pagination until a short page, and returns parsed datetimes.

- [ ] **Step 2: Run the targeted test and verify RED**

Run:

```bash
python3 -m unittest tests.test_generate_star_history.FetchStargazersTests -v
```

Expected: failure because `fetch_stargazers()` is missing.

- [ ] **Step 3: Implement the minimal authenticated fetcher**

Implement:

```python
def fetch_stargazers(repository: str, token: str, opener=urlopen) -> list[datetime]: ...
```

Request 100 records per page from GitHub's REST API with
`Accept: application/vnd.github.star+json`, validate each `starred_at`, and stop
after the first short page.

- [ ] **Step 4: Add the CLI and verify all tests**

The CLI must require `--repo`/`GITHUB_REPOSITORY` and `GITHUB_TOKEN`, accept
`--output`, create the parent directory, and write UTF-8 SVG only after a
successful fetch and render.

Run:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Expected: all tests pass with no warnings.

### Task 3: Automate generation and publish the chart

**Files:**
- Create: `.github/workflows/update-star-history.yml`
- Modify: `README.md`
- Generate: `assets/star-history.svg`

- [ ] **Step 1: Add the workflow**

Configure `workflow_dispatch`, a daily cron schedule, and a source-file push
trigger. Grant `contents: write`; check out the repository; set up Python 3.12;
run `unittest`; invoke the generator with `GITHUB_TOKEN`; and commit/push only
when `assets/star-history.svg` changes.

- [ ] **Step 2: Push the source files and inspect the real run**

Verify the GitHub workflow reaches a successful terminal state. If it fails,
inspect the failing step and correct only the identified cause.

- [ ] **Step 3: Embed the generated local SVG**

Replace the badge-only section with:

```markdown
[![Star History Chart](assets/star-history.svg)](https://github.com/FanBroWell/AI-paper-reviewer/stargazers)

[![GitHub Stars](https://img.shields.io/github/stars/FanBroWell/AI-paper-reviewer?style=for-the-badge&logo=github&label=Stars)](https://github.com/FanBroWell/AI-paper-reviewer/stargazers)
```

- [ ] **Step 4: Final verification**

Run all unit tests, inspect `git diff --check`, validate the SVG as XML, and
fetch the published README and SVG from the default branch. Confirm the README
references the local asset and the SVG contains the cumulative line/area chart.
