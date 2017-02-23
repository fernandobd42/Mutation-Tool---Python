import os # the 'os' module provides functions to interact with the operating system
import re # the 're' module provides functions to interact with regular expression operations
from data import Data # Import the class Data of file data.py

# the class OperatorLines is used to get the operators and lines of the original program
class OperatorLines():

    # method used to get the current operators lines
    def getOperators(self, op1, ext):
        i = 0
        operatorsLines = []
        #selection structure used to validate if the Data.pathProject is different of 'empty'
        if (Data.pathProject != ""):
            path = str(Data.pathProject)
            #repetition structure used to read all files of the project
            for root, dirs, files in os.walk(path):
                for file in files:
                    #selection structure used to get just files with determined ext
                    if file.endswith(ext):
                        fileMutate = os.path.join(root, file)
                        readFile = open(fileMutate, 'r')
                        # mutantFile = open(fileMutate, 'r+')
                        #repetion structure used to read each file with determined extension
                        for line in readFile:
                            i+=1
                            # mutantFile.write(re.sub(' +',' ',line))
                            #selection structure used to get the lines have the current operator
                            if(line.find(op1) > -1):
                                operatorsLines.append(i)
                        # mutantFile.close()
                        readFile.close()
            return operatorsLines
