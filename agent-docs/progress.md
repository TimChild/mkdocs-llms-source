# Progress

## 2026-03-22 — Initial scaffolding

- Created full project structure with pyproject.toml, src/, tests/, docs/, agent-docs/
- Implemented MVP plugin with all core MkDocs hooks:
  - `on_config` — validates site_url
  - `on_files` — tracks source files
  - `on_nav` — walks nav tree to build section structure
  - `on_page_markdown` — captures raw markdown per page
  - `on_post_build` — writes llms.txt, llms-full.txt, copies .md files
- Wrote integration test suite covering:
  - Basic build verification
  - llms.txt content/structure
  - llms-full.txt generation
  - Per-page .md file copying
  - Config options (full_output, markdown_urls, description)
  - Edge cases (trailing slash, nested nav, no site_url)
- Created docs (index, quickstart, configuration, development)
- Set up CI workflows (lint+test on PR, publish on release)
- Created .github/copilot-instructions.md for agent context
