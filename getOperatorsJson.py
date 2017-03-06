import json # JSON stands for "JavaScript Object Notation", which is a lightweight format for computational data exchange
from data import Data # Import the class Data of file data.
import sys;

# the class GetOperator is used to get the data of json file
class GetOperator():
    # method used to get data of json file
    def getData(self):
        try:
            with open(Data.pathJson) as data:
                operators = json.load(data)
            return operators
        except ValueError:
            return None
