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
        self.window.geometry('400x600')
        self.window.title("DrumX Simple GUI")

        self.buttons = {}  # Dictionary for quick lookup by ID

        # Header
        frame_header = Frame(self.window, pady=10)
        frame_header.pack(side=TOP)
        Label(frame_header, text="DrumX Simple GUI", font=("Courier", 18)).pack()
        Label(frame_header, text="Inteded for testing purposes").pack()

        # Switches Frame
        frame_switches = Frame(self.window, pady=10)
        frame_switches.pack(side=TOP)

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