# Configuration Reference

All configuration options are set under the `llms-source` plugin in `mkdocs.yml`.

## Options

### `full_output`

- **Type**: `bool`
- **Default**: `true`

Generate `/llms-full.txt` containing all documentation content concatenated.

```yaml
plugins:
  - llms-source:
      full_output: false  # Disable llms-full.txt generation
```

### `markdown_urls`

- **Type**: `bool`
- **Default**: `true`

Copy source `.md` files into the site output directory, making them accessible at the same URL path as the HTML pages but with a `.md` extension.

```yaml
plugins:
  - llms-source:
      markdown_urls: false  # Don't copy .md files to output
```

### `description`

- **Type**: `str`
- **Default**: `""` (uses `site_description` from mkdocs.yml)

Override the description shown in the llms.txt blockquote header.

```yaml
plugins:
  - llms-source:
      description: "Custom description for LLM consumers"
```

## Full Example

```yaml
site_name: My Project
site_url: https://docs.example.com
site_description: Documentation for My Project

plugins:
  - search
  - llms-source:
      full_output: true
      markdown_urls: true
      description: "API and usage docs for My Project"

nav:
  - Home: index.md
  - Guides:
    - Getting Started: guides/getting-started.md
    - Advanced Usage: guides/advanced.md
  - API Reference:
    - Overview: api/index.md
    - Endpoints: api/endpoints.md
```

## Requirements

- **`site_url`** must be set in `mkdocs.yml` for absolute URLs in `llms.txt`. Without it, the plugin falls back to relative paths and logs a warning.
- **`nav`** should be defined for best results. The plugin auto-derives llms.txt sections from the nav structure. Without nav, MkDocs auto-generates one from the file structure.

## Register Your Site

After deploying your site with `/llms.txt`, consider submitting it to the public llms.txt directories so others can discover it:

- **[llmstxt.site](https://llmstxt.site/submit)** — Community directory with stats on llms.txt files across the web
- **[directory.llmstxt.cloud](https://tally.so/r/wAydjB)** — Curated directory of sites adopting the llms.txt standard

This helps grow the ecosystem and makes your documentation more discoverable by AI tools that reference these directories.
