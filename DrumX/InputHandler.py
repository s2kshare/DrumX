from DrumX.Controller import ControllerType
from DrumX.utils import *
from DrumX.State import AppState
from pynput import keyboard

class InputHandler:
    def __init__(self, engine, controller):
        self.engine = engine
        self.controller = controller
        self.running = True

    def start_listening(self):
        if self.controller.type == ControllerType.KEYBOARD:
            listener = keyboard.Listener(on_press=self.on_press)
            listener.start()

    def on_press(self, key):
        try:
            input_key = key.char.upper()
            if input_key == self.controller.control_scheme["DP1"]:
                AppState.send_command("DP1")
            if input_key == self.controller.control_scheme["DP2"]:
                AppState.send_command("DP2")
            if input_key == self.controller.control_scheme["DP3"]:
                AppState.send_command("DP3")
            if input_key == self.controller.control_scheme["DP4"]:
                AppState.send_command("DP4")
            if input_key == self.controller.control_scheme["DP5"]:
                AppState.send_command("DP5")
            if input_key == self.controller.control_scheme["DP6"]:
                AppState.send_command("DP6")
            if input_key == self.controller.control_scheme["DP7"]:
                AppState.send_command("DP7")
            if input_key == self.controller.control_scheme["DP8"]:
                AppState.send_command("DP8")
            if input_key == self.controller.control_scheme["DP9"]:
                AppState.send_command("DP9")
            if input_key == self.controller.control_scheme["DP10"]:
                AppState.send_command("DP10")
            if input_key == self.controller.control_scheme["DP11"]:
                AppState.send_command("DP11")
            if input_key == self.controller.control_scheme["DP12"]:
                AppState.send_command("DP12")
            if input_key == self.controller.control_scheme["DP13"]:
                AppState.send_command("DP13")
            if input_key == self.controller.control_scheme["DP14"]:
                AppState.send_command("DP14")
            if input_key == self.controller.control_scheme["DP15"]:
                AppState.send_command("DP15")
            if input_key == self.controller.control_scheme["DP16"]:
                AppState.send_command("DP16")
            if input_key == self.controller.control_scheme["KB1"]:
                AppState.send_command("KB1")
            if input_key == self.controller.control_scheme["KB2"]:
                AppState.send_command("KB2")
            if input_key == self.controller.control_scheme["KB3"]:
                AppState.send_command("KB3")
            if input_key == self.controller.control_scheme["KB4"] or key.name.upper() == self.controller.control_scheme["KB4"]:
                AppState.send_command("KB4")
            if input_key == self.controller.control_scheme["MENU"] or key.name.upper() == self.controller.control_scheme["MENU"]:
                AppState.send_command("MENU")
            if input_key == self.controller.control_scheme["SELECT"] or key.name.upper() == self.controller.control_scheme["SELECT"]:
                AppState.send_command("SELECT")
            if input_key == self.controller.control_scheme["BACK"] or key.name.upper() == self.controller.control_scheme["BACK"]:
                AppState.send_command("BACK")
            if input_key == self.controller.control_scheme["OPTIONS"] or key.name.upper() == self.controller.control_scheme["OPTIONS"]:
                AppState.send_command("OPTIONS")
            if input_key == self.controller.control_scheme["RECORD"] or key.name.upper() == self.controller.control_scheme["RECORD"]:
                AppState.send_command("RECORD")
            if input_key == self.controller.control_scheme["PROFILE1"] or key.name.upper() == self.controller.control_scheme["PROFILE1"]:
                AppState.send_command("PROFILE1")
            if input_key == self.controller.control_scheme["PROFILE2"] or key.name.upper() == self.controller.control_scheme["PROFILE2"]:
                AppState.send_command("PROFILE2")
            if input_key == self.controller.control_scheme["PROFILE3"] or key.name.upper() == self.controller.control_scheme["PROFILE3"]:
                AppState.send_command("PROFILE3")
            if input_key == self.controller.control_scheme["PROFILE4"] or key.name.upper() == self.controller.control_scheme["PROFILE4"]:
                AppState.send_command("PROFILE4")
            # self.engine.play_sound(self.controller.control_scheme[input_key])
        except AttributeError:
            pass

    def stop(self):
        self.running = False

