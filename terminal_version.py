import pylab
import pandas
import sys


# Function converting .txt file with spaces to EKG .csv file
def convert_txt_to_csv(file_txt):

    header_list_ekg = "I,II,III,aVR,aVL,AVF,V3R,V1,V2,V4,V5,V6"

    with open(file_txt) as file:
        content = file.read()

    content = content.replace(" ", ",")

    with open(file_txt + ".csv", "w") as file:
        file.write(header_list_ekg + "\n")
        file.write(content)


# Function printing EKG signal
def print_signal(file_csv, name, start, end):

    signal = pandas.read_csv(file_csv)
    line = []

    for index, row in signal.iterrows():
        line.append(row[name])

    if start == None and end == None:
        y = line
        pylab.title(signal.columns[signal.columns.get_loc(name)] + " (full signal)")
    else:
        y = line[start:end]
        pylab.title(signal.columns[signal.columns.get_loc(name)] + " (%dms - %dms)" %(start, end))

    x = range(0, len(y))

    pylab.plot(x,y, 'r')
    pylab.grid(True)
    pylab.xlabel("Time [ms]")
    pylab.ylabel("Amplitude ")
    pylab.show()


# Function printing all EKG signals
def print_all_signals(file_csv):

    signal = pandas.read_csv(file_csv)
    i = 0
    pX = 0
    pY = 0

    while i <= 11:
        
        line = []
        for index, row in signal.iterrows():
            line.append(row[i])

        y = line
        x = range(0, len(y))

        pylab.subplot2grid((6,2), (pX,pY))
        pylab.plot(x,y, 'r')
        pylab.grid(True)
        pylab.title(signal.columns[i])
        pylab.xlabel("Time [ms]")
        pylab.ylabel("Amplitude ")

        i += 1

        if pX < 5:
            pX += 1
        else:
            pX = 0
            pY += 1
        
    pylab.show()


# Termianl interface
def interface():
    file_csv = ""

    while True:
        print("\n----------------------------")
        print("SIGNAL READER")
        print("----------------------------")
        print("Loaded file:", file_csv)
        print("\nChoose option:")
        print("1. Convert .txt to .csv")
        print("2. Enter .csv file")
        print("3. Choose EKG signal [I, II, III, aVR, aVL, AVF, V3R, V1, V2, V4, V5, V6]")
        print("4. Print  all EKG signals")
        print("5. Quit\n")

        while True:
            try:
                choice = int(input("=> "))
                break
            except ValueError:
                print("Valid option!")
    

        while True:
            if choice == 1:
                file_txt = input("Enter .txt file: ")

                if file_txt.endswith(".txt"):
                    convert_txt_to_csv(file_txt)
                else:
                    print("File must be .txt type!")
                break
                           
            if choice == 2:
                file_csv = input("Enter .csv file: ")
                break

            if choice == 3:
                name = input("Enter signal name: ")

                if name in ["I", "II", "III", "aVR", "aVL", "AVF", "V3R", "V1", "V2", "V4", "V5", "V6"]:
                    print("Choose option:\n1. Full signal\n2. Cutted signal")
                    edit = int(input("=> "))
                    
                    if edit == 1:
                        print_signal(file_csv, name, None, None)
                    if edit == 2:
                        start = int(input("Start: "))
                        end = int(input("End: "))
                        print_signal(file_csv, name, start, end)
                else:
                    print("Wrong signal name!")
                break
            
            if choice == 4:
                print_all_signals(file_csv)
                break

            if choice == 5:
                sys.exit()
                    

interface()
