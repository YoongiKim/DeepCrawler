from tkinter import Label,Button,Frame
import tkinter as tk

class SAMPLERGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("DeepCrawler (Training Set Sampler)")
        self.geometry("1000x500")
        self.resizable(False, False)

        # Menu Frame Configuration
        menuFrame = tk.Frame(self,height=2)
        menuFrame.pack(side="top",fill="both", expand=False)
        menuFrame.grid_rowconfigure(0, weight=1)
        menuFrame.grid_columnconfigure(0, weight=1)

        settingBtn = Button(menuFrame, text='Settings', command=lambda: self.show_frame(SettingFrame), width=50, height=2, padx=10, pady=5)
        settingBtn.pack(pady=5, padx=5, side='left', expand=True, fill="x")

        sampleBtn = Button(menuFrame, text='Sampler', command=lambda: self.show_frame(SampleFrame), width=50, height=2, padx=10, pady=5)
        sampleBtn.pack(pady=5, padx=5, side='left', expand=True, fill="x")

        # Main Frame Configuration
        mainFrame = tk.Frame(self,highlightbackground="black", highlightcolor="black", highlightthickness=2)
        mainFrame.pack(side="top", fill="both", expand=True)
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)

        # List of subFrames of Main Frame
        self.frames = {}

        # Setup Settings Frame
        settingFrame = SettingFrame(mainFrame,self)
        self.frames[SettingFrame] = settingFrame
        settingFrame.grid(row=0, column=0, sticky="nsew")

        # Setup Sample Frame
        sampleFrame = SampleFrame(mainFrame, self)
        self.frames[SampleFrame] = sampleFrame
        sampleFrame.grid(row=0, column=0, sticky="nsew")

        # Show Settings Frame Initially
        self.show_frame(SettingFrame)

    def show_frame(self,frame):
        wanted_frame = self.frames[frame]
        wanted_frame.tkraise()

class SettingFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        ## Setting Info
        # Query Info
        queryinfoLabel = tk.Label(self, text="Query : ", font="Helvetica 14 bold")
        queryinfoLabel.grid(padx=10, pady=5, row=0, column=0, sticky="nsew")

        self.queryinfo = tk.Label(self, text="None", font="Helvetica 14")
        self.queryinfo.grid(padx=10, pady=5, row=0, column=1, sticky="nsw")

        # Data Number Info
        numinfoLabel = tk.Label(self, text="Wanted Data Number : ", font="Helvetica 14 bold")
        numinfoLabel.grid(padx=10, pady=5, row=1, column=0, sticky="nsew")

        self.numinfo = tk.Label(self, text="0", font="Helvetica 14")
        self.numinfo.grid(padx=10, pady=5, row=1, column=1, sticky="nsw")

        # Platform Info
        platforminfoLabel = tk.Label(self, text="Platform : ", font="Helvetica 14 bold")
        platforminfoLabel.grid(padx=10, pady=5, row=2, column=0, sticky="nsew")

        self.platforminfo = tk.Label(self, text="0", font="Helvetica 14")
        self.platforminfo.grid(padx=10, pady=5, row=2, column=1, sticky="nsw")


        ## Setting Menu
        # Query Label
        queryLabel = tk.Label(self, text="Enter Query", font='Helvetica 14')
        queryLabel.grid(padx=10, pady=10, row=3, column=0, sticky="nsew")

        # Query Text Field
        queryField = tk.Entry(self,width=60)
        queryField.grid(padx=10, pady=10, row=3, column=1, sticky="nsew")


class SampleFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Sampler")
        label.pack(pady=10, padx=10)
