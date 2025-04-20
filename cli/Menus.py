import time
from cli.utils import *
from DrumX.State import AppState

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

REFRESH = 0.3

def MainMenu():
    while True:
        clear()
        print("   DrumX")
        print("[ MAIN MENU ] \n")

        print(f"[ M1  ] PLAYING: {'ON' if AppState.get_power() else 'OFF'}")
        print("[ M2  ] EDIT KIT")
        print("[ M3  ] EDIT PADS")
        
        print()
        print("[ M4  ] FILE MANAGER")
        print()
        
        print("[ PWR ] QUIT\n")
        time.sleep(REFRESH)

def KitMenu():
    while True:
        clear()
        print("   DrumX\n")
        print("[ KIT MENU ] \n\n")

        print("BUTTON            | NAME")

        print(f"[ M1  ] ")
        print("[ M3  ] EDIT PADS")
        print()
        print("[ M4  ] FILE MANAGER")
        print()
        print("[ PWR ] QUIT\n")
        time.sleep(REFRESH)