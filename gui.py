import sys # The sys module provides a number of functions and variables that can be used to manipulate different parts of the Python.
from PyQt4 import QtGui, QtCore # PyQt is a library used for developing cross platform of graphical user interface.
# The basic GUI widgets are located in the QtGui module.
# The QtCore module contains non-GUI functionality.

from data import Data # Import the class Data of file data.py
from main import Main # Import the class Mutation of file Mutation02.py
from handlingDirectories import HandlingDirectories


# The class Gui use the QtGui.QMainWindow because is the QMainWindow class that provides the main application window.
class Gui(QtGui.QMainWindow):

    def __init__(self): # The __init__ method is the constructor of GUI application
        super(Gui, self).__init__() # The reserved word 'Super' is used to initialize the __init__ method
        self.setGeometry(300, 100, 600, 350) # the size of GUI
        self.setWindowTitle('Test of Mutation') # the title of GUI
        self.setWindowIcon(QtGui.QIcon('./utf.ico')) # the icon of GUI

        # the exit method used on the statusBar of GUI
        exit = QtGui.QAction("&Quit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip('Leave')
        exit.triggered.connect(self.exit)

        # the open file method used on the statusBar of GUI
        openFolder = QtGui.QAction("&Open Folder", self)
        openFolder.setShortcut("Ctrl+O")
        openFolder.setStatusTip('Open Folder')
        openFolder.triggered.connect(self.open)

        mainMenu = self.menuBar()

        exitMenu = mainMenu.addMenu('&Exit')
        exitMenu.addAction(exit)

        fileMenu = mainMenu.addMenu('&Folder')
        fileMenu.addAction(openFolder)

        self.home()

    # method used to add the button on the GUI that will invoke the method 'mutation'
    def home(self):
        p = QtGui.QLabel("Path of Project", self)
        p.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        p.move(50,30)
        p.resize(200,20)
        Data.getPathProject = QtGui.QFileDialog.getExistingDirectory(None, 'Select a Folder:', 'home/fernando/', QtGui.QFileDialog.ShowDirsOnly)
        if (Data.getPathProject != ""):
            path = QtGui.QLabel(Data.getPathProject, self)
        else:
            path = QtGui.QLabel('Empty', self)
        path.move(50,50)
        path.resize(500,20)

        ext = QtGui.QLabel("Extension of File:", self)
        ext.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        ext.move(50,100)
        ext.resize(200,20)
        extt = Data.getExtension = QtGui.QLineEdit(self)
        extt.setPlaceholderText("Extension")
        extt.move(300,100)
        extt.resize(150,20)

        op1 = QtGui.QLabel("Mutation Operator:", self)
        op1.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        op1.move(50,150)
        op1.resize(200,20)
        opr1 = Data.getOperator1 = QtGui.QLineEdit(self)
        opr1.setPlaceholderText("Current Operator")
        opr1.move(300,150)
        opr1.resize(150,20)

        to = QtGui.QLabel("TO", self)
        to.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        to.move(360,175)
        to.resize(200,20)

        op2 = QtGui.QLabel("Mutation Operator:", self)
        op2.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        op2.move(50,200)
        op2.resize(200,20)
        opr2 = Data.getOperator2 = QtGui.QLineEdit(self)
        opr2.setPlaceholderText("Wanted Operator")
        opr2.move(300,200)
        opr2.resize(150,20)

        btn = QtGui.QPushButton("Mutation", self)
        btn.clicked.connect(self.mutation)

        btn.move(300,250)
        btn.resize(150,30)

        self.show()

    # method used to add the button on the statusBar of the GUI that will be invoke the exit
    def exit(self):
        ask = QtGui.QMessageBox.question(self, 'Ask', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if ask == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    # method used to add the button on the statusBar of the GUI that will be Data the path of file .java
    def open(self):
        Data.getPathProject = QtGui.QFileDialog.getExistingDirectory(None, 'Select a Folder:', '/home/fernando/', QtGui.QFileDialog.ShowDirsOnly)
        if (Data.getPathProject != ""):
            path = QtGui.QLabel(Data.getPathProject, self)
            print(Data.getPathProject)
        else:
            path = QtGui.QLabel('empty', self)
        path.move(50,50)
        path.resize(500,20)

    # method used to invoke de method 'createNewDir' and 'mutate' to create a new dir and do the mutations
    def mutation(self):
        d = Data()
        m = Main()
        hd = HandlingDirectories()
        if (d.getPathProject != ""):
            if (d.getExtension!= ""):
                if (d.getOperator1 != ""):
                    if (d.getOperator2 != ""):
                        hd.clearDir()
                        m.mutate()
                        feedback = QtGui.QMessageBox.information(self, 'Information', 'Congratulations, your mutation test was successful.')
        else:
            feedback = QtGui.QMessageBox.information(self, 'Information', 'Fill in all blanks before performing the mutation test')
        # m.createNewDir()
        # m.mutate()

# method used to start the program with the GUI
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Gui()
    sys.exit(app.exec_())

# initializing the program invoking the method 'run'
run()
