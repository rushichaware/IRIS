import re
from flask import Flask,request,render_template,redirect,jsonify
import config
from project_app.utils import Prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form

        SepalLengthCm =   eval(data['SepalLengthCm'])
        SepalWidthCm =  eval(data['SepalWidthCm'])
        PetalLengthCm =  eval(data['PetalLengthCm'])
        PetalWidthCm =  eval(data['PetalWidthCm'])

        predict = Prediction(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
        flower_class = predict.prediction()

        return render_template('index.html', prediction_text='The Flower is {}'.format(flower_class))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=False)