"""MkDocs plugin to generate /llms.txt, /llms-full.txt, and per-page .md files."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

from mkdocs.config import config_options
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation, Section
from mkdocs.structure.pages import Page

log = logging.getLogger("mkdocs.plugins.llms_source")


@dataclass
class PageInfo:
    """Metadata about a single documentation page."""

    title: str
    src_path: str
    markdown: str = ""
    description: str = ""

    def md_url(self, base_url: str) -> str:
        """Return the absolute URL to the .md version of this page."""
        return f"{base_url}/{self.src_path}"


@dataclass
class SectionInfo:
    """A section in the llms.txt output (maps to an H2 heading)."""

    title: str
    pages: list[PageInfo] = field(default_factory=list)


class LlmsTxtPlugin(BasePlugin):
    """Generate /llms.txt, /llms-full.txt, and per-page .md files."""

    config_scheme = (
        ("full_output", config_options.Type(bool, default=True)),
        ("markdown_urls", config_options.Type(bool, default=True)),
        ("description", config_options.Type(str, default="")),
    )

    def __init__(self) -> None:
        super().__init__()
        self._pages: dict[str, str] = {}  # src_path -> markdown content
        self._sections: list[SectionInfo] = []
        self._all_page_paths: set[str] = set()

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        """Validate configuration."""
        if not config.get("site_url"):
            log.warning("llms-source: site_url is not set — llms.txt will use relative URLs.")
        return config

    def on_files(self, files: Files, config: MkDocsConfig) -> Files:
        """Track all documentation source files."""
        for f in files.documentation_pages():
            self._all_page_paths.add(f.src_path)
        return files

    def on_nav(self, nav: Navigation, config: MkDocsConfig, files: Files) -> Navigation:
        """Walk the nav tree to auto-derive llms.txt sections."""
        self._sections = []
        self._walk_nav(nav.items)
        return nav

    def on_page_markdown(self, markdown: str, page: Page, config: MkDocsConfig, files: Files) -> str:
        """Capture raw markdown for each page."""
        self._pages[page.file.src_path] = markdown
        return markdown

    def on_post_build(self, config: MkDocsConfig) -> None:
        """Generate llms.txt, llms-full.txt, and copy .md files to site output."""
        site_dir = Path(config["site_dir"])
        site_url = (config.get("site_url") or "").rstrip("/")
        site_name = config.get("site_name", "Documentation")
        site_desc = self.config.get("description") or config.get("site_description", "")

        # Populate page markdown content into section structures
        for section in self._sections:
            for page_info in section.pages:
                page_info.markdown = self._pages.get(page_info.src_path, "")

        # Write llms.txt
        llms_txt = self._build_llms_txt(site_name, site_desc, site_url)
        (site_dir / "llms.txt").write_text(llms_txt, encoding="utf-8")
        log.info("llms-source: Generated llms.txt")

        # Write llms-full.txt
        if self.config.get("full_output", True):
            llms_full = self._build_llms_full(site_name, site_desc)
            (site_dir / "llms-full.txt").write_text(llms_full, encoding="utf-8")
            log.info("llms-source: Generated llms-full.txt")

        # Copy per-page .md files
        if self.config.get("markdown_urls", True):
            self._copy_md_files(config, site_dir)

    # ── Nav walking ──────────────────────────────────────────────

    def _walk_nav(self, items: list, parent_title: str | None = None) -> None:
        """Recursively walk nav items to build sections."""
        for item in items:
            if isinstance(item, Section):
                section = SectionInfo(title=item.title)
                self._sections.append(section)
                self._collect_pages(item.children, section)
            elif isinstance(item, Page):
                # Top-level page (not inside a section)
                title = self._page_title(item)
                if parent_title is None:
                    # Create an implicit section for top-level pages
                    section = SectionInfo(title=title)
                    section.pages.append(
                        PageInfo(title=title, src_path=item.file.src_path)
                    )
                    self._sections.append(section)
            # Skip Link items (external URLs)

    def _collect_pages(self, items: list, section: SectionInfo) -> None:
        """Collect pages from a nav section, including nested subsections."""
        for item in items:
            if isinstance(item, Page):
                title = self._page_title(item)
                section.pages.append(
                    PageInfo(title=title, src_path=item.file.src_path)
                )
            elif isinstance(item, Section):
                # Flatten nested sections into the parent section
                self._collect_pages(item.children, section)
            # Skip Link items (external URLs)

    @staticmethod
    def _page_title(page: Page) -> str:
        """Get the best available title for a page."""
        if page.title:
            return page.title
        # Fallback: derive from filename
        return PurePosixPath(page.file.src_path).stem.replace("-", " ").replace("_", " ").title()

    # ── Output generation ────────────────────────────────────────

    def _build_llms_txt(self, site_name: str, site_desc: str, site_url: str) -> str:
        """Build the llms.txt index content."""
        lines: list[str] = []
        lines.append(f"# {site_name}\n")

        if site_desc:
            lines.append(f"> {site_desc}\n")

        if self.config.get("full_output", True) and site_url:
            lines.append(f"This file is an index of documentation pages. For all content in a single file, see [{site_name} full docs]({site_url}/llms-full.txt).\n")

        for section in self._sections:
            lines.append(f"## {section.title}\n")
            for page in section.pages:
                url = page.md_url(site_url) if site_url else page.src_path
                desc_part = f": {page.description}" if page.description else ""
                lines.append(f"- [{page.title}]({url}){desc_part}")
            lines.append("")

        return "\n".join(lines).rstrip() + "\n"

    def _build_llms_full(self, site_name: str, site_desc: str) -> str:
        """Build the llms-full.txt with all page content concatenated."""
        lines: list[str] = []
        lines.append(f"# {site_name}\n")

        if site_desc:
            lines.append(f"> {site_desc}\n")

        for section in self._sections:
            lines.append(f"## {section.title}\n")
            for page in section.pages:
                if page.markdown:
                    lines.append(f"### {page.title}\n")
                    lines.append(page.markdown.strip())
                    lines.append("")

        return "\n".join(lines).rstrip() + "\n"

    def _copy_md_files(self, config: MkDocsConfig, site_dir: Path) -> None:
        """Copy source .md files into the site output directory."""
        copied = 0

        for src_path, markdown in self._pages.items():
            dest = site_dir / src_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(markdown, encoding="utf-8")
            copied += 1

        log.info("llms-source: Copied %d .md files to site output", copied)
