import pygame
from mutagen.wave import WAVE

class MusicPlayer:
    def __init__(self, playlist):     
        self.playlist = playlist      #Saves the list of songs
        self.current = 0              #Starts at the first song
        self.is_playing = False       #Tracks if music is playing or not
        self.track_length = 1 
        pygame.mixer.init()           #Turns on the music system

    def play(self):
        path = self.playlist[self.current]

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        self.is_playing = True

        audio = WAVE(path)
        self.track_length = audio.info.length

    def get_progress(self):
        if not self.is_playing:
             return 0

        pos = pygame.mixer.music.get_pos() / 1000

        if self.track_length == 0:
         return 0

        return pos / self.track_length


    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current = (self.current + 1) % len(self.playlist)  #% makes it loop back to start
        self.play()

    def prev_track(self):
        self.current = (self.current - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        return self.playlist[self.current]