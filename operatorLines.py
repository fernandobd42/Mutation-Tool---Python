import os # the 'os' module provides functions to interact with the operating system
from data import Data # Import the class Data of file data.py
from getOperators import GetOperator
import json

# the class OperatorLines is used to get the operators and lines of the original program
class OperatorLines():

    # method used to get the current operators lines
    def getOperators(self, op1, ext):
        i = 0
        operatorsLines = []
        if (Data.pathProject != ""):
            path = str(Data.pathProject)
            #repetition structure used to read all files of the project
            for root, dirs, files in os.walk(path):
                for file in files:
                    #selection structure used to get just files with determined ext
                    if file.endswith(ext):
                        fileMutate = os.path.join(root, file)
                        readFile = open(fileMutate, 'r')
                        #repetion structure used to read each file with determined extension
                        for line in readFile:
                            i+=1
                            #selection structure used to get the lines have the current operator
                            if(line.find(op1) > -1):
                                operatorsLines.append(i)
            return operatorsLines
        else:
            #if the path don't selected, the program return this
            print('Path doesn\'t exist')
