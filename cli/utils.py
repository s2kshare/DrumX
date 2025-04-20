import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_default_scheme():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config['controlScheme']['default']