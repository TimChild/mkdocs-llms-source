# mkdocs-llms-source

MkDocs plugin to generate `/llms.txt` files for LLM-friendly documentation.

## Overview

mkdocs-llms-source generates [llms.txt](https://llmstxt.org/) files from your MkDocs documentation site so that AI tools can efficiently consume your docs without parsing HTML.

The plugin produces three outputs:

1. **`/llms.txt`** — A curated index following the llmstxt.org spec with links to per-page markdown files
2. **`/llms-full.txt`** — All documentation concatenated into a single file
3. **Per-page `.md` files** — Raw markdown at the same URL path as HTML pages

## Quick Start

Install the plugin:

```bash
pip install mkdocs-llms-source
```

Add it to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - llms-source
```

Build your site:

```bash
mkdocs build
```

That's it! Your site will now include `/llms.txt`, `/llms-full.txt`, and per-page `.md` files.

## Configuration

See the [configuration reference](configuration.md) for all options.
