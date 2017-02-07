import os # the 'os' module provides functions to interact with the operating system
from shutil import *# the 'shutil' module provides a higher level interface for file management tasks and  directories that is too easier to use.
from data import Data # Import the class Data of file data.py
from operatorLines import OperatorLines # Import the class OperatorLines of file operatorLines.py
from handlingDirectories import HandlingDirectories # Import the class HandlingDirectories of file handlingDirectories.py
from mutate import Mutate # Import the class Mute of file mute.py

# the class Mutation is used to make a mutation on the files .java in the moment, in future it will be used to make mutation in programs
class Main():

    # method used to do the mutations on the file
    def mutate(self):
        num = 0
        src = unicode(Data.pathProject)
        dst = ""
        lines = OperatorLines().getOriginalLines()

        #selection structure used to validate the variable 'lines' got the lines to be mutated
        if lines != []:
        #repetition structure used to mutate the mutated projects where needed in accordance with the array 'lines', which has the determined positions (mutateLines) to be mutated
            for mutateLine in lines:
                num += 1
                dst = os.getcwd()+'/Mutants/Mutant-'+str(num)
                cloneDir = HandlingDirectories().cloneDir(src, dst)

                mutation = Mutate().mutate(dst, mutateLine)
            print('Success of mutation')
        else:
            print('Dont have any operator in the program')
