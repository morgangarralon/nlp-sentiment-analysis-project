from flask import json
import joblib
import inspect
import numpy as np
from app.models.DataInput import DataInput


class Guesser:
    type = None
    model = None
    
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
        
        return self.model.predict(data_input.getComputedDataset())[0]

    def getModel(self):
        return self.model

    def getSerializableSelf(self):
        self.getReadyForSerialization(self)
        
        return json.dumps(self.__dict__)

    def getReadyForSerialization(self, obj):
        list_attributes = [x for x in dir(obj) if not callable(getattr(obj, x))
                            and not x.startswith('__')
                            and not x.endswith('__')]

        for i, j in enumerate(list_attributes):
            attribute = obj.__getattribute__(list_attributes[i])
            class_attribute = attribute.__class__
            print(inspect.isclass(attribute))
            if isinstance(attribute, np.ndarray):
                attribute = attribute.tolist()
            elif isinstance(attribute, class_attribute):
                 obj.getReadyForSerialization(attribute)