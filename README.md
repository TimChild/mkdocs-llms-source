# mkdocs-llms-txt

[![CI](https://github.com/TimChild/mkdocs-llms-txt/actions/workflows/ci.yml/badge.svg)](https://github.com/TimChild/mkdocs-llms-txt/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/mkdocs-llms-txt)](https://pypi.org/project/mkdocs-llms-txt/)
[![Python](https://img.shields.io/pypi/pyversions/mkdocs-llms-txt)](https://pypi.org/project/mkdocs-llms-txt/)

MkDocs plugin to generate [`/llms.txt`](https://llmstxt.org/) files for LLM-friendly documentation.

## What It Does

Generates three outputs from your MkDocs site:

1. **`/llms.txt`** — A curated index following the [llmstxt.org spec](https://llmstxt.org/) with links to per-page markdown files
2. **`/llms-full.txt`** — All documentation concatenated into a single file (for stuffing into LLM context windows)
3. **Per-page `.md` files** — Raw markdown accessible at the same URL path as HTML pages

## Install

```bash
uv add mkdocs-llms-txt
```

## Usage

Add to your `mkdocs.yml`:

```yaml
site_name: My Project
site_url: https://docs.example.com
site_description: Documentation for My Project

plugins:
  - search
  - llmstxt
```

Build your site:

```bash
mkdocs build
```

The plugin auto-derives the llms.txt section structure from your MkDocs `nav` — zero extra configuration needed.

## Configuration

```yaml
plugins:
  - llmstxt:
      full_output: true           # Generate llms-full.txt (default: true)
      markdown_urls: true         # Copy .md source files to output (default: true)
      description: "Override description for llms.txt header"
```

## How It Works

**Source-first approach**: The plugin uses your original markdown source files directly — no HTML-to-Markdown conversion. This is simpler, more reliable, and preserves your intended formatting.

The llms.txt sections are automatically derived from your MkDocs `nav` configuration, so top-level nav items become H2 sections in the output.

## Example Output

Given this nav:

```yaml
nav:
  - Home: index.md
  - Guides:
    - Getting Started: guides/setup.md
```

The generated `/llms.txt`:

```markdown
# My Project

> Documentation for My Project

## Home

- [My Project](https://docs.example.com/index.md)

## Guides

- [Getting Started](https://docs.example.com/guides/setup.md)
```

## License

MIT
