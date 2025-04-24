from DrumX.Database import Database
from DrumX.InputHandler import InputHandler
from DrumX.AudioEngine import AudioEngine
from DrumX.Controller import Controller
from DrumX.AppState import AppState
from DrumX.utils import log, clear
from DrumX.GUI import DrumXSimpleGUI

import os
import argparse
import sys

def init():
    FILENAME = os.path.basename(__file__)
    FILEPATH = os.path.dirname(__file__)
    
    clear()
    log(f"<{FILENAME}> Starting {FILENAME}")

    # Initialize Engines
    engine = AudioEngine(bpm=80)
    controller = Controller(engine)
    inputhandler = InputHandler(engine, controller)
    app = AppState.get_instance()
    app.initialize("config.json", engine)

    # Database Load Sequence
    db = Database.get_instance()

    # Load Sounds
    engine.load_last_session_kit()
    engine.load_sound("DP1", "sounds/kick.wav")
    engine.load_sound("DP2", "sounds/HH 1.wav")
    engine.load_sound("DP3", "sounds/SNARE 1.wav")

    inputhandler.start_listening()
    
    return inputhandler, engine

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DrumX Drumpad Application")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--gui", action="store_true", help="Run the app with a GUI interface")

    args = parser.parse_args()

    inputhandler, engine = init()

    try:
        if args.gui:
            simple_gui = DrumXSimpleGUI.get_instance()
            simple_gui.run()
        else:
            log("<main.py> Loop Started")
            while True:
                pass
    except KeyboardInterrupt:
        log("<main.py> Interrupted by user", color="red")
    finally:
        try:
            inputhandler.stop()
            Database.get_instance().close()
        except Exception as e:
            log(f"Error stopping input handler: {e}", color="red")
        log("<main.py> Main Loop Stopped")

