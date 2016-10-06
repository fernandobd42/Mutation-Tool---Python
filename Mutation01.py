import os

class Mutation():
    def mutate(self):
        i = 0
        data = []
        file = ('./aux/arquivo.java')

        os.system("rm -rf ./Arquivos")
        os.system("mkdir Arquivos")
        fileJava = open(file, 'r')
        for line in fileJava:
            data.append(line)

        for line in data:
            i += 1
            j = 0
            mutantJava = open('./Arquivos/arquivo'+str(i)+'.java', 'w')
            for line in data:
                if (i == j+1 and data[j].find('Hello world') != -1 ):
                    mutantJava.write(data[j].replace('Hello world', 'Hello Moon', 1))
                else:
                    mutantJava.write(data[j])
                j += 1
            mutantJava.close()
        fileJava.close()
