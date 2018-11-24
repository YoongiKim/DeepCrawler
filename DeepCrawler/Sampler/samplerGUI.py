from tkinter import Label,Button,Frame
import tkinter as tk

class SAMPLERGUI():
    def __init__(self, master):
        self.master = master
        master.title("Sampler (DeepCrawler)")
        master.geometry("1000x700")
        master.resizable(0,0)

        # Initialize Frame
        buttonFrame = Frame(self.master).pack(side='top')
        SetupFrame = Frame(self.master).pack(side='bottom')
        SampleFrame = Frame(self.master).pack(side='bottom')

        # Button Frame
        self.setup_button = Button(buttonFrame, width=50,height=2,text="Setup", command=master.quit)
        self.setup_button.pack(side = 'left')
        self.sample_button = Button(buttonFrame, width=50,height=2,text="Sample", command=master.quit)
        self.sample_button.pack(side = 'right')

        # Setup Frame
        

        # Sample Frame