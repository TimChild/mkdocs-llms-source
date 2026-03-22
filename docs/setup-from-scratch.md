# Setting Up MkDocs from Scratch

This guide is designed for **AI coding agents** and developers who want to add LLM-friendly documentation to an existing project that has no docs yet. Follow these steps to go from zero to a fully deployed documentation site with `/llms.txt` support.

!!! tip "For AI agents"
    If you're an AI agent helping a user set up docs, this page contains everything you need. Read through and execute the steps in order. Offer to set up the GitHub Pages deployment workflow at the end.

## Prerequisites

- A GitHub repository with Python (or any) project
- Python 3.10+
- `uv` (recommended) or `pip`

## Step 1: Install Dependencies

=== "uv (recommended)"

    ```bash
    uv add --dev mkdocs mkdocs-material mkdocs-llms-source
    ```

=== "pip"

    ```bash
    pip install mkdocs mkdocs-material mkdocs-llms-source
    ```

### Recommended Additional Plugins

These are optional but commonly useful:

| Plugin | What it does | Install |
|--------|-------------|---------|
| `mkdocs-material` | Best MkDocs theme — dark mode, search, code copy | Included above |
| `mkdocs-llms-source` | Generates `/llms.txt` for AI tools | Included above |

## Step 2: Create `mkdocs.yml`

Create this file in your project root:

```yaml
site_name: YOUR_PROJECT_NAME
site_url: https://YOUR_GITHUB_USER.github.io/YOUR_REPO_NAME
site_description: A short description of your project
repo_url: https://github.com/YOUR_GITHUB_USER/YOUR_REPO_NAME
repo_name: YOUR_GITHUB_USER/YOUR_REPO_NAME
edit_uri: edit/main/docs/

theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - content.action.edit
    - content.code.copy
    - navigation.instant
    - navigation.footer
    - navigation.top
    - search.suggest
    - search.highlight
    - toc.follow

plugins:
  - search
  - llms-source

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.tabbed:
      alternate_style: true
  - toc:
      permalink: true
  - attr_list
  - md_in_html

nav:
  - Home: index.md
  # Add more pages here as you create them
```

!!! warning "Replace the placeholders"
    Replace `YOUR_PROJECT_NAME`, `YOUR_GITHUB_USER`, and `YOUR_REPO_NAME` with your actual values. The `site_url` is required for `llms-source` to generate correct absolute URLs.

## Step 3: Create Your Docs

Create the `docs/` directory and an `index.md`:

```bash
mkdir -p docs
```

Create `docs/index.md`:

```markdown
# YOUR_PROJECT_NAME

Short description of what your project does.

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

\```bash
pip install your-project
\```

## Quick Example

\```python
import your_project

# Show a quick usage example
\```
```

Add more pages as needed (e.g., `docs/quickstart.md`, `docs/configuration.md`, `docs/api.md`) and list them in the `nav` section of `mkdocs.yml`.

## Step 4: Build and Preview Locally

```bash
mkdocs serve
```

Open `http://127.0.0.1:8000` to preview your site. Check that:

- The site renders correctly
- `/llms.txt` is accessible (build with `mkdocs build` and check `site/llms.txt`)

## Step 5: Add `site/` to `.gitignore`

```
# MkDocs build output
site/
```

## Step 6: Set Up GitHub Pages Deployment

Create `.github/workflows/docs.yml`:

```yaml
name: Deploy Docs

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: astral-sh/setup-uv@v5
      - run: uv sync --all-extras
      - run: uv run python -m mkdocs build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

!!! note "If not using uv"
    Replace the `uv sync` and `uv run` lines with:
    ```yaml
    - uses: actions/setup-python@v5
      with:
        python-version: '3.12'
    - run: pip install mkdocs mkdocs-material mkdocs-llms-source
    - run: mkdocs build
    ```

### Enable GitHub Pages

1. Go to your repo → **Settings** → **Pages**
2. Under **Build and deployment**, select **GitHub Actions** as the source
3. Push to `main` — the workflow will build and deploy automatically

## Step 7: Verify

After the first deployment, your site will be live at:

```
https://YOUR_GITHUB_USER.github.io/YOUR_REPO_NAME/
```

And the LLM-friendly files will be at:

- `https://YOUR_GITHUB_USER.github.io/YOUR_REPO_NAME/llms.txt`
- `https://YOUR_GITHUB_USER.github.io/YOUR_REPO_NAME/llms-full.txt`

## What You Get

After completing this guide, your project will have:

| Output | Description |
|--------|-------------|
| **Documentation site** | Professional docs with dark mode, search, code copy |
| **`/llms.txt`** | Curated index for AI tools following the [llmstxt.org](https://llmstxt.org/) spec |
| **`/llms-full.txt`** | All docs concatenated — perfect for stuffing into LLM context |
| **Per-page `.md` files** | Raw markdown at the same URL paths as HTML pages |
| **Auto-deploy** | Docs rebuild and deploy on every push to `main` |

## Plugin Configuration

The `llms-source` plugin works with zero configuration for most sites. For customization options, see the [Configuration Reference](configuration.md).
