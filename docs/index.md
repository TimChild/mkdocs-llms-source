# mkdocs-llms-source

MkDocs plugin to generate `/llms.txt` files for LLM-friendly documentation.

!!! tip "Let AI set it up for you"

    Paste this into your AI coding agent — it will add the plugin to an existing MkDocs site, or set up MkDocs from scratch:

    ```
    Add the mkdocs-llms-source plugin to my project using the instructions at https://TimChild.github.io/mkdocs-llms-source/llms.txt
    ```

## Overview

mkdocs-llms-source generates [llms.txt](https://llmstxt.org/) files from your MkDocs documentation site so that AI tools can efficiently consume your docs without parsing HTML.

The plugin produces three outputs:

1. **`/llms.txt`** — A curated index following the llmstxt.org spec with links to per-page markdown files
2. **`/llms-full.txt`** — All documentation concatenated into a single file
3. **Per-page `.md` files** — Raw markdown at the same URL path as HTML pages

!!! tip "New to MkDocs?"
    If your project doesn't have docs yet, check out the **[Setup from Scratch](setup-from-scratch.md)** guide — it walks you through creating a full MkDocs site with LLM-friendly output and automatic GitHub Pages deployment.

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
