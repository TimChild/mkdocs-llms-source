"""Shared test fixtures."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures"


@pytest.fixture()
def basic_site(tmp_path: Path) -> Path:
    """Copy the basic-site fixture to a temp directory and return its path."""
    src = FIXTURES_DIR / "basic-site"
    dest = tmp_path / "basic-site"
    shutil.copytree(src, dest)
    return dest
