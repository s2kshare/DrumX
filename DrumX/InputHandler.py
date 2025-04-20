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
            self._listen()

        elif (self.controller.type == ControllerType.GAMEPAD):
            self._listen()

    def on_press(self, key):
        try:
            if key.char in self.controller.control_scheme:
                log(f"Pressed {key}")
                # INFO: Captures Input Here
        except AttributeError:
            pass

    def _listen(self):
        if self.controller.type == ControllerType.RPI:
            while self.running:
                # TODO: Implement logic
                pass

        # Keyboard
        elif self.controller.type == ControllerType.KEYBOARD:
            while self.running:
                for key, sound_index in self.controller.control_scheme.items():
                    if keyboard.is_pressed(key):

                        # INFO : This is live key registration 
                        log(f"Pressed {key}")
                        self.engine.play_sound(sound_index)

        elif self.controller.type == ControllerType.GAMEPAD:
            while self.running:
                # TODO: Implement logic
                pass
    
    def stop(self):
        self.running = False

