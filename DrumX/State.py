import json

MENUS = {
    "main": ["PROFILE1", "PROFILE2", "PROFILE3", "PROFILE4"],
    "kit": ["DP1", "DP2", "DP3", "DP4"]
}

class AppState:
    
    power = False           # State of power
    kit = None              # Selected kit
    playing = True          # State of playing
    menu = None             # Menu being displayed
    menu_hover = 0          # Index of menu being hovered
    config = {}             # Config
    default_scheme = {}     # Default control scheme
    audio_engine = None     # Audio engine

    def initialize(cls, config_path="config.json", engine=None):
        with open(config_path, 'r') as f:
            cls.config = json.load(f)
        if engine:
            cls.set_engine(engine)
        cls.default_scheme = cls.config['controlScheme']['default']

    @classmethod
    def set_engine(cls, engine):
        cls.audio_engine = engine

    @classmethod
    def toggle_power(cls):
        cls.power = not cls.power
    
    @classmethod
    def get_power(cls):
        return cls.power
    
    @classmethod
    def get_kit(cls):
        return cls.kit
    
    @classmethod
    def set_kit(cls, kit):
        cls.kit = kit
        return
    
    @classmethod
    def get_menu(cls):
        return cls.menu

    @classmethod
    def set_menu(cls, menu):
        cls.menu = menu
    
    @classmethod
    def send_command(cls, command):
        if command in cls.default_scheme and not cls.playing:
            print("Disable playing to send commands.")



        # TODO: Fix navigation
        if command == "PROFILE1":
            cls.menu_hover = cls.get_menu_length() - 1 if cls.menu_hover - 1 < 0 else cls.menu_hover - 1
            
        elif command == "PROFILE2":
            cls.menu_hover = cls.get_menu_length() + 1 if cls.menu_hover + 1 < 0 else cls.menu_hover + 1
        elif command == "SELECT":
            selected = cls.get_selected_menu_option()
            print(f"Selected: {selected}")
            # Add logic to switch menus or trigger actions
        elif command == "BACK":
            cls.set_menu("main")
        else:
            print(f"Command '{command}' not recognized or not handled.")


    @classmethod
    def get_menu_hover(cls):
        return cls.menu_hover

    @classmethod
    def set_menu_hover(cls, value):
        cls.menu_hover = value

    @classmethod
    def get_menu_length(cls):
        current_menu = cls.get_menu()
        return len(MENUS.get(current_menu, []))

    @classmethod
    def get_selected_menu_option(cls):
        current_menu = cls.get_menu()
        hover = cls.get_menu_hover()
        return MENUS.get(current_menu, [])[hover]
