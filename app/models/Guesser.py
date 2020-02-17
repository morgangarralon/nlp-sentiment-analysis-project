import joblib
import numpy as np
from app.models.DataInput import DataInput


class Guesser:
    def __init__(self, type = None):
        self.type = type

    def loadGuesser(self, filename):
        self.model = joblib.load(filename)

    def getGuess(self, input):
        data_input = DataInput()
        data_input.loadFromTexte(input)
        data_input.cleanData()
        data_input.tokenizeData()
        data_input.addExtraFeatures()
        data_input.countvectorizeData(type(self.model).__name__ + '.cv')
        self.model.score(data_input.getComputedDataset(), ['neg'])
        return self.model.predict(data_input.getComputedDataset())

    def getModel(self):
        return self.model