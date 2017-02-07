import os # the 'os' module provides functions to interact with the operating system
import shutil # the 'shutil' module provides a higher level interface for file management tasks and  directories that is too easier to use.

# the class HandlingDirectories is used to handler directories
class HandlingDirectories():

    # method used to create the directory where the mutate programs will be saved
    def clearDir(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        if (os.path.exists('Mutants')):
            shutil.rmtree(current_directory + '/Mutants')
            os.makedirs('Mutants')
        else:
            os.makedirs('Mutants')

    # method used to clone original directory program to the mutate directory
    def cloneDir(self, src, dest):
            shutil.copytree(src, dest)
