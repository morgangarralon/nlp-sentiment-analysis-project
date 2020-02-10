from .DataInput import DataInput

class DataInputApi(DataInput):
    def __init__(self, type = None):
        self.type = type

    def getOneData(self):
        return None

    