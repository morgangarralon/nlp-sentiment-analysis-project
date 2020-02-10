from .DataInputApi import DataInputApi

class DataInputTwitter(DataInputApi):
    def __init__(self, type = None):
        self.type = type

    def getOneData(self):
        return None

    