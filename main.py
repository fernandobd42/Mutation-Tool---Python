import os # the 'os' module provides functions to interact with the operating system
from shutil import *# the 'shutil' module provides a higher level interface for file management tasks and  directories that is too easier to use.
from data import Data # Import the class Data of file data.py
from operatorLines import OperatorLines # Import the class OperatorLines of file operatorLines.py
from handlingDirectories import HandlingDirectories # Import the class HandlingDirectories of file handlingDirectories.py
from mutate import Mutate # Import the class Mute of file mute.py
from getOperators import GetOperator
import json

# the class Mutation is used to make a mutation on the files .java in the moment, in future it will be used to make mutation in programs
class Main():

    # method used to do the mutations on the file
    def mutate(self):
        num = 0
        src = unicode(Data.pathProject)
        dst = ""
        #selection structure used to validate the variable 'lines' got the lines to be mutated
        operators = GetOperator().getData()
        for op in operators['Operators']:
            op1 = op['op1']
            op2 = op['op2']
            ext = op['ext']
            lines = OperatorLines().getOperators(op1, ext)
            if lines != []:
                print len(lines), 'Operadores', op1
                #repetition structure used to mutate the mutated projects where needed in accordance with the array 'lines', which has the determined positions (mutateLines) to be mutated
                for mutateLine in lines:
                    num += 1
                    dst = os.getcwd()+'/Mutants/Mutant-'+str(num)
                    cloneDir = HandlingDirectories().cloneDir(src, dst)
                    mutation = Mutate().mutate(dst, mutateLine, op1, op2, ext, num)
            else:
                print 'Dont have the operator',op1 ,'in the program'
    print('Success of mutation')
