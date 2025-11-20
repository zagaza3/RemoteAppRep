import os
import sys

# Detect program directory (works for Python + PyInstaller)
BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))

# Path to nircmd.exe in the same folder
NIRCMD = os.path.join(BASE_DIR, "nircmd.exe")

def volume_up():
    os.system(f'"{NIRCMD}" changesysvolume 5000')

def volume_down():
    os.system(f'"{NIRCMD}" changesysvolume -5000')

def volume_mute():
    os.system(f'"{NIRCMD}" mutesysvolume 2')

def play_pause():
    os.system(f'{NIRCMD} win activate title "Windows Media Player"')
    os.system(f'{NIRCMD} win activate title "Brave"')
    os.system(f'"{NIRCMD}" sendkeypress media_play_pause')

def next_track():
    os.system(f'"{NIRCMD}" sendkeypress media_next')

def prev_track():
    os.system(f'"{NIRCMD}" sendkeypress media_prev')

# TEST
if __name__ == "__main__":
    print("Testing play/pause…")
    volume_mute()