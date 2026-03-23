# Making Documentation LLM-Ready with mkdocs-llms-source

**mkdocs-llms-source** is a MkDocs plugin that makes your documentation instantly consumable by AI coding agents — with zero configuration.

[Star on GitHub :star:](https://github.com/TimChild/mkdocs-llms-source){ .md-button .md-button--primary }
[View on PyPI](https://pypi.org/project/mkdocs-llms-source/){ .md-button }

!!! tip "Try it now"

    Copy this prompt into your AI coding agent — it has everything needed to either add llms-source to an existing MkDocs site, or set up MkDocs from scratch:

    ```
    Add the mkdocs-llms-source plugin to my project using the instructions at https://TimChild.github.io/mkdocs-llms-source/llms.txt
    ```

---

## What It Does

Add two lines to your `mkdocs.yml` and your docs site automatically generates three outputs:

- **`/llms.txt`** — A structured index following the [llmstxt.org](https://llmstxt.org/) spec, with links to individual pages
- **`/llms-full.txt`** — All documentation concatenated into one file, ready for an LLM context window
- **Per-page `.md` files** — Raw markdown accessible at the same URL path as HTML pages

Zero extra configuration. The section structure is auto-derived from your existing MkDocs `nav`.

---

## Why This Matters

### The token efficiency problem

HTML documentation pages carry significant overhead that wastes LLM context window tokens. A typical HTML page is **3–5x larger in tokens** than its markdown source. Navigation bars, JavaScript, CSS, sidebars, footers — none of this helps an LLM understand your API. When working within a context window, every wasted token is documentation your agent *can't* see.

If your docs are built with MkDocs, the source markdown already exists. This plugin just makes it directly available where AI tools expect to find it.

### Growing adoption

The `/llms.txt` standard (proposed by [Jeremy Howard](https://llmstxt.org/) of fast.ai) is gaining serious traction. Major adopters include:

| Category | Examples |
|----------|----------|
| **AI/ML** | Anthropic, Hugging Face, CrewAI, ElevenLabs, Pinecone, Langfuse |
| **Developer Tools** | Cloudflare, Stripe, Cursor, Vercel, Prisma, Expo |
| **Frameworks** | Next.js, Nuxt, Svelte, Angular, Astro, FastHTML |
| **Infrastructure** | NVIDIA, Neon, Turso, Coolify, Modal |

Directories like [llmstxt.site](https://llmstxt.site/) and [directory.llmstxt.cloud](https://directory.llmstxt.cloud/) track thousands of sites that now serve `/llms.txt` files. Other doc frameworks already have plugins (VitePress, Docusaurus, Drupal) — this brings the same capability to MkDocs.

!!! tip "Register your site"

    After deploying, submit your site to the [llmstxt.site directory](https://llmstxt.site/submit) and [directory.llmstxt.cloud](https://tally.so/r/wAydjB) to help grow the ecosystem.

---

## How I Built This (With AI)

I built this plugin in a couple of hours, heavily leveraging Claude Opus 4.6 via the GitHub Copilot extension in VS Code. The full project — plugin code, 12 integration tests, CI/CD pipeline, PyPI publishing, documentation site — was built with me providing direction and the AI doing the implementation heavy lifting.

There's a satisfying recursion to it: **an AI helped me build a tool that helps AIs consume documentation more effectively.**

---

## The Changing Role of Documentation

Documentation has always mattered, but its role is shifting in the age of AI-assisted development:

**For humans** — Docs are becoming less about "how do I call this function?" and more about understanding what agents are building in your codebase. When AI writes significant portions of your code, good documentation becomes your way of staying oriented.

**For AI agents** — Docs are becoming essential infrastructure. Each new agent session starts with zero context. The fastest way to make an agent productive is to point it at well-structured documentation. Better docs = better AI-assisted development.

**For open source** — This creates an interesting new incentive: good documentation doesn't just help human contributors anymore. It directly affects how well AI tools can work with your project. Projects with clean, accessible docs will have a real advantage in an AI-first development world.

---

## Get Started

=== "One command"

    ```bash
    pip install mkdocs-llms-source
    ```

=== "With uv"

    ```bash
    uv add mkdocs-llms-source
    ```

Then add to your `mkdocs.yml`:

```yaml
plugins:
  - llms-source
```

Build your site and you'll find `/llms.txt`, `/llms-full.txt`, and per-page `.md` files in the output.

!!! info "Or let AI do it"

    Just point your AI coding agent at this URL and it will have all the guidance it needs to set this up for you:

    ```
    https://TimChild.github.io/mkdocs-llms-source/llms.txt
    ```

---

*Built with :heart: and AI. [Star the repo](https://github.com/TimChild/mkdocs-llms-source) if you find it useful — it helps others discover the project.*
