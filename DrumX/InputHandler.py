import threading
import time

class InputHandler:
    def __init__(self, engine, controller):
        self.engine = engine
        self.controller = controller
        self.running = True

    def start_listening(self):
        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self):
        pass
    
    def stop(self):
        self.running = False

