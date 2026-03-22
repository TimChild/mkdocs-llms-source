# Quick Start

## Installation

```bash
uv add mkdocs-llms-source
```

## Basic Usage

Add the plugin to your `mkdocs.yml`:

```yaml
site_name: My Project
site_url: https://docs.example.com
site_description: Documentation for My Project

plugins:
  - search
  - llms-source
```

**Important**: Set `site_url` in your `mkdocs.yml` — the llms.txt spec requires absolute URLs.

Build your site as usual:

```bash
mkdocs build
```

The plugin will generate:

- `site/llms.txt` — Index file following the llmstxt.org spec
- `site/llms-full.txt` — All docs concatenated into one file
- `site/*.md` — Per-page markdown files alongside the HTML

## How It Works

The plugin uses a **source-first** approach:

1. It reads your original markdown source files (no HTML-to-Markdown conversion)
2. It auto-derives the llms.txt section structure from your MkDocs `nav` configuration
3. It generates the output files during the MkDocs build process

This means zero extra configuration is needed for most sites.

## Verify

After building, check that the files were created:

```bash
cat site/llms.txt
```

You should see something like:

```markdown
# My Project

> Documentation for My Project

## Home

- [My Project](https://docs.example.com/index.md)
```
