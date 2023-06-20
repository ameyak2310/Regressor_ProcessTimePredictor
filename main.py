""" 
Flask app to serve churn model.
"""

# Libraries
import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Third party
from src.prediction import prediction


app = Flask("preocesstime")

with open("bin/reg_rf.bin", "rb") as f_in:
    """Loads encoder and model from binaries"""
    model = pickle.load(f_in)

with open("bin/enc.bin", "rb") as f_in:
    """Loads encoder and model from binaries"""
    enc = pickle.load(f_in)


@app.route("/predict", methods=["POST"])
def predict():
    """Prediction function

    Returns:
        dict: Returns probability and decesion.
    """
    payload = dict(request.get_json())
    # process_time = prediction(df=pd.DataFrame([payload]), enc=enc, model=model)
    process_time = prediction(data=payload, encoder=enc, model=model)
    result = {
        "PROCESS TIME": float(process_time[0]),
    }
    print(result)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9696)
