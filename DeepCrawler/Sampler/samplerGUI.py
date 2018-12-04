from tkinter import Label,Button,Frame
import tkinter as tk

class SAMPLERGUI():
    def __init__(self, master):
        self.master = master
        master.title("Sampler (DeepCrawler)")
        master.resizable(0,0)

        # Initialize Frame
        self.menuFrame = Frame(self.master)
        self.menuFrame.pack(side='top')
        self.SetupFrame = Frame(self.master)
        self.SetupFrame.pack(side='bottom')
        self.SampleFrame = Frame(self.master)
        self.SampleFrame.pack(side='bottom')

        # Button Frame
        self.setup_button = Button(self.menuFrame, width=50,height=2,text="Setup", command=self.master.quit)
        self.setup_button.pack(side='left')
        self.sample_button = Button(self.menuFrame, width=50,height=2,text="Sample", command=self.master.quit)
        self.sample_button.pack(side='left')

        # Setup Frame
        # TODO Make Setup Frame and make crawler calling method


        # Sample Frame
        # TODO Make Sample Frame and make sampling and saving method