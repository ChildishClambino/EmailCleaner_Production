import sys
import os

# Add the project root directory to the system path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from gui.app_gui import launch_gui

if __name__ == "__main__":
    launch_gui()
