# Serve a Machine Learning Model as a Webservice
Serving a simple machine learning model as a webservice using [flask](http://flask.pocoo.org/) and [docker](https://www.docker.com/).

## Getting Started
1.) Use Model_training.ipynb to train a model on the iris dataset and generate a pickled model file (iris_trained_model.pkl)
3.) Use app.py to wrap the inference logic in a flask server to serve the model as a REST webservice:
4.) Execute the command python app.py to run the flask app.
5.) Go to the browser and hit the url 0.0.0.0:5000 to get a website displayed to enter our observations. 
6.) To deploy the machine learning model on Heroku, create first a heroku account.
7.) Login to Heroku
8.) Create a heroku app and connect to the GIT repository
9.) Once successfuly build and deployed start the Heroku app and use it for creating predictions
