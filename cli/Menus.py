import time
from cli.utils import *
from DrumX.State import AppState

REFRESH = 0.5
default = get_default_scheme()
MENUS = {
    "main": ["PROFILE1", "PROFILE2", "PROFILE3", "PROFILE4"],
    "kit": ["DP1", "DP2", "DP3", "DP4"]
}

import os

def MainMenu():
    menu_items = ["PLAYING: ON" if AppState.get_power() else "PLAYING: OFF",
                  "EDIT KIT", "EDIT PADS", "FILE MANAGER"]
    os.system("cls" if os.name == "nt" else "clear")
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->\n")
    print("                        DrumX")
    print("                    [ MAIN MENU ]\n")
    selected = AppState.get_menu_hover()
    for i, item in enumerate(menu_items):
        prefix = "* " if i == selected else "  "
        print(f"{prefix}[ PROFILE{i+1} ] {item}")
    
    print("\n<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-\n")



def KitMenu():
    print("->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->\n")
    print("                        DrumX")
    print("                    [ MAIN MENU ]\n")
    current_menu = AppState.get_menu() or "kit"
    AppState.set_menu(current_menu)
    menu_items = MENUS[current_menu]
    for i, key in enumerate(menu_items):
        prefix = "* " if i == AppState.get_menu_hover() else "  "
        print(f"{prefix}[ {key} ]")
    
    print()
    print("[ PROFILE4 ] FILE MANAGER\n")
    print("<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-\n")