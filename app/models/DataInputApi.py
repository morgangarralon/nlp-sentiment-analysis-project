from app.models.DataInput import DataInput

class DataInputApi(DataInput):
    api = None

    def __init__(self, typ):
        print("DataInputAPI called w/ typ =", typ)

    def getData(self):
        return self.api.getData()

    