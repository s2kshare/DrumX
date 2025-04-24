from tkinter import *
import tkinter.colorchooser as colorchooser
import json
import os

class DrumXSimpleGUI:
    """
    Main GUI class for DrumX Simple GUI application.
    Implements a singleton pattern to ensure only one instance exists.
    """
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """Get or create the singleton instance of the GUI"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
        
    def __init__(self):
        """Initialize the GUI with all components"""
        # Main window setup
        self.window = Tk()
        self.window.geometry('500x700')
        self.window.title("DrumX Simple GUI")
        self.buttons = {}  # Dictionary for quick lookup by ID
        
        # Load configuration
        self.config = self.load_config()
        self.controller_type = self.config.get("controllerType", "keyboard")
        
        # Settings variables
        self.show_input_keys = BooleanVar(value=False)
        self.highlight_color = "red"
        self.pad_color = "black"
        
        # Create the menubar
        self.create_menubar()
        
        # Build the UI components
        self.build_header()
        self.build_controls()
        self.build_drumpad()
                
    def load_config(self):
        """
        Load configuration from config.json file.
        
        Returns:
            dict: The configuration data or a default config if loading fails
        """
        try:
            config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            # Return small default config
            return {
                "controllerType": "keyboard",
                "controlScheme": {
                    "keyboard": {
                        "DP1": "1", "DP2": "2", "DP3": "3", "DP4": "4",
                        "DP5": "Q", "DP6": "W", "DP7": "E", "DP8": "R",
                        "DP9": "A", "DP10": "S", "DP11": "D", "DP12": "F",
                        "DP13": "Z", "DP14": "X", "DP15": "C", "DP16": "V"
                    }
                }
            }
    
    def build_header(self):
        """Build the header section of the GUI"""
        frame_header = Frame(self.window, pady=50)
        frame_header.pack(side=TOP)
        Label(frame_header, text="DrumX Simple GUI", font=("Courier", 18)).pack()
        Label(frame_header, text="Intended for testing purposes").pack()
    
    def build_controls(self):
        """Build the control section including knobs, function buttons, and navigation buttons"""
        # Container for all controls
        frame_switches = Frame(self.window, pady=0)
        frame_switches.pack(side=TOP)
        
        # Build knobs section
        self.build_knobs(frame_switches)
        
        # Build function button section
        self.build_function_button(frame_switches)
        
        # Build navigation buttons section
        self.build_navigation_buttons(frame_switches)
    
    def build_knobs(self, parent_frame):
        """
        Build the knobs section.
        
        Args:
            parent_frame: The parent frame to place the knobs
        """
        frame_knobs = Frame(parent_frame)
        frame_knobs.grid(row=0, column=0)
        
        for i in range(4):
            btn_id = f"KB{i+1}"
            key_mapping = self.get_key_mapping(btn_id)
            
            button = Button(frame_knobs, text=str(i), width=1, height=1, bg=self.pad_color, fg="white")
            button.grid(row=0, column=i, padx=1, pady=1)
            self.buttons[btn_id] = button
    
    def build_function_button(self, parent_frame):
        """
        Build the function button section.
        
        Args:
            parent_frame: The parent frame to place the function button
        """
        frame_functionButton = Frame(parent_frame)
        frame_functionButton.grid(row=0, column=1)
        
        btn_id = "FUNCTION"
        key_mapping = self.get_key_mapping(btn_id)
        
        button_function = Button(frame_functionButton, text="Fn", width=4, height=5, bg=self.pad_color, fg="white")
        button_function.grid(row=0, column=0, padx=4, pady=4)
        self.buttons[btn_id] = button_function
    
    def build_navigation_buttons(self, parent_frame):
        """
        Build the navigation buttons section.
        
        Args:
            parent_frame: The parent frame to place the navigation buttons
        """
        frame_navigationButtons = Frame(parent_frame)
        frame_navigationButtons.grid(row=0, column=2)
        
        # First row of navigation buttons
        nav_buttons_row1 = [
            ("SELECT", "Select", 0, 0),
            ("BACK", "Back", 0, 1),
            ("OPTIONS", "Options", 0, 2),
            ("RECORD", "Record", 0, 3)
        ]
        
        # Second row of navigation buttons
        nav_buttons_row2 = [
            ("PROFILE1", "Profile 1", 1, 0),
            ("PROFILE2", "Profile 2", 1, 1),
            ("PROFILE3", "Profile 3", 1, 2),
            ("MENU", "Menu", 1, 3)
        ]
        
        # Create all navigation buttons
        for btn_id, text, row, col in nav_buttons_row1 + nav_buttons_row2:
            key_mapping = self.get_key_mapping(btn_id)
            button = Button(frame_navigationButtons, text=text, width=4, height=2, bg=self.pad_color, fg="white")
            button.grid(row=row, column=col, padx=4, pady=4)
            self.buttons[btn_id] = button
    
    def build_drumpad(self):
        """Build the drumpad section with a 4x4 grid of buttons"""
        frame_drumpad = Frame(self.window, pady=10)
        frame_drumpad.pack()
        
        for row in range(4):
            for col in range(4):
                index = row * 4 + col + 1
                btn_id = f"DP{index}"
                key_mapping = self.get_key_mapping(btn_id)
                
                btn = Button(frame_drumpad, text=btn_id, width=8, height=4, bg=self.pad_color, fg="white")
                btn.grid(row=row, column=col, padx=4, pady=4)
                self.buttons[btn_id] = btn
    
    def get_key_mapping(self, button_id):
        """
        Get the key mapping for a specific button ID based on the current controller type.
        
        Args:
            button_id: The ID of the button to get mapping for
            
        Returns:
            str: The key mapped to this button or empty string if not mapped
        """
        try:
            return self.config["controlScheme"][self.controller_type].get(button_id, "")
        except (KeyError, TypeError):
            return ""
                
    def create_menubar(self):
        """Create menubar with menu items"""
        # Create the main menubar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        
        # Create File menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Sounds", command=self.load_sounds)
        file_menu.add_command(label="Load VSTs", command=self.load_vsts)
        file_menu.add_command(label="Load Extensions", command=self.load_extensions)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
        
        # Create Settings menu
        settings_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_checkbutton(label="Show input keys", variable=self.show_input_keys, 
                                      command=self.toggle_input_keys)
        settings_menu.add_command(label="Set Highlight Color", command=self.set_highlight_color)
        settings_menu.add_command(label="Set Pad Color", command=self.set_pad_color)
        
        # Create Controller Type submenu
        controller_menu = Menu(settings_menu, tearoff=0)
        settings_menu.add_cascade(label="Controller Type", menu=controller_menu)
        
        # Add controller type options
        self.controller_var = StringVar(value=self.controller_type)
        for controller in ["keyboard", "gamepad", "rpi"]:
            if controller in self.config.get("controlScheme", {}):
                controller_menu.add_radiobutton(
                    label=controller.capitalize(),
                    variable=self.controller_var,
                    value=controller,
                    command=self.change_controller_type
                )
    
    # Menu command functions
    def load_sounds(self):
        """Handle loading sounds from the menu"""
        print("Loading sounds...")
        # Add your functionality here
    
    def load_vsts(self):
        """Handle loading VSTs from the menu"""
        print("Loading VSTs...")
        # Add your functionality here
    
    def load_extensions(self):
        """Handle loading extensions from the menu"""
        print("Loading extensions...")
        # Add your functionality here
    
    def toggle_input_keys(self):
        """
        Toggle between showing pad IDs and input keys on buttons.
        Updates all button texts based on the current setting.
        """
        show_keys = self.show_input_keys.get()
        print(f"Show input keys: {show_keys}")
        
        # Update all buttons with their corresponding key mappings
        for btn_id, button in self.buttons.items():
            if show_keys:
                key = self.get_key_mapping(btn_id)
                if key:  # Only show key if it exists
                    button.config(text=f"{btn_id}\n{key}")
                else:
                    button.config(text=btn_id)
            else:
                # Remove key mapping display
                button.config(text=btn_id)
    
    def change_controller_type(self):
        """
        Change the controller type and update button mappings.
        Called when a different controller type is selected from the menu.
        """
        self.controller_type = self.controller_var.get()
        print(f"Controller type changed to: {self.controller_type}")
        
        # Update button labels if showing input keys
        if self.show_input_keys.get():
            self.toggle_input_keys()
    
    def set_highlight_color(self):
        """
        Open color chooser dialog to select highlight color.
        Updates the highlight color used when buttons are toggled.
        """
        color = colorchooser.askcolor(title="Choose Highlight Color", initialcolor=self.highlight_color)[1]
        if color:
            self.highlight_color = color
            print(f"Highlight color set to: {color}")
    
    def set_pad_color(self):
        """
        Open color chooser dialog to select pad color.
        Updates the default color of all pad buttons.
        """
        color = colorchooser.askcolor(title="Choose Pad Color", initialcolor=self.pad_color)[1]
        if color:
            self.pad_color = color
            print(f"Pad color set to: {color}")
            
            # Update all buttons with the new color
            for button in self.buttons.values():
                if button.cget("bg") != self.highlight_color:  # Don't change highlighted buttons
                    button.config(bg=color)
        
    def toggle_button(self, btn_id):
        """
        Toggle the color state of a button between default and highlighted.
        
        Args:
            btn_id: The ID of the button to toggle
        """
        if btn_id in self.buttons:
            btn = self.buttons[btn_id]
            current_color = btn.cget("bg")
            new_color = self.highlight_color if current_color != self.highlight_color else self.pad_color
            self.window.after(0, lambda: btn.config(bg=new_color))
    
    def run(self):
        """Start the main application loop"""
        self.window.mainloop()

if __name__ == "__main__":
    app = DrumXSimpleGUI.get_instance()
    app.run()