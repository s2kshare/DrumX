from DrumX.InputHandler import InputHandler
from DrumX.AudioSuite import AudioEngine
from DrumX.Controller import Controller
from DrumX.utils import *
import os

# Initialize
os.system('cls' if os.name == 'nt' else 'clear')
FILENAME = os.path.basename(__file__)
FILEPATH = os.path.dirname(__file__)
log(f"<{FILENAME}> Starting {FILENAME}")

# Global Variables
engine = AudioEngine(bpm=80)
controller = Controller(engine)
inputhandler = InputHandler(engine, controller)

engine.load_sound(0, "sounds/kick.wav")
engine.set_loop(0)

inputhandler.start_listening()

log(f"<{FILENAME}> Loop Started")
try:
    while True:
        pass
except KeyboardInterrupt:
    log(f"<{FILENAME}> Main Loop Stopped")
    try:
        inputhandler.stop()
    except Exception as e:
        log(str(e), color="red")