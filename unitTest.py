import unittest
import os.path
from data import Data

class TestStringMethods(unittest.TestCase):
    def testJson(self):
        Data.pathJson = 'operators.json'
        assert Data.pathJson.endswith('json')

    def testPath(self):
        Data.pathProject = "/home/directory"
        assert Data.pathProject != ""

    def testMain(self):
        Data.pathMain = "/home/directory/file.java"
        assert os.path.basename(Data.pathMain).endswith('java')

if __name__ == '__main__':
    unittest.main()
