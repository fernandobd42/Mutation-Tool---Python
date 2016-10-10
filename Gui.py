import sys # The sys module provides a number of functions and variables that can be used to manipulate different parts of the Python.
from PyQt4 import QtGui, QtCore # PyQt is a library used for developing cross platform of graphical user interface.
# The basic GUI widgets are located in the QtGui module.
# The QtCore module contains non-GUI functionality.

from Mutation01 import Mutation # Import the class Mutation of file Mutation01

# The class Gui use the QtGui.QMainWindow because is the QMainWindow class that provides the main application window.
class Gui(QtGui.QMainWindow):
    def __init__(self): # The __init__ method is the constructor of GUI application
        super(Gui, self).__init__() # The reserved word 'Super' is used to initialize the __init__ method
        self.setGeometry(400, 100, 500, 300) # the size of GUI
        self.setWindowTitle('Test of Mutation') # the title of GUI
        self.setWindowIcon(QtGui.QIcon('./aux/utf.ico')) # the icon of GUI

        # the exit method used on the statusBar of GUI
        exit = QtGui.QAction("&Quit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip('Leave')
        exit.triggered.connect(self.exit)

        # the open file method used on the statusBar of GUI
        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.open)

        self.statusBar()

        mainMenu = self.menuBar()

        exitMenu = mainMenu.addMenu('&Exit')
        exitMenu.addAction(exit)

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)

        self.home()

    # method used to add the button on the GUI that will invoke the method 'mutation'
    def home(self):
        btn = QtGui.QPushButton("Mutation", self)
        btn.clicked.connect(self.mutation)
        btn.resize(100,40)
        btn.move(200,100)
        self.show()

    # method used to add the button on the statusBar of the GUI that will be invoke the exit
    def exit(self):
        ask = QtGui.QMessageBox.question(self, 'Ask',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if ask == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    # method used to add the button on the statusBar of the GUI that will be get the path of file .java
    def open(self):
        m = Mutation()
        Mutation.originalJavaFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        if (m.originalJavaFile != ""):
            print(m.originalJavaFile)
        else:
            print('empty')

    # method used to invoke de method 'createNewDir' and 'mutate' to create a new dir and do the mutations
    def mutation(self):
        m = Mutation()
        m.createNewDir()
        m.mutate()

# method used to start the program with the GUI
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Gui()
    sys.exit(app.exec_())

# initializing the program invoking the method 'run'
run()
