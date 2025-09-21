import argparse
import os
import sys
from typing import Optional

VERSION = "0.1.1"


def load_config(config_file: str) -> dict:
    if not os.path.exists(config_file):
        raise SystemExit(f"{config_file} not found")
    try:
        import yaml
    except Exception:
        raise SystemExit(
            "PyYAML is required to load configuration (install with 'pip install pyyaml')"
        )
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config or {}


def run_tui() -> None:
    try:
        # Import the TUI runner from package; may raise ImportError if textual not installed
        from iomx.tui.app import run_tui as _run
    except Exception as e:  # ImportError or other
        print(
            "Textual or TUI modules are not available. Install 'textual' and try again."
        )
        print("To install: pip install textual")
        return
    _run()


def main(argv: Optional[list] = None) -> None:
    parser = argparse.ArgumentParser(
        prog="iomx", description="iomx — I/O Multiplexer for IoT streams"
    )
    sub = parser.add_subparsers(dest="command")

    # run command (default behavior)
    run_parser = sub.add_parser("run", help="Run iomx with a configuration file")
    run_parser.add_argument(
        "--config", type=str, default="config.yaml", help="Path to config file"
    )

    # tui command
    sub.add_parser("tui", help="Open the Textual TUI (requires textual)")
    sub.add_parser("lsserial", help="List serial ports (uses pyserial if available)")

    # version
    sub.add_parser("version", help="Show version and exit")

    args = parser.parse_args(argv)

    if args.command in (None, "run"):
        # default to run
        try:
            config = load_config(getattr(args, "config", "config.yaml"))
        except SystemExit as e:
            print(e)
            return
        print("Loaded configuration:", config)
        for stream in config.get("streams", []):
            print(f"Starting {stream.get('protocol')} stream with settings: {stream}")
        print("done")
        return

    if args.command == "tui":
        run_tui()
        return

    if args.command == "lsserial":
        try:
            from iomx.commands.lsserial import list_serial_ports
        except Exception:
            print("lsserial utility requires 'pyserial' for best results. Install with: pip install pyserial")
            # still try to import the module to run fallback
            try:
                from iomx.commands.lsserial import list_serial_ports
            except Exception:
                return
        ports = list_serial_ports()
        if not ports:
            print("No serial ports found")
        else:
            for p in ports:
                print(p)
        return

    if args.command == "version":
        print(f"iomx version {VERSION}")
        return


if __name__ == "__main__":
    main(sys.argv[1:])
