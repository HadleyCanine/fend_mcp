#!/usr/bin/env python

# Run "pytest" from the command line to execute these tests.

import pytest
from fend_mcp import fend

def test_fend_basic():
    result = fend("2 + 2")
    assert result == "4"

def test_fend_unit_conversion():
    result = fend("10 meters to feet")
    assert "32.808" in result  # Approximate value

def test_error_handling():
    result = fend("5 feet in sec")
    assert "cannot convert from feet to secs" in result
