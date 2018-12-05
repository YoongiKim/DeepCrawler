from tkinter import Label,Button,Frame
import tkinter as tk

class SAMPLERGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Main Frame Configuration
        mainFrame = tk.Frame(self)
        mainFrame.pack(side="top", fill="both", expand=True)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        # List of Frames
        self.frames = {}

        # Setup Settings Frame
        settingFrame = SettingFrame(mainFrame,self)
        self.frames[SettingFrame] = settingFrame
        settingFrame.grid(row=0, column=0, sticky="nsew")

        # Show Settings Frame Initially
        self.show_frame(SettingFrame)

    def show_frame(self,frame):
        wanted_frame = self.frames[frame]
        wanted_frame.tkraise()

class SettingFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

class SampleFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)