# iomx — I/O Multiplexer

**One data multiplexer to watch them all**

_iomx_ is a lightweight CLI tool, designed to run smoothly locally or over SSH, to multiplex, inspect, and log multi-protocol IoT data streams.

It provides a simple, unified way to monitor data from **serial devices, MQTT brokers, WebSocket (ws) endpoints**, and more.

## ✨ Features

-   Multiplex multiple interfaces with a single tool
-   Supported protocols: Serial, MQTT, WebSocket (ws) — designed to be extensible
-   Output to console or structured logs (JSON, JSONL, YAML, plain text)
-   Lightweight and dependency-minimal (pure Python 3)
-   Ideal for **debugging, testing, and monitoring IoT devices**
-   Includes a **terminal-multiplexer mode**, inspired by tools like `tmux`, to view multiple streams side-by-side

## 🔍 Why iomx?

iomx is a **small, Unix-style CLI utility**: quick to install, easy to script, and ready to use for everyday IoT development and diagnostics.

Unlike heavyweight frameworks (e.g. Node-RED) or single-protocol clients (e.g. `mosquitto_sub`), it is designed to remain minimalistic and start in seconds.

While the main focus of iomx is to act as a **reader/multiplexer**, it also integrates a few lightweight features typically found in a broker — making it handy not only for inspection but also for simple message routing or bridging.

## 🎯 Target audience

Makers and developers working with Arduino, ESP32/8266, or IoT projects in general.
Especially useful when working remotely over SSH.

## ⚠️ Heads up

**iomx is currently in early development (pre-alpha stage)**

## Documentation

Full documentation is available in the `docs/` directory. It uses Sphinx with MyST (Markdown) so you can author pages in Markdown and build HTML with Sphinx or publish on ReadTheDocs.

The CLI uses a resource-first syntax. Examples are documented in `docs/usage.md`.

```
iomx version
```

If you previously used `iomx lsserial`, update your usage to `iomx serial ls`.

## Installation notes

Recommended dependencies (some commands are optional):

```
pip install -r requirements.txt
```

requirements.txt includes: `textual`, `pyserial`, `pyperclip` (clipboard helper).

## Contributing

If you’d like to add more serial commands (connect/monitor) or other resource subcommands (mqtt, ws), the CLI is structured to make that straightforward: add a subparser under the resource, and wire it to `iomx.commands.<resource>`.
