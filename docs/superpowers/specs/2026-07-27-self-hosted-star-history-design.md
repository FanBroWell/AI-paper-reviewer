# Self-hosted Star History Design

## Goal

Restore a visible GitHub star-history curve in the README without exposing a
personal access token or depending on Star History's anonymous SVG endpoint.

## Root cause

GitHub now restricts timestamped stargazer data to repository administrators
and collaborators. The old README image was rendered by Star History's server,
which is neither an administrator nor a collaborator of this repository, so it
can no longer fetch the data needed to draw the curve.

## Design

The repository will generate and store its own `assets/star-history.svg`.
A small Python standard-library script will request timestamped stargazers with
the repository-scoped `GITHUB_TOKEN`, convert them to a cumulative daily series,
and render a dependency-free SVG. A GitHub Actions workflow will test the
generator, refresh the SVG every day and on manual dispatch, and commit the SVG
only when its contents change.

The README will embed the repository-local SVG and retain the live total-stars
badge. The personal fine-grained token will never appear in repository files,
workflow logs, or README markup.

## Components

- `scripts/generate_star_history.py`: API pagination, daily cumulative series,
  deterministic SVG rendering, and command-line entry point.
- `tests/test_generate_star_history.py`: unit tests for chronological
  aggregation, SVG output, empty history, and paginated API responses.
- `.github/workflows/update-star-history.yml`: test, generate, and commit job
  using only the ephemeral repository `GITHUB_TOKEN`.
- `assets/star-history.svg`: generated chart displayed by GitHub.
- `README.md`: local chart embed plus live stars badge.

## Error handling

The generator exits with a readable error when the token or repository name is
missing, the API returns a non-success status, or a stargazer entry lacks a
timestamp. The workflow does not overwrite the last known-good SVG when data
fetching or tests fail.

## Validation

Unit tests must pass locally. The workflow must complete successfully on
GitHub, commit a non-empty SVG, and the README image URL must return an SVG with
the expected repository name and chart elements.
