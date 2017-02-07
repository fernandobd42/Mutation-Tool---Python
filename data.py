class Data():

    def __init__(self):
        self.pathProject = ""
        self.extension = ""
        self.operator1 = ""
        self.operator2 = ""

    # Methods to set and get values with security
        # Method to get the path of the program to be tested
    def getPathProject(self):
        return self.pathProject

    # Method to get the extension of files to be tested
    def getExtension(self):
        return self.extension

    # Method to get the original operator
    def getOperator1(self):
        return self.operator1

    # Method to get the wanted operator
    def getOperator2(self):
        return self.operator2
