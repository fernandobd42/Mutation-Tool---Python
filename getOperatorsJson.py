import json
from data import Data # Import the class Data of file data.py

class GetOperator():
    def getData(self):
        with open('operators.json') as data:
            operators = json.load(data)
        return operators
