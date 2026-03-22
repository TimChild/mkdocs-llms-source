# Development

## Setup

Clone the repository and install in development mode:

```bash
git clone https://github.com/TimChild/mkdocs-llms-source.git
cd mkdocs-llms-source
uv sync --all-extras
```

## Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=mkdocs_llms_source
```

## Linting

```bash
ruff check src/ tests/
```

Auto-fix:

```bash
ruff check --fix src/ tests/
```

## Building Docs

The project dogfoods its own plugin:

```bash
mkdocs serve    # Local dev server
mkdocs build    # Build static site
```

## Project Structure

- `src/mkdocs_llms_source/plugin.py` — Main plugin implementation
- `tests/` — Test suite with fixtures
- `docs/` — Human-facing documentation (published via MkDocs)
- `agent-docs/` — Agent working notes (not published)

## Architecture

The plugin hooks into MkDocs' build lifecycle:

1. **`on_config`** — Validates that `site_url` is set
2. **`on_files`** — Tracks available source files
3. **`on_nav`** — Walks the nav tree to build llms.txt section structure
4. **`on_page_markdown`** — Captures raw markdown content for each page
5. **`on_post_build`** — Writes `llms.txt`, `llms-full.txt`, and copies `.md` files

Key design decision: **source-first** — we use original markdown source files, not HTML-to-Markdown conversion. This is simpler and preserves author formatting.
