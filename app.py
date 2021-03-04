# Serve model as a flask application

import pickle
import numpy as np
import flask
from flask import Flask, request, render_template
import os

model = None
app = Flask(__name__)


def load_model():
    global model
    # model variable refers to the global variable
    script_dir = os.path.dirname(__file__)
    fileName = 'iris_trained_model.pkl'
    path = script_dir + '/' + fileName
    print(path)
    with open(path, 'rb') as f:
        model = pickle.load(f)
        print(model)


@app.route('/')
@app.route('/index')
def home_endpoint():
    print("hello world")
    return flask.render_template("index.html")

def ValuePredictor(to_predict_list):
    #data = request.get_json()  # Get data posted as a json
    #data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
    #prediction = model.predict(data)  # runs globally loaded model on the data
    #return str(prediction[0])
    to_predict = np.array(to_predict_list).reshape(1,4)
    load_model()  # load model at the beginning once only
    #loaded_model = pickle.load(open(“model.pkl”,”rb”))
    result = model.predict(to_predict)
    return result[0]

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    print("hello world POST")
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list)
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        prediction = str(result)
        print(prediction)
        return render_template("predict.html", predictionStr=prediction)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

