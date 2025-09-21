import argparse
import os
import sys
import subprocess
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

    # resource-oriented commands (recommended): e.g. `iomx serial ls`
    serial_parser = sub.add_parser("serial", help="Serial device commands")
    serial_sub = serial_parser.add_subparsers(dest="serial_command")
    serial_sub.add_parser("ls", help="List serial ports (uses pyserial if available)")

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
    if args.command == "serial":
        # currently only `ls` is implemented
        if getattr(args, "serial_command", None) != "ls":
            print("Please specify a serial subcommand. Try: 'iomx serial ls'")
            return

        try:
            import iomx.commands.lsserial as lsmod
        except ImportError as e:
            print("serial ls requires 'pyserial' for best results. Install with: pip install pyserial")
            print(f"ImportError: {e}")
            return
        except Exception:
            import traceback

            print("Failed to import iomx.commands.lsserial — full traceback below:")
            traceback.print_exc()
            return

        # Call the module's main to reproduce the original (verbose) output
        try:
            ports = lsmod.main(verbosity=1)
        except Exception:
            import traceback

            print("Error while running lsserial.main():")
            traceback.print_exc()
            return

        if not ports:
            print("No serial ports found")
            return

        # ports are objects; copy last.device to clipboard (like the original script)
        last = ports[-1].device if hasattr(ports[-1], "device") else ports[-1]
        try:
            import pyperclip

            pyperclip.copy(last)
            print(f"\n# COPIED TO CLIPBOARD: {last}")
        except Exception:
            # Fallback to platform-specific clipboard commands
            import shutil

            system = sys.platform
            copied = False
            if system == "darwin":
                if shutil.which("pbcopy"):
                    try:
                        p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
                        p.communicate(str(last).encode())
                        copied = True
                    except Exception:
                        copied = False
            elif system.startswith("linux"):
                if shutil.which("xclip"):
                    try:
                        p = subprocess.Popen(["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE)
                        p.communicate(str(last).encode())
                        copied = True
                    except Exception:
                        copied = False
                elif shutil.which("xsel"):
                    try:
                        p = subprocess.Popen(["xsel", "--clipboard", "--input"], stdin=subprocess.PIPE)
                        p.communicate(str(last).encode())
                        copied = True
                    except Exception:
                        copied = False
            elif system.startswith("win"):
                try:
                    p = subprocess.Popen(["clip"], stdin=subprocess.PIPE)
                    p.communicate(str(last).encode())
                    copied = True
                except Exception:
                    copied = False

            if copied:
                print(f"\n# COPIED TO CLIPBOARD (fallback): {last}")
            else:
                print(f"\n# COULD NOT COPY TO CLIPBOARD — last port: {last}")
        return

    if args.command == "version":
        print(f"iomx version {VERSION}")
        return


if __name__ == "__main__":
    main(sys.argv[1:])
