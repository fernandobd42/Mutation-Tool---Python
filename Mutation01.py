import os
import glob
import shutil
from os import makedirs

class Mutation():
    originalJavaFile = ""

    def createNewDir(self):
        if (os.path.exists('Files')):
            current_directory = os.path.dirname(os.path.abspath(__file__))
            shutil.rmtree(current_directory + '/Files/')
            makedirs("Files")
        else:
            makedirs("Files")

    def mutate(self):
        i = 0
        numFile = 0
        data = []

        if (self.originalJavaFile != ""):
            file = self.originalJavaFile
            fileJava = open(file, 'r')

            for line in fileJava:
                i+=1
                if(line.find('Hello world') > -1):
                    data.append(i)

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
            print('File doesn\'t exist')
