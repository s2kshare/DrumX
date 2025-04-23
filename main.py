from DrumX.Database import Database
from DrumX.InputHandler import InputHandler
from DrumX.AudioEngine import AudioEngine
from DrumX.Controller import Controller
from DrumX.AppState import AppState
from DrumX.utils import log
import os

def run():
    FILENAME = os.path.basename(__file__)
    FILEPATH = os.path.dirname(__file__)
    log(f"<{FILENAME}> Starting {FILENAME}")

    # Initialize Engines
    engine = AudioEngine(bpm=80)
    controller = Controller(engine)
    inputhandler = InputHandler(engine, controller)
    app = AppState.get_instance()
    app.initialize("config.json", engine)

    # Database Load Sequence
    db = Database.get_instance()
    print(db)
    print(db)
    print(db)
    print(db)
    print(db)

    # Load Sounds
    engine.load_last_session_kit()
    engine.load_sound("DP1", "sounds/kick.wav")
    engine.load_sound("DP2", "sounds/HH 1.wav")
    engine.load_sound("DP3", "sounds/SNARE 1.wav")

    inputhandler.start_listening()
    
    log(f"<{FILENAME}> Loop Started")
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        log(f"<{FILENAME}> Interrupted by user", color="red")
    finally:
        try:
            inputhandler.stop()
            Database.get_instance().close()
        except Exception as e:
            log(f"Error stopping input handler: {e}", color="red")
        log(f"<{FILENAME}> Main Loop Stopped")

if __name__ == "__main__":
    run()
