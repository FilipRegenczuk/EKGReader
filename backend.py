import pylab
import pandas
import sys
import os
from io import StringIO


class Backend(object):


    # Function checking if file is .txt or .csv
    def check_file(self, file):

        if os.path.splitext(file)[1] == ".csv":
            return True
        else:
            return False

    
    # Function converting .txt file with spaces to EKG .csv file
    def convert_txt_to_csv(self, file_txt):

        header_list_ekg = "I,II,III,aVR,aVL,AVF,V3R,V1,V2,V4,V5,V6"
        content = header_list_ekg + "\n"

        with open(file_txt) as file:
            content += file.read()

        content = content.replace(" ", ",")
        stringData = StringIO(content)
        file_csv = pandas.read_csv(stringData)
       
        return file_csv


    # Function printing EKG signal
    def print_signal(self, file_csv, name):

        signal = pandas.read_csv(file_csv)
        line = []

        for index, row in signal.iterrows():
            line.append(row[name])

        y = line
        x = range(0, len(y))

        pylab.plot(x,y, 'r')
        pylab.grid(True)
        pylab.title(signal.columns[signal.columns.get_loc(name)])
        pylab.show()


    # Function printing all EKG signals
    def print_all_signals(self, file):

        # Check if file is .txt
        if self.check_file(file) == False:
            signal = self.convert_txt_to_csv(file)      # Then convert to csv
        else:
            signal = pandas.read_csv(file)

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

            i += 1

            if pX < 5:
                pX += 1
            else:
                pX = 0
                pY += 1
            
        pylab.show()
