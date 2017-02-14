#!/usr/bin/python
import os # the 'os' module provides functions to interact with the operating system
import sys # The sys module provides a number of functions and variables that can be used to manipulate different parts of the Python.
from PyQt4 import QtGui, QtCore # PyQt is a library used for developing cross platform of graphical user interface.
# The basic GUI widgets are located in the QtGui module.
# The QtCore module contains non-GUI functionality.

from data import Data # Import the class Data of file data.py
from main import Main # Import the class Mutation of file Mutation02.py
from handlingDirectories import HandlingDirectories # Import the class HandlingDirectories of file handlingDirectories.py


# The class Gui use the QtGui.QMainWindow because is the QMainWindow class that provides the main application window.
class Gui(QtGui.QMainWindow):
    d = os.getcwd()

    def __init__(self): # The __init__ method is the constructor of GUI application
        super(Gui, self).__init__() # The reserved word 'Super' is used to initialize the __init__ method
        self.resize(800,300) # the size of GUI
        self.setWindowIcon(QtGui.QIcon('./utf.ico')) # the icon of GUI
        self.setWindowTitle('Test of Mutation') # the title of GUI
        self.setFixedSize(self.size()) # the size of GUI that's fixed
        self.center() # the GUI centered on the window

        # the exit method used on the statusBar of GUI
        exit = QtGui.QAction("&Quit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip('Leave')
        exit.triggered.connect(self.exit)

        # the openFolder method used on the statusBar of GUI
        openFolder = QtGui.QAction("&Open Folder", self)
        openFolder.setShortcut("Ctrl+O")
        openFolder.setStatusTip('Open Folder')
        openFolder.triggered.connect(self.openFolder)

        # the openJson method used on the statusBar of GUI
        openJson = QtGui.QAction("&Open Json", self)
        openJson.setShortcut("Ctrl+P")
        openJson.setStatusTip('Open Json')
        openJson.triggered.connect(self.openJson)

        mainMenu = self.menuBar()

        exitMenu = mainMenu.addMenu('&Exit')
        exitMenu.addAction(exit)

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFolder)
        fileMenu.addAction(openJson)

        self.home()

    # method used to add the button on the GUI that will invoke the method 'mutation'
    def home(self):
        p = QtGui.QLabel("Path of Project:", self)
        p.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        p.move(30,30)
        p.resize(150,20)
        self.openFolder()

        j = QtGui.QLabel("Path of Json:", self)
        j.setFont(QtGui.QFont("Times", 12, weight=QtGui.QFont.Bold))
        j.move(30,75)
        j.resize(150,20)
        self.openJson()

        btn = QtGui.QPushButton("Mutation", self)
        btn.clicked.connect(self.mutation)
        btn.move(250, 150)
        btn.resize(300,100)

        self.statusBar()
        self.show()

    # method used to centralize the gui on the monitor
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # method used to exit of program
    def exit(self):
        ask = QtGui.QMessageBox.question(self, 'Ask', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if ask == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    # method used to get the path of the project
    def openFolder(self):
        Data.pathProject = QtGui.QFileDialog.getExistingDirectory(None, 'Select the Directory of Original Program:', self.d, QtGui.QFileDialog.ShowDirsOnly)
        if (Data.pathProject != ""):
            path = QtGui.QLabel(Data.pathProject, self)
        else:
            path = QtGui.QLabel('Empty', self)
        path.move(150,25)
        path.resize(500,30)
        print path.text()
        return path.text()

    # method used to get the path of the json file
    def openJson(self):
        Data.pathJson = QtGui.QFileDialog.getOpenFileName(self, 'Select the Json File that has the Operators')
        if (Data.pathJson != ""):
            json = QtGui.QLabel(Data.pathJson, self)
        else:
            json = QtGui.QLabel('Empty', self)
        json.move(150,70)
        json.resize(500,30)
        print json.text()
        return json.text()

    # method used to invoke de method 'createNewDir' and 'mutate' to create a new dir and do the mutations
    def mutation(self):
        d = Data()
        m = Main()
        hd = HandlingDirectories()
        if (d.pathProject != "" and d.pathJson != ""):
            hd.clearDir()
            m.mutate()
            feedback = QtGui.QMessageBox.information(self, 'Information', 'Congratulations, your mutation test was successful.')
        else:
            feedback = QtGui.QMessageBox.critical(self, 'Information', 'Fill in all blanks before performing the mutation test')

# method used to start the program with the GUI
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Gui()
    GUI.show()
    sys.exit(app.exec_())

# initializing the program invoking the method 'run'
run()
