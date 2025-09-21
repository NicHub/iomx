# Installation

Install the project and optional dependencies used by some commands.

Recommended (editable install for development):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

Optional dependencies for features:

- `textual` — TUI interface (`iomx tui`)
- `pyserial` — serial port enumeration (`iomx serial ls`)
- `pyperclip` — clipboard copy support (fallbacks exist on most OS)
