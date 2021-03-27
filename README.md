# Serve a Machine Learning Model as a Webservice
Serving a simple machine learning model as a webservice using [flask](http://flask.pocoo.org/) and [heroku](http://www.heroku.com/).

## Getting Started
1. Use Model_training.ipynb to train a logistic regression model on the [iris dataset](http://archive.ics.uci.edu/ml/datasets/iris) and generate a pickled model file (iris_trained_model.pkl)
2. Use app.py to wrap the inference logic in a flask server to serve the model as a REST webservice:
    * Execute the command `python app.py` to run the flask app.
    * Go to the browser and hit the url `0.0.0.0:80` to get a message `Hello World!` displayed. **NOTE**: A permission error may be received at this point. In this case, change the port number to 5000 in `app.run()` command in `app.py`. 
    (Port 80 is a privileged port, so change it to some port that isn't, eg: 5000)
 3. To deploy the machine learning model on Heroku, create first a heroku account.
 4. Login to Heroku
 5. Create a heroku app and connect to the GIT repository 

