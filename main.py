from DrumX.InputHandler import InputHandler
from DrumX.AudioSuite import AudioEngine
from DrumX.Controller import Controller
from DrumX.State import AppState
from DrumX.utils import log
import os

# Menu Imports
from cli.Menus import MainMenu, KitMenu

def run():
    FILENAME = os.path.basename(__file__)
    FILEPATH = os.path.dirname(__file__)
    log(f"<{FILENAME}> Starting {FILENAME}")

    engine = AudioEngine(bpm=80)
    controller = Controller(engine)
    inputhandler = InputHandler(engine, controller)

    engine.load_sound("DP1", "sounds/kick.wav")
    inputhandler.start_listening()
    log(f"<{FILENAME}> Loop Started")
    AppState.set_menu(MainMenu)

    try:
        menu = AppState.get_menu()
        menu()
    except KeyboardInterrupt:
        log(f"<{FILENAME}> Interrupted by user", color="red")
    finally:
        try:
            inputhandler.stop()
        except Exception as e:
            log(f"Error stopping input handler: {e}", color="red")
        log(f"<{FILENAME}> Main Loop Stopped")

if __name__ == "__main__":
    run()
