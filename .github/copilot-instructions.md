# Copilot Instructions for mkdocs-llms-source

## Repository Overview

This is a MkDocs plugin that generates /llms.txt files following the
[llmstxt.org](https://llmstxt.org/) specification. It makes MkDocs documentation
sites easily consumable by LLMs and AI coding tools.

## Tech Stack

- Python 3.10+, MkDocs plugin API
- Build: hatchling
- Test: pytest
- Lint: ruff
- Docs: MkDocs Material (dogfooding this plugin)

## How to Build / Test / Run

```bash
# Install in dev mode
uv sync --all-extras

# Run tests
uv run pytest

# Lint
uv run ruff check src/ tests/

# Build docs (dogfooding)
uv run mkdocs build

# Serve docs locally
uv run mkdocs serve
```

## Architecture

- `src/mkdocs_llms_source/plugin.py` — Main plugin class using MkDocs hook API
- Plugin hooks used: on_config, on_files, on_nav, on_page_markdown, on_post_build
- Source-first approach: uses original markdown, no HTML→MD conversion
- Auto-derives llms.txt sections from MkDocs nav config (zero-config)

## Key Design Decisions

- **Source-first**: We use the original .md source, not HTML→Markdown conversion.
  This is simpler and more reliable. Trade-off: dynamically generated content
  (API docs, executed code blocks) won't appear in the markdown output.
- **Nav-derived sections**: By default, the llms.txt H2 sections mirror the
  MkDocs nav structure. No duplicate config needed.
- **Three outputs**: /llms.txt (index), /llms-full.txt (all content), per-page
  .md files (individual pages).

## Documentation Structure

- `docs/` — Human-facing docs published via MkDocs
- `agent-docs/` — Agent working notes (NOT published). Check todo.md at session
  start, update progress.md after milestones.
- `.github/copilot-instructions.md` — This file. Auto-loaded by Copilot.

## Common Pitfalls

- `site_url` must be set in mkdocs.yml for absolute URLs in llms.txt
- `use_directory_urls` affects where .md files get written in site output
- The plugin entry point in pyproject.toml must match the class path exactly
- When editing plugin.py, remember that MkDocs calls hooks in a specific order: on_config → on_files → on_nav → on_page_markdown (per page) → on_post_build

## Releasing to PyPI

Versioning is handled automatically by `hatch-vcs` based on git tags.
The release flow is intentional and manual:

1. Make sure all changes are committed and pushed to `main`
2. Ensure CI is green
3. Tag the release: `git tag vX.Y.Z`
4. Push the tag: `git push origin vX.Y.Z`
5. Create a GitHub release from the tag:
   `gh release create vX.Y.Z --title "vX.Y.Z" --generate-notes`
6. The `publish.yml` workflow will automatically build and publish to PyPI

**When to release**: After merging meaningful changes (new features, bug fixes).
Do NOT forget to tag and release — pushing to `main` alone does NOT publish to PyPI.
The docs site auto-deploys on every push to `main` (no tag needed).
