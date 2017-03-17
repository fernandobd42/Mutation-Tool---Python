import unittest
import os.path

class TestStringMethods(unittest.TestCase):
    def testJson(self):
        json = 'operators.json'
        assert json.endswith('json')

    def testPath(self):
        path = "/home/directory"
        assert path != ""

    def testMain(self):
        main = "/home/directory/file.java"
        assert os.path.basename(main).endswith('java')

if __name__ == '__main__':
    unittest.main()
