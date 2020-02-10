from .DataInput import DataInput

class DataInputUser(DataInput):
    def __init__(self, type = None):
        self.type = type

    def getOneData(self):
        return None

    