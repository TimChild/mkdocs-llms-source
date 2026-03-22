# TODO

## Phase 1 — MVP (complete)
- [x] Scaffold project structure (pyproject.toml, src/, tests/)
- [x] Implement basic plugin: on_config, on_files, on_nav, on_page_markdown, on_post_build
- [x] Auto-derive sections from MkDocs nav
- [x] Generate /llms.txt with proper spec format
- [x] Generate /llms-full.txt with all content
- [x] Copy per-page .md files to site output
- [x] Write integration tests with a fixture MkDocs site
- [x] Dogfood: use plugin on its own docs site
- [x] Publish to PyPI (v0.1.0)
- [x] CI workflow (lint + test on PR)
- [x] Publish workflow (PyPI on release tag)
- [x] GitHub Pages docs deployment
- [x] v1.0.0 release

## Future — Add when requested
These are potential enhancements to implement if/when users request them:

- [ ] Explicit `sections` config with glob support (override auto-derived nav structure)
- [ ] `optional` section support (per llmstxt.org spec)
- [ ] Optional HTML→Markdown fallback for generated pages (API docs, macros)
- [ ] Preprocessing hooks (custom transforms before output)
- [ ] `base_url` override (for versioned docs / Read the Docs)
- [ ] Per-page description annotations (via frontmatter)
