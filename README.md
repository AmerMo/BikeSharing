# Bike Sharing Model

## Intro

The `app.py` contains code for the flask application that can be run on its own. The rest of the files refer to the `ie_bike_model` package.

this app is used to predict # users renting a bike in a specific


## Running the app

0. Make sure you have  `ie_bike_model` package installed, if not install it as follows:  

```
$ pip install lib/
```

0. Make sure you have `flask` installed, otherwise run the following:

```
$ pip install flask
```
1. To run the app  in the command line use one of the following

```
$ python app.py --debug
```
incase you need to run in debugging mode

or simply run the following
```
$ flask run
```

## Program execution

1. To see modules versions information, please visit http://127.0.0.1:5000/

2. Train first your model by running http://127.0.0.1:5000/train_and_persist

3. To train the model using POST method, please run http://127.0.0.1:5000/train
then click on submit to see the training results

4. To see both train and predict at the same index level please visit  http://127.0.0.1:5000/model
then click on submit to see the training results

5. Then predict by openeing http://127.0.0.1:5000/predict?date=2011-06-30T10:00:00&weathersit=1&temperature_C=20&feeling_temperature_C=18&humidity=80&windspeed=5 with your browser.


6. Incase you decided to run the predict function without any parameters or some of them, the program will take care of that and will pass default values been initialized inside the predict function, for that you can try running the following

http://127.0.0.1:5000/predict
