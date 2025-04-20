from enum import Enum

class ControllerType(Enum):
    KEYBOARD = "keyboard"
    RPI = "rpi"
    GAMEPAD = "gamepad"

class Controller:
    def __init__(self, engine, config):
        
        print("Controller init:", [e.name for e in ControllerType])
        type = input("Select Controller Type: ")
        
        if type == "keyboard":
            self.type = ControllerType.KEYBOARD
        elif type == "rpi":
            self.type = ControllerType.RPI
        elif type == "gamepad":
            self.type = ControllerType.GAMEPAD

        self.engine = engine
        self.config = config