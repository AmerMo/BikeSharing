import argparse
from flask import Flask, redirect, url_for, request, abort, render_template
import ie_bike_model.model as bike_model
import sklearn
import platform
import datetime as dt
import ie_bike_model
import sys, os
import time
from datetime import timedelta


class CustException(Exception):
    pass


class APIException(CustException):
    def __init__(self, status=None, title=None, type=None, detail=None, **kwargs):
        super(AIVException, self).__init__(detail)
        self.status = status
        self.detail = detail
        self.title = title
        self.type = type


app = Flask(__name__)


@app.route("/model")
def model():
    return render_template("index.html")


@app.route("/train")
def upload_file():
    return render_template("train.html")


@app.route("/train_and_persist", methods=["GET", "POST"])
def train_and_persist():
    if request.method == "POST":
        score = round(bike_model.train_and_persist(), 4)
        return {
            "Model Training": "train_and_persist",
            "status": "OK",
            "Score": score,
            "Method": "POST",
        }
    else:
        score = round(bike_model.train_and_persist(), 4)
        return {
            "Model Training": "train_and_persist",
            "status": "OK",
            "Score": score,
            "Method": "GET",
        }


# @app.route('/testPOST', methods=['GET','POST']) #allow both GET and POST requests
# def testPOST():
#     return '''<form method="POST">
#                   Language: <input type="text" name="language"><br>
#                   Framework: <input type="text" name="framework"><br>
#                   <input type="submit" value="Submit"><br>
#               </form>'''


@app.route("/predict")
def predict():
    mydict = dict()
    """
    check if passing parameters are wrong; if yes return error 400

    """
    try:
        if request.args.get("date") is not None:
            mydict["date"] = dt.datetime.fromisoformat(request.args.get("date"))
        else:
            mydict["date"] = dt.datetime(2011, 1, 1, 0, 0, 0)
    except ValueError:
        abort(400, "date parameter is not valid date format!")

    try:
        if request.args.get("weathersit") is not None:
            mydict["weathersit"] = int(request.args.get("weathersit"))
        else:
            mydict["weathersit"] = 1
    except ValueError:
        abort(400, "weathersit parameter is not integer !")

    try:
        if request.args.get("temperature_C") is not None:
            mydict["temperature_C"] = float(request.args.get("temperature_C"))
        else:
            mydict["temperature_C"] = 9.84
    except ValueError:
        abort(400, "temperature_C parameter is not float !")

    try:
        if request.args.get("feeling_temperature_C") is not None:
            mydict["feeling_temperature_C"] = float(
                request.args.get("feeling_temperature_C")
            )
        else:
            mydict["feeling_temperature_C"] = 14.395
    except ValueError:
        abort(400, "feeling_temperature_C parameter is not float !")

    try:
        if request.args.get("humidity") is not None:
            mydict["humidity"] = float(request.args.get("humidity"))
        else:
            mydict["humidity"] = 81.0
    except ValueError:
        abort(400, "humidity parameter is not float !")

    try:
        if request.args.get("windspeed") is not None:
            mydict["windspeed"] = float(request.args.get("windspeed"))
        else:
            mydict["windspeed"] = 0.0
    except ValueError:
        abort(400, "windspeed parameter is not float !")

    start_time = time.time()
    result = bike_model.predict(mydict)
    elapsed_time_secs = time.time() - start_time

    return {
        "result": result,
        "elapsed_time": round(elapsed_time_secs, 3),
    }


@app.route("/")
def hello():
    return {
        "status": "ok",
        "greeting": "Hello, to bike share prediction model!",
        "scikit-learn-version": sklearn.__version__,
        "python-version": platform.python_version(),
        "ie-bike-model-version": ie_bike_model.__version__,
    }


@app.route("/api")
def api():
    args = dict(request.args)
    return {
        "status": "ok",
        "name": args.get("name", "<NOT GIVEN>"),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sample flask application")
    parser.add_argument("--debug", action="store_true", help="enable debug mode")
    args = parser.parse_args()

    app.run(debug=args.debug)
