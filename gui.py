import tkinter as tk 
from PIL import Image, ImageTk

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
        buttonFile = tk.Button(window, text="Enter EKG file", width=15)
        buttonFile.grid(row=1, column=0, padx=px, pady=py)
        buttonPrintAll = tk.Button(window, text="Print all signals", width=15)
        buttonPrintAll.grid(row=2, column=0, padx=px, pady=py)
        buttonPrintOne = tk.Button(window, text="Print a signal", width=15)
        buttonPrintOne.grid(row=2, column=1, padx=px, pady=py)
        buttonInstruction = tk.Button(window, text="Instruction", width=15, command=self.openInstructionWindow)
        buttonInstruction.grid(row=3, column=0, padx=px, pady=py)
        buttonQuit = tk.Button(window, text="Quit", width=15, command=window.destroy)
        buttonQuit.grid(row=3, column=1, padx=px, pady=py)

        # Entry:
        entryFile = tk.Entry(window, width=18)
        entryFile.grid(row=1, column=1, padx=px, pady=py)

    
    def openInstructionWindow(self):
        windowInstruction = tk.Tk()
        WindowInstruction(windowInstruction)
        windowInstruction.mainloop()



class WindowInstruction(object):

    def __init__(self, window):
        self.window = window

        instruction = """
        EKG Reader application is used to print EKG signals.
        User can enter .txt or .csv files of EKG signals,
        which he/she wants to print.

        Steps: 
        1. Enter EKG file.
        2. Print all signals or selected.
        3. Analyze EKG signal(s) on graph(s)
        """

        # Window features
        window.title("EKG Reader: Instruction")
        window.resizable(0, 0)
        window.geometry('310x240')
        window.iconbitmap('images/icon.ico')

        # Labels:
        labelTitle = tk.Label(window, text="Instruction:", font='bold', justify='left')
        labelTitle.pack()
        labelInstruction = tk.Label(window, text=instruction)
        labelInstruction.pack()



window = tk.Tk()
Window(window)
window.mainloop()