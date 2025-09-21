# iomx — I/O Multiplexer

**One data multiplexer to watch them all**

_iomx_ is a lightweight CLI tool, designed to run smoothly localy or over SSH, to multiplex, inspect, and log multi-protocol IoT data streams.

It provides a simple, unified way to monitor data from **serial devices, MQTT brokers, WebSocket endpoints**, and more.

## ✨ Features

-   Multiplex multiple interfaces with a single tool
-   Supported protocols: Serial, MQTT, WebSocket — designed to be extensible
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

---

Copyright (C) 2025, GPL-3.0-or-later, Nicolas Jeanmonod, ouilogique.com
