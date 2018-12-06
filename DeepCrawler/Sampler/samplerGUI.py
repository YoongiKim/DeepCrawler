from tkinter import Button,messagebox
import tkinter as tk


query = ""
datanum = 0
platform = {
    "Naver_Blog":False,
    "Google":False
}

class SAMPLERGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("DeepCrawler (Training Set Sampler)")
        self.geometry("1000x600")
        self.resizable(False, False)

        # Menu Frame Configuration
        menuFrame = tk.Frame(self,height=2)
        menuFrame.pack(side="top",fill="both", expand=False)
        menuFrame.grid_rowconfigure(0, weight=1)
        menuFrame.grid_columnconfigure(0, weight=1)

        self.settingBtn = Button(menuFrame, text='Settings', highlightbackground="grey", highlightcolor="black", highlightthickness=2, command=lambda: self.show_frame(SettingFrame), width=50, height=2, padx=10, pady=5)
        self.settingBtn.pack(pady=5, padx=5, side='left', expand=True, fill="x")

        self.sampleBtn = Button(menuFrame, text='Sampler', command=lambda: self.show_frame(SampleFrame), width=50, height=2, padx=10, pady=5)
        self.sampleBtn.pack(pady=5, padx=5, side='left', expand=True, fill="x")

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
        if frame == SettingFrame:
            self.settingBtn.config(highlightbackground="grey", highlightcolor="black", highlightthickness=2)
            self.sampleBtn.config(highlightbackground="white", highlightcolor="white", highlightthickness=2)
        else:
            self.sampleBtn.config(highlightbackground="grey", highlightcolor="black", highlightthickness=2)
            self.settingBtn.config(highlightbackground="white", highlightcolor="white", highlightthickness=2)
        wanted_frame.tkraise()

class SettingFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        ## Setting Info Indicator Frame
        indicatorFrame = IndicatorFrame(self,controller)
        indicatorFrame.config(highlightbackground="black", highlightcolor="black", highlightthickness=2)
        indicatorFrame.pack(pady=5,padx=5, side="top",expand=False, fill="both")

        ## Setting Menu Selector Frame
        setterFrame = SetterFrame(self,controller,indicatorFrame)
        setterFrame.pack(pady=5,padx=5, side="top",expand=True, fill="both")

class IndicatorFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        # Query Info
        queryinfoLabel = tk.Label(self, text="Query : ", font="Helvetica 14 bold")
        queryinfoLabel.grid(padx=10, pady=(20, 5), row=0, column=0, sticky="nse")

        self.queryinfo = tk.Label(self, text="None", font="Helvetica 14")
        self.queryinfo.grid(padx=10, pady=(20, 5), row=0, column=1, sticky="nsw")

        # Data Number Info
        numinfoLabel = tk.Label(self, text="Wanted Data Number : ", font="Helvetica 14 bold")
        numinfoLabel.grid(padx=10, pady=5, row=1, column=0, sticky="nse")

        self.numinfo = tk.Label(self, text="0", font="Helvetica 14")
        self.numinfo.grid(padx=10, pady=5, row=1, column=1, sticky="nsw")

        # Platform Info
        platforminfoLabel = tk.Label(self, text="Platform : ", font="Helvetica 14 bold")
        platforminfoLabel.grid(padx=10, pady=(5,20), row=2, column=0, sticky="nse")

        self.platforminfo = tk.Label(self, text="None", font="Helvetica 14")
        self.platforminfo.grid(padx=10, pady=(5,20), row=2, column=1, sticky="nsw")

class SetterFrame(tk.Frame):
    def __init__(self,parent,controller,indicator):
        tk.Frame.__init__(self, parent)
        self.indicator = indicator

        ## Query Setting row
        # Query Label
        queryLabel = tk.Label(self, text="Enter Query", font='Helvetica 14')
        queryLabel.grid(padx=10, pady=(10, 5), row=3, column=0, sticky="nse")

        # Query Text Field
        self.queryField = tk.Entry(self, width=70)
        self.queryField.bind("<Return>", lambda event: self.setQuery())
        self.queryField.grid(padx=10, pady=(10, 5), row=3, column=1, sticky="nsew")

        # Query Button
        queryBtn = tk.Button(self, text="Set", width=12, command=self.setQuery)
        queryBtn.grid(padx=5, pady=(10, 5), row=3, column=2, sticky="nsw")

        ## Data number Setting row
        # Data Num Label
        numLabel = tk.Label(self, text="Enter wanted Data Number", font="Helvetica 14")
        numLabel.grid(padx=10, pady=5, row=4, column=0, sticky="nse")

        # Data Num Field
        self.numField = tk.Entry(self, width=70)
        self.numField.bind("<Return>", lambda event: self.setNum())
        self.numField.grid(padx=10, pady=5, row=4, column=1, sticky="nsew")

        # Data Num Button
        numBtn = tk.Button(self, text="Set", width=12, command=self.setNum)
        numBtn.grid(padx=5, pady=5, row=4, column=2, sticky="nsw")

        ## Platform Selection row
        # Platform Selection Label
        platformLabel = tk.Label(self, text="Select Platform", font="Helvetica 14")
        platformLabel.grid(padx=10, pady=5, row=5, column=0, sticky="nse")

    def setQuery(self):
        # Get Query from Text Field
        temp = self.queryField.get()
        self.queryField.delete(0, 'end')
        if temp == "":
            messagebox.showwarning("Query Warning","None Query is not allowed. Please Set a Valid Query")
        else:
            query = temp
            self.indicator.queryinfo.config(text=query)

    def setNum(self):
        # Get Number from Text Field
        temp = self.numField.get()
        self.numField.delete(0,'end')
        if temp.isdigit() and int(float(temp))>>0:
            datanum = int(float(temp))
            self.indicator.numinfo.config(text=datanum)
        else:
            messagebox.showwarning("Data Number Warning","Please Enter Integer bigger than 0")

class SampleFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Sampler")
        label.pack(pady=10, padx=10)
