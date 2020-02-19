import joblib
import inspect
import builtins
import jsonpickle
import numpy as np
from flask import json
from json import JSONEncoder
from app.models.DataInput import DataInput

def get_builtins():
    return tuple(filter(lambda x: not x.startswith('_'), dir(builtins)))

class Guesser():
    type = None
    model = None
    tolisted_attributes = []

    def __init__(self, type = None):
        self.type = type
    
    def to_json(self) :
        return jsonpickle.encode(self)

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
        NoneType = type(None)
        primitive_type_names = (int, str, float, bool, type, object, NoneType)
        builtin_type_names = tuple(filter(lambda x: not x.startswith('_'), dir(builtins)))
    
        self.getReadyForSerialization([self], self, (primitive_type_names + builtin_type_names))
        
        return jsonpickle.encode(self)

    def getReadyForSerialization(self, obj, mother_obj, primitive_types):
        list_attributes = [x for x in dir(obj[0]) if not callable(getattr(obj[0], x))
                            and not x.startswith('__')
                            and not x.endswith('__')]

        for i, j in enumerate(list_attributes):
            attribute = obj[0].__getattribute__(list_attributes[i])
            if type(attribute) == np.ndarray:
                attribute = attribute.tolist()
                obj[0].__setattr__(list_attributes[i], attribute)
                self.tolisted_attributes.append(obj[0].__class__.__name__ + '.' + list_attributes[i])
            elif type(attribute) not in primitive_types:
                mother_obj.getReadyForSerialization([attribute], mother_obj, primitive_types)