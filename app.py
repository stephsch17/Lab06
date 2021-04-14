# Serve model as a flask application
import pickle
import numpy as np
import flask
from flask import Flask, request, render_template
import os

app = Flask(__name__)


# Load model from pickle file
def load_model():
    script_dir = os.path.dirname(__file__)
    fileName = 'iris_trained_model.pkl'
    path = script_dir + "/" + fileName
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model

@app.route('/')
@app.route('/index')
def home_endpoint():
    return flask.render_template("index.html")

# Create input vector, load model, and make prediction
def predict_value(prediction_input):
    to_predict = np.array(prediction_input).reshape(1,4)
    model = load_model()
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

