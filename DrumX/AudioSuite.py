import pygame
import time
import threading
from DrumX.utils import log

class AudioEngine:
    """
    The AudioEngine class is responsible for playing and managing audio.
    It will load sounds when they are requested, and play them when requested.
    """

    def __init__(self, bpm=120):
        """
        Initialize the AudioEngine with a specified beat per minute (BPM).
        """
        try:
            pygame.mixer.init()
        except pygame.error:
            log("System can't play audio", "red")
            quit()
        
        pygame.mixer.init()
        self.bpm = bpm
        self.sounds = {}  # Dictionary of btn_id -> pygame.mixer.Sound
        self.active_loops = {}  # Dictionary of btn_id -> threading.Event
        self.beat_interval = 60 / self.bpm

    def load_sound(self, btn_id, filepath):
        """
        Load a sound file and associate it with a btn_id.
        
        Parameters:
        btn_id (str): The identifier for the sound.
        filepath (str): The path to the sound file to be loaded.
        """
        sound = pygame.mixer.Sound(filepath)  # Load the sound from the given filepath
        self.sounds[btn_id] = sound  # Store the sound in the dictionary with its btn_id

    def play_sound(self, btn_id):
        """
        Play a sound once with the given btn_id.
        
        Parameters:
        btn_id (str): The identifier for the sound to be played.
        """
        if btn_id in self.sounds:
            self.sounds[btn_id].play()
        else:
            print(f"Sound '{btn_id}' not found")

    def set_profile(self):
        pass

    def set_loop(self, btn_id):
        """
        Play a sound on a loop with the given btn_id.
        
        Parameters:
        btn_id (str): The identifier for the sound to be looped.
        """
        if btn_id not in self.sounds:
            print(f"Sound '{btn_id}' not found")
            return

        if btn_id in self.active_loops:
            print(f"Sound '{btn_id}' is already playing on a loop")
            return

        stop_event = threading.Event()
        self.active_loops[btn_id] = stop_event

        def loop():
            """
            Loop until the stop event is set.
            
            This function will be run in a daemon thread.
            """
            # Loop until the stop event is set
            while not stop_event.is_set():
                # Get the sound object associated with the given btn_id
                sound = self.sounds[btn_id]
                # Play the sound
                sound.play()
                # Wait for the beat interval before playing the sound again
                time.sleep(self.beat_interval)

        # Start a daemon thread to run the loop
        threading.Thread(target=loop, daemon=True).start()

    def stop_loop(self, btn_id):
        """
        Stop a sound that is currently playing on a loop with the given btn_id.
        
        Parameters:
        btn_id (str): The identifier for the sound to be stopped.
        """
        if btn_id in self.active_loops:
            # Set the stop event to signal the loop to stop
            self.active_loops[btn_id].set()
            # Remove the stop event from the dictionary
            del self.active_loops[btn_id]

    def set_bpm(self, bpm):
        """
        Set the beat per minute (BPM) for the audio engine.
        
        This will change the interval between beats, which is used
        when playing sounds on a loop.
        
        Parameters:
        bpm (int): The new BPM.
        """
        self.bpm = bpm
        self.beat_interval = 60 / bpm

    def kill(self):
        """
        Close all threads and services.
        """
        for stop_event in self.active_loops.values():
            stop_event.set()
        self.active_loops.clear()
        pygame.mixer.quit()