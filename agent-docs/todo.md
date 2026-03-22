# TODO

## Phase 1 — MVP
- [x] Scaffold project structure (pyproject.toml, src/, tests/)
- [x] Implement basic plugin: on_config, on_files, on_nav, on_page_markdown, on_post_build
- [x] Auto-derive sections from MkDocs nav
- [x] Generate /llms.txt with proper spec format
- [x] Generate /llms-full.txt with all content
- [x] Copy per-page .md files to site output
- [x] Write integration tests with a fixture MkDocs site
- [ ] Dogfood: use plugin on its own docs site
- [ ] Publish v0.1.0 to PyPI

## Phase 2 — Polish
- [ ] Explicit `sections` config with glob support
- [ ] `optional` section support
- [ ] Handle `use_directory_urls: false`
- [ ] Handle missing site_url gracefully (✓ partial — logs warning, uses relative)
- [ ] CI workflow (lint + test on PR)
- [ ] Publish workflow (PyPI on release tag)

## Phase 3 — Advanced
- [ ] Optional HTML→Markdown fallback for generated pages (API docs, macros)
- [ ] Preprocessing hooks (custom transforms)
- [ ] `base_url` override (for versioned docs / Read the Docs)
- [ ] Per-page description annotations (via frontmatter)
