#!/usr/bin/env python3
import os

# Structure du projet iomx
structure = {
    "iomx/": [
        "__init__.py",
        "core.py",
        "cli.py",
        "commands/__init__.py",
        "commands/serial.py",
        "commands/mqtt.py",
        "commands/websocket.py",
        "output/__init__.py",
        "output/json_out.py",
        "output/yaml_out.py",
        "output/text_out.py",
        "tui/__init__.py",
        "tui/app.py",
        "gui/__init__.py",
        "gui/app.py",
    ],
    "tests/": [
        "test_cli.py",
        "test_serial.py",
        "test_mqtt.py",
        "test_websocket.py",
    ],
    "examples/": [
        "mqtt_serial_demo.sh",
        "logging_config.yaml",
    ],
    "docs/": [
        "index.md",
    ],
    "": [  # racine
        "README.md",
        "LICENSE",
        "pyproject.toml",
        "requirements.txt",
        ".gitignore",
    ],
}

# Contenu minimal pour certains fichiers
boilerplate = {
    "__init__.py": "",
    "README.md": "# iomx — I/O Multiplexer\n\n**One data multiplexer to watch them all**\n",
    "LICENSE": "MIT License\n",
    "pyproject.toml": """[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "iomx"
version = "0.1.0"
description = "Lightweight CLI tool to multiplex, inspect, and log multi-protocol IoT streams"
authors = [{name = "Your Name"}]
license = {text = "MIT"}
dependencies = []
requires-python = ">=3.8"

[project.scripts]
iomx = "iomx.cli:main"
""",
    "requirements.txt": "",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n",
    "iomx/cli.py": """import argparse

VERSION = "0.1.0"

def main():
    parser = argparse.ArgumentParser(
        prog="iomx",
        description="iomx — I/O Multiplexer for IoT streams"
    )
    parser.add_argument("--version", action="store_true", help="Show version and exit")

    args = parser.parse_args()

    if args.version:
        print(f"iomx version {VERSION}")
    else:
        print("iomx CLI — no command specified (try --help)")
""",
    "iomx/core.py": '"""Core logic for iomx (I/O Multiplexer)."""\n',
    "iomx/commands/serial.py": '"""Serial protocol implementation for iomx."""\n',
    "iomx/commands/mqtt.py": '"""MQTT protocol implementation for iomx."""\n',
    "iomx/commands/websocket.py": '"""WebSocket protocol implementation for iomx."""\n',
    "iomx/output/json_out.py": '"""JSON output formatter for iomx."""\n',
    "iomx/output/yaml_out.py": '"""YAML output formatter for iomx."""\n',
    "iomx/output/text_out.py": '"""Text output formatter for iomx."""\n',
    "iomx/tui/app.py": '"""Text User Interface for iomx."""\n',
    "iomx/gui/app.py": '"""Graphical User Interface for iomx."""\n',
    "tests/test_cli.py": '"""Tests for CLI module."""\n',
    "tests/test_serial.py": '"""Tests for Serial protocol."""\n',
    "tests/test_mqtt.py": '"""Tests for MQTT protocol."""\n',
    "tests/test_websocket.py": '"""Tests for WebSocket protocol."""\n',
    "examples/mqtt_serial_demo.sh": '#!/bin/bash\necho "MQTT Serial demo"\n',
    "examples/logging_config.yaml": 'version: 1\n',
    "docs/index.md": "# iomx Documentation\n",
}


def create_structure(structure, boilerplate):
    for directory, files in structure.items():
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Created directory: {directory}")
        for f in files:
            path = os.path.join(directory, f)
            if not os.path.exists(path):
                # Créer le dossier parent si nécessaire (pour les sous-dossiers)
                parent_dir = os.path.dirname(path)
                if parent_dir and not os.path.exists(parent_dir):
                    os.makedirs(parent_dir, exist_ok=True)

                content = ""
                # Vérifier d'abord les chemins complets
                if path in boilerplate:
                    content = boilerplate[path]
                # Puis vérifier les noms de fichiers exacts
                elif f in boilerplate:
                    content = boilerplate[f]
                # Enfin vérifier les correspondances par suffixe (comme avant)
                else:
                    for key in boilerplate:
                        if f.endswith(key):
                            content = boilerplate[key]
                            break

                with open(path, "w") as fh:
                    fh.write(content)
                print(f"Created file: {path}")


if __name__ == "__main__":
    create_structure(structure, boilerplate)
    print("DONE")
