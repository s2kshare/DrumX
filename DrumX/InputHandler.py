from DrumX.Controller import ControllerType 
from DrumX.utils import *
from pynput import keyboard

class InputHandler:
    def __init__(self, engine, controller):
        self.engine = engine
        self.controller = controller
        self.running = True

    def start_listening(self):

        if (self.controller.type == ControllerType.KEYBOARD):
            listener = keyboard.Listener(on_press=self.on_press)
            listener.start()

        elif (self.controller.type == ControllerType.RPI):
            pass

        elif (self.controller.type == ControllerType.GAMEPAD):
            pass

    def on_press(self, key):
        try:
            if key.char in self.controller.control_scheme:
                log(f"Pressed {key}")
                # INFO: Captures Input Here
                self.engine.play_sound(self.controller.control_scheme[key.char])
        except AttributeError:
            pass

    def stop(self):
        self.running = False

