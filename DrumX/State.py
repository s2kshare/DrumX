import json

class AppState:
    POWER = False
    kit = None
    menu = None
    with open('config.json', 'r') as f:
        config = json.load(f)
    default_scheme = config['controlScheme']['default']

    @classmethod
    def toggle_power(cls):
        cls.POWER = not cls.POWER
    
    @classmethod
    def get_power(cls):
        return cls.POWER
    
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
        if command in cls.default_scheme:
            print(command)