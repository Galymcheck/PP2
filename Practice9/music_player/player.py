import pygame

class MusicPlayer:
    def __init__(self, playlist):     
        self.playlist = playlist      #Saves the list of songs
        self.current = 0              #Starts at the first song
        self.is_playing = False       #Tracks if music is playing or not

        pygame.mixer.init()           #Turns on the music system

    def play(self):
        pygame.mixer.music.load(self.playlist[self.current])
        pygame.mixer.music.play()
        self.is_playing = True

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