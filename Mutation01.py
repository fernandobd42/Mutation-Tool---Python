import os
import glob
import shutil
from os import makedirs

class Mutation():

    def createNewDir(self):
        if (os.path.exists('Arquivos')):
            current_directory = os.path.dirname(os.path.abspath(__file__))
            shutil.rmtree(current_directory + '/Arquivos/')
            makedirs("Arquivos")
        else:
            makedirs("Arquivos")

    def mutate(self):
        i = 0
        numFile = 0
        data = []
        file = ('./aux/arquivo.java')

        fileJava = open(file, 'r')
        for line in fileJava:
            i+=1
            if(line.find('Hello world') > -1):
                data.append(i)

        for mutationPosition in data:
            numFile += 1
            print('arquivo',numFile)
            i = 0
            fileJava = open(file, 'r')
            mutantFile = open('./Arquivos/arquivo'+str(numFile)+'.java', 'w')
            for line in fileJava:
                i += 1
                if (mutationPosition == i):
                    mutantFile.write(line.replace('Hello world', 'Hello Moon', 1))
                else:
                    mutantFile.write(line)
            mutantFile.close()
        fileJava.close()
