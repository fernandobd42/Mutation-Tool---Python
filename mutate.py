import os # the 'os' module provides functions to interact with the operating system
import sys # The 'sys' module provides a number of functions and variables that can be used to manipulate different parts of the Python.

from data import Data # Import the class Data of file data.py
from getOperatorsJson import GetOperator # Import the class GetOperator of file getOperatorsJson.py
from operatorLines import OperatorLines # Import the class OperatorLines of file operatorLines.py
from handlingDirectories import HandlingDirectories # Import the class HandlingDirectories of file handlingDirectories.py
from log import * # import all of the file log.py
from screenshot import Screenshot # import the class Screenshot of file screenshot.py
from compare import Compare

# the class Mutate is used to do the mutation on the mutated programs
class Mutate():
    # instantiating the method log of the class Log
    Log().log(os.getcwd())

    # method used to do the mutation
    def mutate(self):
        pathOrigin = os.getcwd()
        dstImages = pathOrigin + '/Images/'
        count = 0
        src = unicode(Data.pathProject)
        dst = ""
        result = ""
        #geting the data of json
        operators = GetOperator().getData()
        #repetition structure used to read each one operator of the json
        for op in operators['Operators']:
            num = 0
            name = op['name'].encode('utf-8')
            op1 = op['op1'].encode('utf-8')
            op2 = op['op2'].encode('utf-8')
            ext = 'java'
            lines = OperatorLines().getOperators(op1, ext)
            #selection structure used to validate the variable 'lines' got the lines to be mutated
            if lines != []:
                logging.info("'%s' lines have the operator '%s'" % (len(lines), op1))
                print("'%s' lines have the operator '%s'" % (len(lines), op1))

                #repetition structure used to mutate the mutated projects where needed in accordance with the array 'lines', which has the determined positions (mutateLines) to be mutated
                for mutateLine in lines:
                    num += 1
                    count += 1
                    nameImage = 'imagem'+str(count)
                    pathMutant = pathOrigin +'/Mutants/'+str(count)+'-Mutant-'+name
                    HandlingDirectories().cloneDir(src, pathMutant)
                    Mutate().replace(pathMutant, ext, mutateLine, count, op1, op2)
                    Screenshot().getScreenshot(pathMutant, dstImages, nameImage)
                    image = dstImages + nameImage + '.png'
                    self.result = Compare().compare(image)

            else:
                logging.error("No one of the operators past by the json was found in the original program")
                print("No one of the operators past by the json was found in the original program")

        logging.info(self.result)
        print(self.result)


    # method used to replace operators
    def replace(self, pathMutant, ext, mutateLine, count, op1, op2):
        i = 0
        #repetition structure used to swepper the directory 'path'
        for root, dirs, files in os.walk(pathMutant):
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
                            logging.info("'%s' MUTATE: Replace operator '%s' to '%s'" %(count, op1, op2))
                            print("'%s' MUTATE: Replace operator '%s' to '%s'" %(count, op1, op2))
                            mutantFile.write(line.replace(op1, op2, 1))
                        else:
                            mutantFile.write(line)
                    mutantFile.close()
                    readFile.close()
