# from tkinter import *
from tkinter import ttk 
from tkinter import *
# from tkinter.ttk import *
from tkinter import filedialog
from pygame import mixer


class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('mp3 player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=10,y=20);Play.place(x=120,y=20);Pause.place(x=230,y=20);Stop.place(x=120,y=60)
        self.music_file = False
        self.playing_state = False
        self.paused_state = False
        self.stopped_state = False

    def load(self):
        mixer.init()  # Initialzing pyamge mixer
        self.music_file = filedialog.askopenfilename()
        mixer.music.load(self.music_file)re

    def play(self):
        if self.music_file:
            # mixer.init()        # Initialzing pyamge mixer
            # mixer.music.load(self.music_file)
            if not self.playing_state and not self.paused_state:
                mixer.music.play()  # Playing Music with Pygame
            elif not self.playing_state and self.paused_state:
                mixer.music.unpause()
            self.playing_state = True
            self.paused_state = False

    def pause(self):
        if self.playing_state:
            mixer.music.pause()
            self.playing_state = False
            self.paused_state = True

    def stop(self):
        if self.playing_state:
            mixer.music.stop()
            self.playing_state = False


root = Tk()
app = MusicPlayer(root)
root.mainloop()
