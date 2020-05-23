import pylab
import pandas
import sys
import numpy


# Function converting .txt file with spaces to EKG .csv file
def convert_txt_to_csv(file_txt):

    header_list_ekg = "I,II,III,aVR,aVL,AVF,V3R,V1,V2,V4,V5,V6"

    with open(file_txt) as file:
        content = file.read()

    file_txt = file_txt.replace(".txt", "")
    content = content.replace(" ", ",")

    with open(file_txt + ".csv", "w") as file:
        file.write(header_list_ekg + "\n")
        file.write(content)


# Function printing EKG signal
def print_signal(file_csv, name, start, end, freq, fft):

    signal = pandas.read_csv(file_csv)
    line = []

    for index, row in signal.iterrows():
        line.append(row[name])

    # Cutting or not of Y axis
    if start == None and end == None:
        y = line
        pylab.title(signal.columns[signal.columns.get_loc(name)] + " (full signal)")
    else:
        y = line[start:end]
        pylab.title(signal.columns[signal.columns.get_loc(name)] + " (%dms - %dms)" %(start, end))


    x = list(range(0, len(y)))

    # Calibration of Y axis
    for i in x:
        x[i] = x[i] * 1/freq * 1000

    if fft == False:
        pylab.plot(x,y, 'r')
        pylab.grid(True)
        pylab.xlabel("Time [ms]")
        pylab.ylabel("Amplitude ")
        pylab.show()
    else:

        # Number of samplepoints
        N = len(x)
        # sample spacing
        T = 1.0 / freq

        x2 = numpy.linspace(0.0, N*T, N)
        yfft = numpy.fft.fft(y)
        yifft = numpy.fft.ifft(y)
        xf = numpy.linspace(0.0, 1.0/(2.0*T), N/2)


        pylab.subplot(311)
        pylab.grid(True)
        pylab.title("EKG signal")
        pylab.xlabel("Time [ms]")
        pylab.ylabel("Amplitude")
        pylab.plot(x,y,'r')

        pylab.subplot(312)
        pylab.grid(True)
        pylab.title("Transformata Fouriera")
        pylab.xlabel("Frequency [Hz]")
        pylab.ylabel("Amplitude")
        pylab.plot(xf, 2.0/N * numpy.abs(yfft[:N//2]))

        pylab.subplot(313)
        pylab.grid(True)
        pylab.title("Odwrotna transformata Fouriera")
        pylab.xlabel("Frequency [Hz]")
        pylab.ylabel("Amplitude")
        pylab.plot(xf, 2.0/N * numpy.abs(yifft[:N//2]))

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
    file_csv = None

    while True:
        print("\n----------------------------")
        print("SIGNAL READER")
        print("----------------------------")
        print("Loaded file:", file_csv)
        print("\nChoose option:")
        print("1. Convert .txt to .csv")
        print("2. Enter .csv file")
        print("3. Print EKG signal [I, II, III, aVR, aVL, AVF, V3R, V1, V2, V4, V5, V6]")
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
                    freq = int(input("Enter frequency: "))
                    print("Choose option:\n1. Full signal\n2. Cutted signal")
                    edit = int(input("=> "))
                    
                    if edit == 1:
                        print("Determine the fourier transform? (y/n)")
                        fft = input("=> ")
                        if fft == "y":
                            print_signal(file_csv, name, None, None, freq, True)
                        if fft == "n":
                            print_signal(file_csv, name, None, None, freq, False)

                    if edit == 2:
                        start = int(input("Start: "))
                        end = int(input("End: "))
                        print_signal(file_csv, name, start, end, freq)
                else:
                    print("Wrong signal name!")
                break
            
            if choice == 4:
                print_all_signals(file_csv)
                break

            if choice == 5:
                sys.exit()
                    

interface()
