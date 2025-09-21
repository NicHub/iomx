# iomx documentation

Welcome to the iomx documentation.

This documentation uses Sphinx with the MyST parser so content can be written in Markdown and built with Sphinx.

Contents

- installation
- usage

To build locally:

```bash
pip install -r docs/requirements.txt
sphinx-build -b html docs/ docs/_build/html && open docs/_build/html/index.html
```

See `usage.md` for CLI examples and commands.

```{toctree}
:maxdepth: 2
:caption: Contents

installation
usage
```
