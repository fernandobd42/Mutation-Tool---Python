import subprocess # the 'subprocess' module allows you to spawn new processes
import os # the 'os' module provides functions to interact with the operating system
import sys # the 'sys' module provides a number of functions and variables that can be used to manipulate different parts of the Python.
import signal # the 'signal' module provides mechanisms to use signal handlers in Python
import os.path # the module implements some useful functions on pathnames

# the class Compile is used to compile and execute java program's
class Compile():

    # method used to compile and execute java program's
    def compile_execute_java(self, pathMain, fileMain):
        os.chdir(pathMain)

        cmdJavac = 'javac ' + fileMain
        javac = subprocess.call(cmdJavac, shell=True)

        cmdJava = 'java ' + os.path.splitext(fileMain)[0]
        java = subprocess.Popen("exec " + cmdJava, signal.SIGTERM, shell=True)

        pid = java.pid
        return pid
