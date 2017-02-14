import os # the 'os' module provides functions to interact with the operating system
from data import Data # Import the class Data of file data.py
from getOperatorsJson import GetOperator # Import the class GetOperator of file getOperatorsJson.py
from operatorLines import OperatorLines # Import the class OperatorLines of file operatorLines.py
from handlingDirectories import HandlingDirectories # Import the class HandlingDirectories of file handlingDirectories.py

# the class Mutate is used to do the mutation on the mutated programs
class Mutate():
    # method used to do the mutation
    def mutate(self):
        count = 0
        src = unicode(Data.pathProject)
        dst = ""
        operators = GetOperator().getData()
        #repetition structure used to get the operators in order of the json
        for op in operators['Operators']:
            num = 0
            op1 = op['op1']
            op2 = op['op2']
            ext = op['ext']
            lines = OperatorLines().getOperators(op1, ext)
            #selection structure used to validate the variable 'lines' got the lines to be mutated
            if lines != []:
                print len(lines), 'lines have the operator', op1
                #repetition structure used to mutate the mutated projects where needed in accordance with the array 'lines', which has the determined positions (mutateLines) to be mutated
                for mutateLine in lines:
                    num += 1
                    count += 1
                    dst = os.getcwd()+'/Mutants/'+str(count)+'-Mutant-'+str(op1)+'-'+str(num)
                    cloneDir = HandlingDirectories().cloneDir(src, dst)
                    mutation = Mutate().replace(dst, mutateLine, op1, op2, ext, count)
            else:
                print 'Dont have the operator',op1 ,'in the program'
        print('Success of mutation')


    # method used to replace operators
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
                            print count, 'MUTATE: Replace operator', op1, 'to', op2
                            mutantFile.write(line.replace(op1, op2, 1))
                        else:
                            mutantFile.write(line)
                    mutantFile.close()
                    readFile.close()
