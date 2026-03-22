"""Tests for the mkdocs-llms-source plugin."""

from __future__ import annotations

from pathlib import Path

from mkdocs.commands.build import build as mkdocs_build
from mkdocs.config.base import load_config


def _build_site(site_path: Path) -> None:
    """Build a MkDocs site using the Python API."""
    config_path = str(site_path / "mkdocs.yml")
    cfg = load_config(config_path)
    # Force site_dir to be under the fixture directory for easy assertions
    cfg["site_dir"] = str(site_path / "site")
    mkdocs_build(cfg)


class TestBasicBuild:
    """Integration tests that build a full MkDocs site."""

    def test_llms_txt_generated(self, basic_site: Path) -> None:
        """llms.txt is created in site output."""
        _build_site(basic_site)
        site = basic_site / "site"
        assert (site / "llms.txt").exists()

    def test_llms_txt_content(self, basic_site: Path) -> None:
        """llms.txt contains correct structure."""
        _build_site(basic_site)
        content = (basic_site / "site" / "llms.txt").read_text()

        # H1 with site name
        assert "# Test Site" in content
        # Blockquote with site description
        assert "> A test documentation site" in content
        # Links to .md files with absolute URLs
        assert "https://test.example.com/index.md" in content
        assert "https://test.example.com/guide.md" in content
        # Section headers
        assert "## Home" in content
        assert "## Guides" in content

    def test_llms_full_txt_generated(self, basic_site: Path) -> None:
        """llms-full.txt is created when full_output is true (default)."""
        _build_site(basic_site)
        site = basic_site / "site"
        assert (site / "llms-full.txt").exists()

    def test_llms_full_txt_content(self, basic_site: Path) -> None:
        """llms-full.txt contains all page content."""
        _build_site(basic_site)
        content = (basic_site / "site" / "llms-full.txt").read_text()

        assert "# Test Site" in content
        assert "This is the home page" in content
        assert "This guide walks you through" in content

    def test_per_page_md_files(self, basic_site: Path) -> None:
        """Per-page .md files are copied to site output."""
        _build_site(basic_site)
        site = basic_site / "site"

        assert (site / "index.md").exists()
        assert (site / "guide.md").exists()

        # Content should match source
        index_content = (site / "index.md").read_text()
        assert "# Welcome" in index_content

    def test_page_titles_from_content(self, basic_site: Path) -> None:
        """Page titles are derived from nav or page content, not filenames."""
        _build_site(basic_site)
        content = (basic_site / "site" / "llms.txt").read_text()

        # Nav title for guide.md is "Setup Guide"
        assert "[Setup Guide]" in content
        # Nav title for index.md is "Home" (from nav key)
        assert "[Home]" in content


class TestConfigOptions:
    """Test plugin configuration variations."""

    def test_full_output_disabled(self, basic_site: Path) -> None:
        """llms-full.txt is NOT created when full_output is false."""
        mkdocs_yml = basic_site / "mkdocs.yml"
        config = mkdocs_yml.read_text().replace(
            "  - llms-source",
            "  - llms-source:\n      full_output: false",
        )
        mkdocs_yml.write_text(config)

        _build_site(basic_site)
        assert not (basic_site / "site" / "llms-full.txt").exists()

    def test_markdown_urls_disabled(self, basic_site: Path) -> None:
        """Per-page .md files are NOT created when markdown_urls is false."""
        mkdocs_yml = basic_site / "mkdocs.yml"
        config = mkdocs_yml.read_text().replace(
            "  - llms-source",
            "  - llms-source:\n      markdown_urls: false",
        )
        mkdocs_yml.write_text(config)

        _build_site(basic_site)
        site = basic_site / "site"
        # llms.txt should still exist
        assert (site / "llms.txt").exists()
        # But per-page .md files should not
        assert not (site / "guide.md").exists()

    def test_custom_description(self, basic_site: Path) -> None:
        """Custom description overrides site_description in llms.txt."""
        mkdocs_yml = basic_site / "mkdocs.yml"
        config = mkdocs_yml.read_text().replace(
            "  - llms-source",
            '  - llms-source:\n      description: "Custom plugin description"',
        )
        mkdocs_yml.write_text(config)

        _build_site(basic_site)
        content = (basic_site / "site" / "llms.txt").read_text()
        assert "> Custom plugin description" in content

    def test_no_site_url(self, basic_site: Path) -> None:
        """Plugin still works without site_url, using relative URLs."""
        mkdocs_yml = basic_site / "mkdocs.yml"
        config = mkdocs_yml.read_text().replace("site_url: https://test.example.com\n", "")
        mkdocs_yml.write_text(config)

        _build_site(basic_site)
        content = (basic_site / "site" / "llms.txt").read_text()
        # Should use relative paths instead of absolute URLs
        assert "index.md" in content
        assert "https://" not in content


class TestEdgeCases:
    """Test edge cases and unusual configurations."""

    def test_site_url_trailing_slash(self, tmp_path: Path) -> None:
        """Trailing slash in site_url doesn't cause double slashes."""
        docs = tmp_path / "docs"
        docs.mkdir()
        (docs / "index.md").write_text("# Index\n\nContent.")
        (tmp_path / "mkdocs.yml").write_text(
            "site_name: Test\n"
            "site_url: https://example.com/\n"
            "plugins:\n  - llms-source\n"
            "nav:\n  - Home: index.md\n"
        )

        _build_site(tmp_path)
        content = (tmp_path / "site" / "llms.txt").read_text()
        assert "https://example.com/index.md" in content
        assert "https://example.com//index.md" not in content

    def test_nested_nav_sections(self, tmp_path: Path) -> None:
        """Nested nav sections are flattened into parent section."""
        docs = tmp_path / "docs"
        docs.mkdir()
        (docs / "index.md").write_text("# Home\n")
        (docs / "a.md").write_text("# Page A\n")
        (docs / "b.md").write_text("# Page B\n")
        (tmp_path / "mkdocs.yml").write_text(
            "site_name: Test\n"
            "site_url: https://example.com\n"
            "plugins:\n  - llms-source\n"
            "nav:\n"
            "  - Home: index.md\n"
            "  - Section:\n"
            "    - Sub:\n"
            "      - A: a.md\n"
            "      - B: b.md\n"
        )

        _build_site(tmp_path)
        content = (tmp_path / "site" / "llms.txt").read_text()
        assert "## Section" in content
        assert "[A]" in content
        assert "[B]" in content
