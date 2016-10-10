import sys
from PyQt4 import QtGui, QtCore
from Mutation01 import Mutation

class Gui(QtGui.QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.setGeometry(400, 100, 500, 300)
        self.setWindowTitle('Test of Mutation')
        self.setWindowIcon(QtGui.QIcon('./aux/utf.ico'))

        exit = QtGui.QAction("&Quit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip('Leave')
        exit.triggered.connect(self.exit)

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

    def home(self):
        btn = QtGui.QPushButton("Mutation", self)
        btn.clicked.connect(self.mutation)
        btn.resize(100,40)
        btn.move(200,100)
        self.show()

    def exit(self):
        sys.exit()

    def open(self):
        m = Mutation()
        Mutation.originalJavaFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')

        if (m.originalJavaFile != ""):
            print(m.originalJavaFile)
        else:
            print('empty')

    def mutation(self):
        m = Mutation()
        m.createNewDir()
        m.mutate()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Gui()
    sys.exit(app.exec_())

run()
