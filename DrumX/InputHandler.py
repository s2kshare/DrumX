import threading
import time

class InputHandler:
    def __init__(self, engine, config):
        self.engine = engine
        self.config = config
        self.running = True

    def start_listening(self):
        threading.Thread(target=self._listen, daemon=True).start()

    def _listen(self):
        # self.engine.play_sound(0)
        pass
    
    def stop(self):
        self.running = False

