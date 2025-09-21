"""List serial ports utility (moved from iomx.tools)."""
from typing import List
import sys


def list_serial_ports() -> List[str]:
    try:
        import serial.tools.list_ports as list_ports
    except Exception:
        list_ports = None

    ports = []
    if list_ports is not None:
        for p in list_ports.comports():
            ports.append(p.device)
        return ports

    # fallback
    import glob

    if sys.platform.startswith("linux"):
        candidates = glob.glob("/dev/ttyS*") + glob.glob("/dev/ttyUSB*") + glob.glob("/dev/ttyACM*")
    elif sys.platform == "darwin":
        candidates = glob.glob("/dev/tty.*") + glob.glob("/dev/cu.*")
    elif sys.platform.startswith("win"):
        candidates = [f"COM{i}" for i in range(1, 257)]
    else:
        candidates = []

    return candidates


def main():
    ports = list_serial_ports()
    if not ports:
        print("No serial ports found")
        return
    for p in ports:
        print(p)


if __name__ == "__main__":
    main()
