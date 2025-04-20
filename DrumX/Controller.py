from enum import Enum
import json

class ControllerType(Enum):
    KEYBOARD = "keyboard"
    RPI = "rpi"
    GAMEPAD = "gamepad"

class Controller:
    def __init__(self, engine, config = "config.json"):
        with open(config) as f:
            config = json.load(f)
        
        # Import Controller type from config
        type = config['controllerType']
        if type == "keyboard":
            self.type = ControllerType.KEYBOARD
        elif type == "rpi":
            self.type = ControllerType.RPI
        elif type == "gamepad":
            self.type = ControllerType.GAMEPAD

        self.engine = engine
        self.config = config