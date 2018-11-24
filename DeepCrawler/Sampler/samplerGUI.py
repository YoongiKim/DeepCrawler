from tkinter import Label,Button

class SAMPLERGUI():
    def __init__(self, master):
        self.master = master
        master.title("Sampler (DeepCrawler)")
        master.geometry("1000x700")
        master.resizable(0,0)
        master.grid_columnconfigure(0, weight=1)

        self.setup_button = Button(master, width=50,height=2,text="Setup", command=master.quit)
        self.setup_button.grid(row=0,column=0, sticky='nw')
        self.sample_button = Button(master, width=50,height=2,text="Sample", command=master.quit)
        self.sample_button.grid(row=0,column=1, sticky='nw')

    def greet(self):
        print("Greetings!")