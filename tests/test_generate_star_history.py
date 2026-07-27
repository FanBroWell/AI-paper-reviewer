import json
import os
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from unittest.mock import patch

from scripts import generate_star_history as generator


class ModuleAvailabilityTests(unittest.TestCase):
    def test_generator_module_exists(self):
        self.assertTrue(
            Path("scripts/generate_star_history.py").is_file(),
            "star-history generator module is missing",
        )

    def test_generator_exposes_required_api(self):
        for name in (
            "parse_timestamp",
            "build_daily_series",
            "render_svg",
            "fetch_stargazers",
            "main",
        ):
            self.assertTrue(callable(getattr(generator, name, None)), name)


class DailySeriesTests(unittest.TestCase):
    def call_implemented(self, function, *args, **kwargs):
        try:
            return function(*args, **kwargs)
        except NotImplementedError:
            self.fail(f"{function.__name__} is not implemented")

    def test_parse_timestamp_accepts_github_utc_format(self):
        parsed = self.call_implemented(
            generator.parse_timestamp, "2026-07-03T04:05:06Z"
        )
        self.assertEqual(
            parsed,
            datetime(2026, 7, 3, 4, 5, 6, tzinfo=timezone.utc),
        )

    def test_parse_timestamp_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            self.call_implemented(generator.parse_timestamp, "not-a-timestamp")

    def test_build_daily_series_sorts_fills_gaps_and_accumulates(self):
        stars = [
            datetime(2026, 7, 3, 12, tzinfo=timezone.utc),
            datetime(2026, 7, 1, 8, tzinfo=timezone.utc),
            datetime(2026, 7, 3, 18, tzinfo=timezone.utc),
        ]

        series = self.call_implemented(
            generator.build_daily_series,
            stars,
            today=date(2026, 7, 4),
        )

        self.assertEqual(
            series,
            [
                (date(2026, 7, 1), 1),
                (date(2026, 7, 2), 1),
                (date(2026, 7, 3), 3),
                (date(2026, 7, 4), 3),
            ],
        )

    def test_build_daily_series_keeps_empty_history_empty(self):
        self.assertEqual(
            self.call_implemented(
                generator.build_daily_series,
                [],
                today=date(2026, 7, 4),
            ),
            [],
        )


class SvgRenderingTests(unittest.TestCase):
    def call_implemented(self, *args, **kwargs):
        try:
            return generator.render_svg(*args, **kwargs)
        except NotImplementedError:
            self.fail("render_svg is not implemented")

    def test_render_svg_contains_accessible_cumulative_chart(self):
        series = [
            (date(2026, 7, 1), 1),
            (date(2026, 7, 2), 1),
            (date(2026, 7, 3), 3),
        ]

        svg = self.call_implemented(series, "FanBroWell/AI-paper-reviewer")

        self.assertTrue(svg.startswith('<?xml version="1.0"'))
        self.assertIn("<svg", svg)
        self.assertIn("FanBroWell/AI-paper-reviewer Star History", svg)
        self.assertIn('class="star-area"', svg)
        self.assertIn('class="star-line"', svg)
        self.assertIn("2026-07-01", svg)
        self.assertIn("3 Stars", svg)

    def test_render_svg_escapes_repository_name(self):
        svg = self.call_implemented([], "owner/repo<&>")

        self.assertIn("owner/repo&lt;&amp;&gt;", svg)
        self.assertNotIn("owner/repo<&>", svg)
        self.assertIn("No stars yet", svg)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class FetchStargazersTests(unittest.TestCase):
    def test_fetch_stargazers_authenticates_and_paginates(self):
        requests = []
        first_page = [
            {"starred_at": "2026-07-01T00:00:00Z", "user": {"login": f"user-{i}"}}
            for i in range(100)
        ]
        second_page = [
            {"starred_at": "2026-07-02T00:00:00Z", "user": {"login": "last"}}
        ]

        def opener(request, timeout):
            requests.append((request, timeout))
            page = int(parse_qs(urlsplit(request.full_url).query)["page"][0])
            return FakeResponse(first_page if page == 1 else second_page)

        try:
            stars = generator.fetch_stargazers(
                "FanBroWell/AI-paper-reviewer",
                "test-token",
                opener=opener,
            )
        except NotImplementedError:
            self.fail("fetch_stargazers is not implemented")

        self.assertEqual(len(stars), 101)
        self.assertEqual(len(requests), 2)
        self.assertEqual(requests[0][1], 30)
        self.assertEqual(
            requests[0][0].get_header("Authorization"),
            "Bearer test-token",
        )
        self.assertEqual(
            requests[0][0].get_header("Accept"),
            "application/vnd.github.star+json",
        )

    def test_fetch_stargazers_rejects_missing_timestamp(self):
        def opener(request, timeout):
            return FakeResponse([{"user": {"login": "missing-time"}}])

        try:
            with self.assertRaisesRegex(ValueError, "starred_at"):
                generator.fetch_stargazers(
                    "FanBroWell/AI-paper-reviewer",
                    "test-token",
                    opener=opener,
                )
        except NotImplementedError:
            self.fail("fetch_stargazers is not implemented")


class CommandLineTests(unittest.TestCase):
    def test_main_generates_svg_from_repository_environment(self):
        stars = [datetime(2026, 7, 1, tzinfo=timezone.utc)]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "nested" / "star-history.svg"
            with patch.dict(
                os.environ,
                {
                    "GITHUB_REPOSITORY": "FanBroWell/AI-paper-reviewer",
                    "GITHUB_TOKEN": "test-token",
                },
                clear=True,
            ), patch.object(
                generator,
                "fetch_stargazers",
                return_value=stars,
            ) as fetch:
                try:
                    status = generator.main(["--output", str(output)])
                except NotImplementedError:
                    self.fail("main is not implemented")

            self.assertEqual(status, 0)
            self.assertTrue(output.is_file())
            self.assertIn("1 Stars", output.read_text(encoding="utf-8"))
            fetch.assert_called_once_with(
                "FanBroWell/AI-paper-reviewer",
                "test-token",
            )


if __name__ == "__main__":
    unittest.main()
