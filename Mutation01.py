import os # the 'os' module provides functions to interact with the operating system
import shutil # the 'shutil' module provides a higher level interface for file management tasks and  directories that is too easier to use.
from os import makedirs # the 'makedirs' is a recursive directory creation function

# the class Mutation is used to make a mutation on the files .java in the moment, in future it will be used to make mutation in programs
class Mutation():
    originalJavaFile = "" # variable used to get the path of file .java

    # method used to create a new directory where the mutated files will be saved
    def createNewDir(self):
        if (os.path.exists('Files')):
            current_directory = os.path.dirname(os.path.abspath(__file__))
            shutil.rmtree(current_directory + '/Files/')
            makedirs("Files")
        else:
            makedirs("Files")

    # method used to do the mutations on the file .java
    def mutate(self):
        i = 0
        numFile = 0
        data = []

        # selection structure used to validate the variable 'originalJavaFile' got the path of the file .java
        if (self.originalJavaFile != ""):
            file = self.originalJavaFile
            fileJava = open(file, 'r')

            # repetition structure used to get the lines who'll be mutated, and inserting them in the array
            for line in fileJava:
                i+=1
                if(line.find('Hello world') > -1):
                    data.append(i)

            # repetition structure used to create the mutated files where needed in accordance with the array 'data', which has the positions to be mutated
            for mutationPosition in data:
                numFile += 1
                print('Mutant',numFile)
                i = 0
                fileJava = open(file, 'r')
                mutantFile = open('./Files/Mutant'+str(numFile)+'.java', 'w')
                for line in fileJava:
                    i += 1
                    if (mutationPosition == i):
                        mutantFile.write(line.replace('Hello world', 'Hello Moon', 1))
                    else:
                        mutantFile.write(line)
                mutantFile.close()
            fileJava.close()
            print('Success of mutation')
        else:
            # if the file isn't selected, the program return this
            print('File doesn\'t exist')
