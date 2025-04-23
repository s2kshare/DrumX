import json

class AppState:
    _instance = None

    def __init__(self):
        self.power = True
        self.kit = None
        self.playing = True
        self.menu = None
        self.menu_hover = 0
        self.config = {}
        self.default_scheme = {}
        self.audio_engine = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def initialize(self, config_path="config.json", engine=None):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        if engine:
            self.set_engine(engine)
        self.default_scheme = self.config['controlScheme']['default']

    def set_engine(self, engine):
        self.audio_engine = engine

    def toggle_power(self):
        self.power = not self.power

    def get_power(self):
        return self.power

    def get_kit(self):
        return self.kit

    def set_kit(self, kit):
        self.kit = kit

    def get_menu(self):
        return self.menu

    def set_menu(self, menu):
        if menu == "main":
            pass
        if menu == "kit":
            pass
        self.menu = menu

    def get_menu_hover(self):
        return self.menu_hover

    def set_menu_hover(self, value):
        self.menu_hover = value

    def send_command(self, command):
        if command in self.default_scheme and self.playing:
            # print("Disable playing to send commands.")
            if self.audio_engine:
                if command.startswith("DP"):
                    self.audio_engine.play_sound(command)
                elif command.startswith("PROFILE"):
                    self.audio_engine.set_profile(command)
        elif command in self.default_scheme and not self.playing:
            if command == "PROFILE1":
                self.menu_hover = self.get_menu_length() - 1 if self.menu_hover - 1 < 0 else self.menu_hover - 1
            elif command == "PROFILE2":
                self.menu_hover = self.get_menu_length() + 1 if self.menu_hover + 1 < 0 else self.menu_hover + 1
            elif command == "SELECT":
                selected = self.get_selected_menu_option()
                print(f"Selected: {selected}")
                # Logic to switch menus or trigger actions
            elif command == "BACK":
                self.set_menu("main")
            else:
                print(f"Command '{command}' not recognized or not handled.")
        else:
            print("Error. How'd you get here?")
