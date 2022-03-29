#!/usr/bin/env python

"""Tests for `usg_audit_failures_inspector` package."""


import unittest
from click.testing import CliRunner

from usg_audit_failures_inspector import usg_audit_failures_inspector
from usg_audit_failures_inspector import cli


class TestUsg_audit_failures_inspector(unittest.TestCase):
    """Tests for `usg_audit_failures_inspector` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'usg_audit_failures_inspector.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
