import os # the 'os' module provides functions to interact with the operating system
from data import Data # Import the class Data of file data.py

# the class Mute is used to do the mutation on the mutate programs
class Mute():

    # method used to do the mutation
    def mute(self, path, mutateLine):
        ext = Data.getExtension.text()
        op1 = Data.getOperator1.text()
        op2 = Data.getOperator2.text()
        i = 0
        #repetition structure used to swepper the directory 'path'
        for root, dirs, files in os.walk(path):
            #repetition structure used to get only 'file' on this directory
            for file in files:
                #selection structure used to get only files with determined extension 'ext'
                if file.endswith(ext):
                    fileMutate = os.path.join(root, file)
                    readFile = open(fileMutate, 'r+')
                    mutantFile = open(fileMutate, 'r+')
                    #repetition structure used to read each line of readFile
                    for line in readFile:
                        i += 1
                        #selection structure used to get only the line that have 'mutateLine' equal 'i'
                        if (mutateLine == i):
                            print 'MUTE: Change operator', op1, 'to', op2, 'in line', mutateLine
                            mutantFile.write(line.replace(op1, op2, 1))
                        else:
                            mutantFile.write(line)
                    mutantFile.close()
                    readFile.close()
