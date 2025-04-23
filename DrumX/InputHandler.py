from DrumX.Controller import ControllerType
from DrumX.utils import *
from DrumX.AppState import AppState
from pynput import keyboard

# TODO: Refactor on_press for multiple inputs or change name

class InputHandler:
    def __init__(self, engine, controller):
        self.engine = engine
        self.controller = controller
        self.running = True
        self.state = AppState.get_instance()
        self.holdingFunction = False

    def start_listening(self):
        if self.controller.type == ControllerType.KEYBOARD:
            listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
            listener.start()
    
    def on_release(self, key):
        try:
            key_name = key.name.upper()
        except AttributeError:
            key_name = None
        print(key)

        if self.holdingFunction and key == "FUNCTION":
            self.holdingFunction = False


    def on_press(self, key):
        try:
            input_key = key.char.upper()
        except AttributeError:
            input_key = None

        try:
            key_name = key.name.upper()
        except AttributeError:
            key_name = None

        if key == "FUNCTION":
            self.holdingFunction = True

        for command in [
            "DP1", "DP2", "DP3", "DP4", "DP5", "DP6", "DP7", "DP8",
            "DP9", "DP10", "DP11", "DP12", "DP13", "DP14", "DP15", "DP16",
            "KB1", "KB2", "KB3", "KB4",
            "MENU", "SELECT", "BACK", "OPTIONS", "RECORD",
            "PROFILE1", "PROFILE2", "PROFILE3", "FUNCTION"
        ]:
            mapped_key = self.controller.control_scheme.get(command)
            if input_key == mapped_key or key_name == mapped_key:
                self.state.send_command(command)
                break

    def stop(self):
        self.running = False

