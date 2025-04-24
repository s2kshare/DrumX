from tkinter import *

# TODO: Capture close event to stop the audio engine

class DrumXSimpleGUI:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.window = Tk()
        self.window.geometry('450x700')
        self.window.title("DrumX Simple GUI")

        self.buttons = {}  # Dictionary for quick lookup by ID

        # Header
        frame_header = Frame(self.window, pady=50)
        frame_header.pack(side=TOP)
        Label(frame_header, text="DrumX Simple GUI", font=("Courier", 18)).pack()
        Label(frame_header, text="Inteded for testing purposes").pack()

        # Switches Frame
        frame_switches = Frame(self.window, pady=0)
        frame_switches.pack(side=TOP)

        frame_knobs = Frame(frame_switches)
        frame_knobs.grid(row=0, column=0)

        for i in range(4):
            button = Button(frame_knobs, text=str(i), width=1, height=1, bg="black", fg="white")
            button.grid(row=0, column=i, padx=1, pady=1)
            self.buttons[i] = button

        frame_navigationButtons = Frame(frame_switches)
        frame_navigationButtons.grid(row=0, column=2)

        button_select = Button(frame_navigationButtons, text="Select", width=4, height=2, bg="black", fg="white")
        button_select.grid(row=0, column=0, padx=4, pady=4)

        button_back = Button(frame_navigationButtons, text="Back", width=4, height=2, bg="black", fg="white")
        button_back.grid(row=0, column=1, padx=4, pady=4)

        button_options = Button(frame_navigationButtons, text="Options", width=4, height=2, bg="black", fg="white")
        button_options.grid(row=0, column=2, padx=4, pady=4)

        button_record = Button(frame_navigationButtons, text="Record", width=4, height=2, bg="black", fg="white")
        button_record.grid(row=0, column=3, padx=4, pady=4)

        button_profile1 = Button(frame_navigationButtons, text="Profile 1", width=4, height=2, bg="black", fg="white")
        button_profile1.grid(row=1, column=0, padx=4, pady=4)

        button_profile2 = Button(frame_navigationButtons, text="Profile 2", width=4, height=2, bg="black", fg="white")
        button_profile2.grid(row=1, column=1, padx=4, pady=4)

        button_profile3 = Button(frame_navigationButtons, text="Profile 3", width=4, height=2, bg="black", fg="white")
        button_profile3.grid(row=1, column=2, padx=4, pady=4)

        button_profile4 = Button(frame_navigationButtons, text="Profile 4", width=4, height=2, bg="black", fg="white")
        button_profile4.grid(row=1, column=3, padx=4, pady=4)

        # Drumpad Frame (4x4 Grid)
        frame_drumpad = Frame(self.window, pady=10)
        frame_drumpad.pack()

        for row in range(4):
            for col in range(4):
                index = row * 4 + col + 1
                btn_id = f"DP{index}"
                btn = Button(frame_drumpad, text=btn_id, width=8, height=4, bg="black", fg="white")
                btn.grid(row=row, column=col, padx=4, pady=4)
                self.buttons[btn_id] = btn

    def toggle_button(self, btn_id):
        if btn_id in self.buttons:
            btn = self.buttons[btn_id]
            current_color = btn.cget("bg")
            new_color = "red" if current_color != "red" else "black"
            self.window.after(0, lambda: btn.config(bg=new_color))

    def run(self):
        self.window.mainloop()