import os # the 'os' module provides functions to interact with the operating system
import logging # the 'logging' module defines functions and classes which implement a flexible event logging system for applications and libraries.

# the class Log is used to create the log of program
class Log():
    # method used to print on the console and write on the 'MutateTool.log' the infos, errors and bugs relationed to program
    def log(self, output_dir):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # print on the console
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # write on 'MutateTool.log'
        handler = logging.FileHandler(os.path.join(output_dir, "MutateTool.log"),"w")
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
