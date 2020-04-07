import tkinter as tk 
import os
from PIL import Image, ImageTk
from tkinter import filedialog, ttk
from backend import Backend

backend = Backend()


class Window(object):

    def __init__(self, window):
        self.window = window

        # Window features
        window.title("EKG Reader")
        window.resizable(0, 0)
        window.geometry('310x240')
        window.iconbitmap('images/icon.ico')

        # Front:
        load = Image.open('images/title.jpg')
        render = ImageTk.PhotoImage(load)
        labelTitle = tk.Label(window, image=render)
        labelTitle.image = render
        labelTitle.grid(row=0, column=0, columnspan=2)

        # Buttons:
        px = 20
        py = 5
        buttonFile = tk.Button(window, text="Enter EKG file", width=15, command=self.browseFiles)
        buttonFile.grid(row=1, column=0, padx=px, pady=py)
        buttonPrintAll = tk.Button(window, text="Print all signals", width=15, command=self.printSignals)
        buttonPrintAll.grid(row=2, column=0, padx=px, pady=py)
        buttonPrintOne = tk.Button(window, text="Print a signal", width=15, command=self.openSignalWindow)
        buttonPrintOne.grid(row=2, column=1, padx=px, pady=py)
        buttonInstruction = tk.Button(window, text="Instruction", width=15, command=self.openInstructionWindow)
        buttonInstruction.grid(row=3, column=0, padx=px, pady=py)
        buttonQuit = tk.Button(window, text="Quit", width=15, command=window.destroy)
        buttonQuit.grid(row=3, column=1, padx=px, pady=py)

        # Entry:
        self.file = tk.StringVar()
        self.entryFile = tk.Entry(window, textvariable=self.file, state='readonly', width=18)
        self.entryFile.grid(row=1, column=1, padx=px, pady=py)


    def browseFiles(self): 
        self.file = filedialog.askopenfilename(title = "Select a file", filetypes = (("Text or CSV files", "*.txt *.csv"), ))
        filename = os.path.basename(self.file)
        self.entryFile.configure(state='normal')
        self.entryFile.delete(0, tk.END)
        self.entryFile.insert(tk.END, filename)
        self.entryFile.configure(state='readonly')

    
    def printSignals(self):
        backend.print_all_signals(self.file)
       

    def openSignalWindow(self):
        windowSignal = tk.Tk()
        WindowSignal(windowSignal)
        windowSignal.mainloop()
    

    def openInstructionWindow(self):
        windowInstruction = tk.Tk()
        WindowInstruction(windowInstruction)
        windowInstruction.mainloop()


class WindowSignal(object):

    def __init__(self, window):
        self.widow = window

        # Window features
        window.title("Choose a signal")
        window.resizable(0, 0)
        window.geometry('300x50')
        window.iconbitmap('images/icon.ico')

        # Label:
        labelInfo = tk.Label(window, text="Choose a signal:")
        labelInfo.grid(row=0, column=0, padx=5, pady=12)

        # Combobox:
        signals = ["I", "II", "III", "aVR", "aVL", "AVF", "V3R", "V1", "V2", "V4", "V5", "V6"]
        comboSignals = ttk.Combobox(window, values=signals, state="readonly", width=5)
        comboSignals.grid(row=0, column=1, padx=5, pady=12)

        # Button:
        buttonOK = tk.Button(window, text="OK", width=15)
        buttonOK.grid(row=0, column=2, padx=5, pady=12)



class WindowInstruction(object):

    def __init__(self, window):
        self.window = window

        instruction = """
        EKG Reader application is used to print EKG 
        signals. User can enter .txt or .csv files 
        of EKG signals, which he/she wants to print.

        Steps: 
        1. Enter EKG file.
        2. Print all signals or selected.
        3. Analyze EKG signal(s) on graph(s)
        """

        # Window features
        window.title("Instruction")
        window.resizable(0, 0)
        window.geometry('310x240')
        window.iconbitmap('images/icon.ico')

        # Labels:
        labelTitle = tk.Label(window, text="Instruction:", font='bold', fg='#ae0000')
        labelTitle.pack()
        labelInstruction = tk.Label(window, text=instruction, anchor='w', justify='left', width=300)
        labelInstruction.pack()

        # Button:
        buttonOK = tk.Button(window, text="OK", width=15, command=window.destroy)
        buttonOK.pack(pady=10)


window = tk.Tk()
Window(window)
window.mainloop()