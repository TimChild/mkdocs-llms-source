# Configuration Reference

All configuration options are set under the `llmstxt` plugin in `mkdocs.yml`.

## Options

### `full_output`

- **Type**: `bool`
- **Default**: `true`

Generate `/llms-full.txt` containing all documentation content concatenated.

```yaml
plugins:
  - llmstxt:
      full_output: false  # Disable llms-full.txt generation
```

### `markdown_urls`

- **Type**: `bool`
- **Default**: `true`

Copy source `.md` files into the site output directory, making them accessible at the same URL path as the HTML pages but with a `.md` extension.

```yaml
plugins:
  - llmstxt:
      markdown_urls: false  # Don't copy .md files to output
```

### `description`

- **Type**: `str`
- **Default**: `""` (uses `site_description` from mkdocs.yml)

Override the description shown in the llms.txt blockquote header.

```yaml
plugins:
  - llmstxt:
      description: "Custom description for LLM consumers"
```

## Full Example

```yaml
site_name: My Project
site_url: https://docs.example.com
site_description: Documentation for My Project

plugins:
  - search
  - llmstxt:
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
