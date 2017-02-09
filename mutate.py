import os # the 'os' module provides functions to interact with the operating system
from data import Data # Import the class Data of file data.py
from getOperators import GetOperator
from operatorLines import OperatorLines
from handlingDirectories import HandlingDirectories

# the class Mute is used to do the mutation on the mutate programs
class Mutate():
    def mutate(self):
        num = 0
        src = unicode(Data.pathProject)
        dst = ""
        operators = GetOperator().getData()
        for op in operators['Operators']:
            op1 = op['op1']
            op2 = op['op2']
            ext = op['ext']
            lines = OperatorLines().getOperators(op1, ext)
            #selection structure used to validate the variable 'lines' got the lines to be mutated
            if lines != []:
                print len(lines), 'Operadores', op1
                #repetition structure used to mutate the mutated projects where needed in accordance with the array 'lines', which has the determined positions (mutateLines) to be mutated
                for mutateLine in lines:
                    num += 1
                    dst = os.getcwd()+'/Mutants/Mutant-'+str(num)
                    cloneDir = HandlingDirectories().cloneDir(src, dst)
                    mutation = Mutate().replace(dst, mutateLine, op1, op2, ext, num)
            else:
                print 'Dont have the operator',op1 ,'in the program'
        print('Success of mutation')


    # method used to do the mutation
    def replace(self, path, mutateLine, op1, op2, ext, count):
        i = 0
        #repetition structure used to swepper the directory 'path'
        for root, dirs, files in os.walk(path):
            #repetition structure used to get only 'file' on this directory
            for file in files:
                #selection structure used to get only files with determined extension 'ext'
                if file.endswith(ext):
                    fileMutate = os.path.join(root, file)
                    readFile = open(fileMutate, 'r')
                    mutantFile = open(fileMutate, 'r+')
                    #repetition structure used to read each line of readFile
                    for line in readFile:
                        i += 1
                        #selection structure used to get only the line that have 'mutateLine' equal 'i'
                        if (mutateLine == i):
                            print count, 'MUTATE: Replace operator', op1, 'to', op2, 'in line', mutateLine
                            mutantFile.write(line.replace(op1, op2, 1))
                        else:
                            mutantFile.write(line)
                    mutantFile.close()
                    readFile.close()
