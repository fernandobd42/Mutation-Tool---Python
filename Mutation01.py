import os

class Mutation():
    def mutate(self):
        i = 0
        numFile = 0
        data = []
        file = ('./aux/arquivo.java')

        os.system('rm -rf ./Arquivos/*')
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
