from ie_bike_model.model import predict


def test_predict_returns_expected_list():
    import datetime as dt

    dict = {
        "date": dt.datetime(2011, 1, 1, 0, 0, 0),
        "weathersit": 1,
        "temperature_C": 9.84,
        "feeling_temperature_C": 14.395,
        "humidity": 81.0,
        "windspeed": 0.0,
    }
    expected_array = [11]
    pred = predict(dict)
    print("pred output: ", pred)
    print("expected array type", type(expected_array))
    print("pred type", type(pred))
    assert pred == expected_array
