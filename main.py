from DrumX.AudioHandler import AudioEngine

engine = AudioEngine(bpm=120)

engine.load_sound("0", "sounds/kick.wav")

while True:
    engine.play_sound("0")