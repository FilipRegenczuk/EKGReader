import tkinter as tk 

class Window(object):

    def __init__(self, window):
        self.window = window

        # window features
        window.title("EKG Reader")
        window.resizable(0, 0)
        window.geometry('300x200')

        buttonFile = tk.Button(window, text="Enter EKG file", width=15)
        buttonFile.grid(row=0, column=0)
        buttonPrintAll = tk.Button(window, text="Print all signals", width=15)
        buttonPrintAll.grid(row=1, column=0)
        buttonPrintOne = tk.Button(window, text="Print a signal", width=15)
        buttonPrintOne.grid(row=1, column=1)
        buttonInstruction = tk.Button(window, text="Instruction", width=15)
        buttonInstruction.grid(row=2, column=0)
        buttonQuit = tk.Button(window, text="Quit", width=15)
        buttonQuit.grid(row=2, column=1)



window = tk.Tk()
Window(window)
window.mainloop()