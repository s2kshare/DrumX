from enum import Enum
import json
from DrumX.utils import log

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
        else:
            log(f"Invalid controller type: {type}", "red")
            raise ValueError(f"Invalid controller type: {type}")
            quit
        
        log(f"Controller connected: {self.type}", "cyan")

        self.engine = engine
        self.config = config
        self.control_scheme = config['controlScheme'][self.type.value]
