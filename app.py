# Serve model as a flask application

import pickle
import numpy as np
import flask
from flask import Flask, request, render_template
import os

model = None
app = Flask(__name__)


def load_model():
    # model is declared as global variable
    global model
    # and can be access inside and outside of the function
    # path to pickle file
    script_dir = os.path.dirname(__file__)
    fileName = 'iris_trained_model.pkl'
    path = script_dir + "/" + fileName
    # load model from pickle file
    # path = os.getcwd() + "/" + fileName
    with open(path, 'rb') as f:
        model = pickle.load(f)

@app.route('/')
@app.route('/index')
def home_endpoint():
    # Prediction result is shown in predict.html
    return flask.render_template("index.html")

def predict_value(prediction_input):
    # Create vector
    to_predict = np.array(prediction_input).reshape(1,4)
    # Make prediction
    print(model)
    # load model at the beginning once only
    load_model()
    result = model.predict(to_predict)
    return result

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        # Here we put what we receive from the form into a dictionary
        # Example: {'seplen': '5', 'sepwid': '3', 'petlen': '3', 'petwid': '2'}
        form_input = request.form.to_dict()
        # Here we just extract the values
        form_values = list(form_input.values())
        # Here we bring them into the proper format (i.e., float)
        prediction_input = list(map(float, form_values))
        # Here we call function predict value
        result = predict_value(prediction_input)
        # Prediction result is shown in predict.html
        return render_template("predict.html", prediction_result=result)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)

