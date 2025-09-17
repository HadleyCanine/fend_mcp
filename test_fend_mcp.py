#!/usr/bin/env python
import pytest
from unittest.mock import patch

from fend_mcp import fend

# Run "pytest" from the command line to execute these tests.


def test_fend_basic():
    result = fend("2 + 2")
    assert result == "4"

def test_fend_unit_conversion():
    result = fend("10 meters to feet")
    assert "32.808" in result # Approximate value

def test_fend_error_handling():
    result = fend("5 feet in sec")
    assert "cannot convert from feet to secs" in result

def test_fend_missing_binary():
    with patch("subprocess.run") as mock_run:
        mock_run.side_effect = FileNotFoundError("The system cannot find the file specified")
        result = fend("2 + 2")
        assert "Error running fend" in result

def test_fend_permission_error():
    with patch('fend_mcp.subprocess.run') as mock_run:
        mock_run.side_effect = PermissionError("Permission denied")
        result = fend("2 + 2")
        assert "Error running fend" in result

def test_fend_timeout():
    import subprocess
    with patch('fend_mcp.subprocess.run') as mock_run:
        mock_run.side_effect = subprocess.TimeoutExpired('fend', 5)
        result = fend("2 + 2")
        assert "Error running fend" in result
