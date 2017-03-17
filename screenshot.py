import pyscreenshot # the 'pyscreenshot' module can be used to copy the contents of the screen
import time # the 'time' module provides various time-related functions
import signal # the 'signal' module provides mechanisms to use signal handlers in Python
import os # the 'os' module provides functions to interact with the operating system

from data import Data # Import the class Data of file data.py
from compile import Compile # import the class Compile of file compile.py

# the class Screenshot is used to take screenshot of gui's
class Screenshot():

    # method used to take and save screenshots
    def screenshot(self, dstImage, nameImage):
        pathImage = dstImage + nameImage

        # grab screenshot and save image file
        pyscreenshot.grab(backend='scrot').save(pathImage + '.png')


    # method used to compile and execute java program's, then take and save thescreenshot after kill the program
    def getScreenshot(self, pathMutant, dstImage, nameImage):
        pathMainFile = pathMutant + '/JavaCAlculator22/src/'
        fileMain = os.path.basename(unicode(Data.pathMain))

        java = Compile().compile_execute_java(pathMainFile, fileMain)

        time.sleep(1)
        Screenshot().screenshot(dstImage, nameImage)

        os.kill(java, signal.SIGKILL)
