import numpy as np
import config
import pickle
import json

class Prediction():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm

    def model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

    def prediction(self):
        self.model()

        test_array = np.array([[self.SepalLengthCm,self.SepalWidthCm,self.PetalLengthCm,self.PetalWidthCm]])

        class_prediction = self.model.predict(test_array)[0]
        return class_prediction

if __name__ == '__main__':
    SepalLengthCm =   4.5
    SepalWidthCm =  2.0
    PetalLengthCm =  5.3
    PetalWidthCm =  2.5

    predict = Prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    predict.prediction()