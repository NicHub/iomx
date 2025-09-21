# Installation

Install the project and optional dependencies used by some commands.

Recommended (editable install for development):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

## First-time setup (quick start)

This section describes how to run and develop `iomx` for the first time.

Requirements: Python 3.12 or higher.

### 1. Get the repository

```bash
git clone https://github.com/NicHub/iomx.git
cd iomx
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. System dependencies (Raspberry Pi)

On Raspberry Pi (Raspbian / Raspberry Pi OS) some system libraries are required to build extensions and access USB/serial:

```bash
sudo apt update
sudo apt install -y python3-venv build-essential libusb-1.0-0-dev pkg-config
```

If you use USB serial devices, add your user to the `dialout` group to access serial ports:

```bash
sudo usermod -aG dialout $USER
# then reconnect or reboot to apply group membership
```

### 4. Verify the installation

After installation, run a quick smoke test:

```bash
iomx version
iomx serial ls
```

### 5. (Optional) TUI

To use the Textual TUI:

```bash
pip install textual
python -m iomx.cli tui
```

### 6. Local documentation

To build the HTML documentation locally:

```bash
python -m pip install -r docs/requirements.txt
python -m sphinx -b html docs/ docs/_build/html
open docs/_build/html/index.html  # macOS
```
