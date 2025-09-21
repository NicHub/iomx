"""

lsserial.py

This script lists the serial devices connected in verbose and summarized lists.
It is tested on Python3 only.
If you prefer a single line command, there are some alternatives below.

# Prerequisites
pip install pyserial
or
python3 -m pip install pyserial

# Create alias in ~/.bash_profile or ~/.zshrc
alias lsserial='python3 ~/lsserial.py'

# If you only need the summary, you just need to run this command in bash
python3 -m serial.tools.list_ports

# Alternate solution in pure bash for macOS
alias lsserial_b='ls -1 /dev/tty.* | grep -v -e Bluetooth -e Jabra'

# Alternate solution in pure bash for Raspberry Pi OS
alias lsserial_b='ls -1 /dev/tty* | grep tty[A-Z] | grep -v -e Bluetooth -e Jabra'

# Ubuntu & Raspberry Pi OS serial diagnostic with this command
dmesg

"""

import serial.tools.list_ports
import sys
import time
import platform
import subprocess
import threading

NB_ITER = 0
EXCLUDED_PORTS = [
    "Bluetooth",
    "Jabra",
    "debug-console",
]

SOUNDTRACKS = [
    "/Library/Application Support/GarageBand/Instrument Library/Sampler/Sampler Files/String Ensemble/05n7aE2.wav",
    "/System/Library/Sounds/Basso.aiff",
    "/System/Library/Sounds/Blow.aiff",
    "/System/Library/Sounds/Bottle.aiff",
    "/System/Library/Sounds/Frog.aiff",
    "/System/Library/Sounds/Funk.aiff",
    "/System/Library/Sounds/Glass.aiff",
    "/System/Library/Sounds/Hero.aiff",
    "/System/Library/Sounds/Morse.aiff",
    "/System/Library/Sounds/Ping.aiff",
    "/System/Library/Sounds/Pop.aiff",
    "/System/Library/Sounds/Purr.aiff",
    "/System/Library/Sounds/Sosumi.aiff",
    "/System/Library/Sounds/Submarine.aiff",
    "/System/Library/Sounds/Tink.aiff",
]

system = platform.system()
SOUND_COMMANDS = {
    "Darwin": f"afplay '{SOUNDTRACKS[8]}'",
    "Linux": 'aplay -q /usr/share/sounds/sound-icons/alert.wav 2>/dev/null || echo -e "\a"',
}
SOUND_COMMAND = SOUND_COMMANDS.get(system, "")

MUSIC_THREAD = None
MUSIC_PLAYING = False


def scan_serial_ports():
    """___"""
    ports = []
    for port in serial.tools.list_ports.comports():
        excluded_found = False
        for excluded_port in EXCLUDED_PORTS:
            if port.device.find(excluded_port) > -1:
                excluded_found = True
                break
        if excluded_found:
            continue
        ports.append(port)
    return ports


def list_serial_ports():
    """Compatibility wrapper for simple programmatic use.

    Returns a list of device name strings (e.g. ['/dev/cu.USB0']).
    """
    return [p.device for p in scan_serial_ports()]


def play_music_nonblocking(start_stop=False):
    """___"""

    global MUSIC_THREAD, MUSIC_PLAYING

    def play_music_thread():
        global MUSIC_PLAYING
        MUSIC_PLAYING = True
        while MUSIC_PLAYING:
            try:
                subprocess.run(SOUND_COMMAND, shell=True, check=False)

                # Use shorter sleep intervals to make stopping more responsive
                for _ in range(10):
                    if not MUSIC_PLAYING:
                        break
                    time.sleep(0.01)
            except Exception as e:
                print(f"Error playing sound: {e}")
                MUSIC_PLAYING = False
                break

    if start_stop:
        if not MUSIC_PLAYING:
            MUSIC_THREAD = threading.Thread(target=play_music_thread)
            MUSIC_THREAD.daemon = True
            MUSIC_THREAD.start()
    else:
        MUSIC_PLAYING = False


def monitor_port_availability(ports):
    """___"""
    global NB_ITER
    NB_ITER = 0
    all_ports_available_prev = True
    while True:
        available_ports = serial.tools.list_ports.comports()
        available_port_names = [port.device for port in available_ports]
        all_ports_available = all(port in available_port_names for port in ports)
        if all_ports_available_prev != all_ports_available:
            subprocess.run(f"afplay '{SOUNDTRACKS[1]}'", shell=True, check=False)
            all_ports_available_prev = all_ports_available
        else:
            play_music_nonblocking(start_stop=not all_ports_available)
        NB_ITER += 1
        if all_ports_available:
            print(f"{NB_ITER = }", end="\r", flush=True)  # noqa
        else:
            missing_ports = [port for port in ports if port not in available_port_names]
            main()
            print(f"\n\n# MISSING: {missing_ports}")

        time.sleep(1)


def lsserial_verbosity_1(ports):
    """___"""
    print("\n\n# SERIAL PORTS DETAILS")
    for counter, port in enumerate(ports):
        print("")
        print("- ID:                    %d" % (counter))
        print("  port.device:           %s" % (port.device))
        print("  port.name:             %s" % (port.name))
        print("  port.description:      %s" % (port.description))
        print("  port.hwid:             %s" % (port.hwid))
        print("  port.vid:              %s" % (port.vid))
        print("  port.pid:              %s" % (port.pid))
        print("  port.serial_number:    %s" % (port.serial_number))
        print("  port.location:         %s" % (port.location))
        print("  port.manufacturer:     %s" % (port.manufacturer))
        print("  port.product:          %s" % (port.product))
        print("  port.interface:        %s" % (port.interface))


def lsserial_verbosity_0(ports):
    """___"""
    print("\n\n# SERIAL PORTS SUMMARY\n")
    for counter, port in enumerate(ports):
        print("- %s. port.device: %s" % (counter, port.device))


def main(verbosity=0):
    """___"""
    ports = scan_serial_ports()
    if len(ports) == 0:
        print("\n\n# NO SERIAL PORT FOUND")
        return ports

    if verbosity > 0:
        lsserial_verbosity_1(ports)
    lsserial_verbosity_0(ports)
    return ports


if __name__ == "__main__":

    """
USAGE:

lsserial \
/dev/cu.usbmodem114201 \
/dev/cu.usbmodem11101  \
/dev/cu.usbmodem11201  \
/dev/cu.usbmodem11301  \
/dev/cu.usbmodem114301 \
/dev/cu.usbmodem114101 \
    """

    try:
        ports = main(verbosity=1)
        if len(sys.argv) > 1 and "ipykernel" not in sys.modules:
            ports = sys.argv[1:]
            monitor_port_availability(ports)
        if not ports:
            raise SystemExit()
        try:
            import pyperclip

            pyperclip.copy(ports[-1].device)
            print(f"\n\n# COPIED TO CLIPBOARD\n\n    {ports[-1].device}")
        except Exception:
            # If pyperclip is not available or fails, just print the last device
            print(f"\n\n# LAST PORT: {ports[-1].device}")
    except SystemExit:
        pass
    except KeyboardInterrupt:
        print("\r" "\033[2K" "\033[A", end="", flush=True)
    else:
        print(f"\n\n# FINALLY {NB_ITER = }", end="\n\n", flush=True)  # noqa
