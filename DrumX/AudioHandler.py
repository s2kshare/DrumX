import pygame
import time
import threading

class AudioEngine:
    def __init__(self, bpm=120):
        pygame.mixer.init()
        self.bpm = bpm
        self.sounds = {
        }
        self.active_loops = {}
        self.beat_interval = 60 / self.bpm

    def load_sound(self, sound_id, filepath):
        sound = pygame.mixer.Sound(filepath)
        self.sounds[sound_id] = sound

    def play_sound(self, sound_id):
        if sound_id in self.sounds:
            self.sounds[sound_id].play()
        else:
            print(f"Sound '{sound_id}' not found")

    def play_loop(self, sound_id):
        if sound_id not in self.sounds:
            print(f"Sound '{sound_id}' not found")
            return

        stop_event = threading.Event()
        self.active_loops[sound_id] = stop_event

        def loop():
            while not stop_event.is_set():
                self.play_sound(sound_id)
                time.sleep(self.beat_interval)

        threading.Thread(target=loop, daemon=True).start()

    def stop_loop(self, sound_id):
        if sound_id in self.active_loops:
            self.active_loops[sound_id].set()
            del self.active_loops[sound_id]

    def set_bpm(self, bpm):
        self.bpm = bpm
        self.beat_interval = 60 / bpm
