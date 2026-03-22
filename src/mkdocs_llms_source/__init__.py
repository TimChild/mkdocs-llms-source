"""MkDocs plugin to generate /llms.txt for LLM-friendly documentation."""

try:
    from mkdocs_llms_source._version import __version__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0+unknown"
