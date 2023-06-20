""" Response seeker
"""
import requests

payload = {
    "Sr. No.": 501,
    "Year": 2017,
    "Author": "Azzouz S.",
    "Exp": 1,
    "Data": 18,
    "Vel": 2,
    "Temp": 45,
    "RH": 20,
    "Fit": 0.142,
    "Variety": "Thomson",
    "Technique": "Convective",
    "Pretreatment": "Untreated",
    "P_temp": "Untreated",
    "P_time": "Untreated",
    "kg_r": "null",
    "kg_m": 69,
    "Diff_r": "null",
    "Diff_m": 0.000306,
    "Do": 750000000,
    "TD": 2483,
    "alpha": 0.0179,
    "aLR": 0.023,
    "aRL": 0.149,
    "mwR": "29.6",
    "Density": 1075,
    "Berry Count": 400,
    "Radius": 0.822,
    "Dry_Mass": 205.778,
    "Weight_i": 1000,
    "Vol_i": 930.233,
    "Water_i": 794.222,
    "MR_i": 1,
    "MC_i": 3.8596,
    "MC_i.1": 0.7942,
    "Weight_f": 289.098,
    "Vol_f": 224.107,
    "Water_f": 83.32,
    "MC_eq_Lit": 0.4049,
    "MC_eq_Lit.1": 0.2882,
    "MR_f": 0,
    "MC_f": 0.4049,
    "MC_f.1": 0.2882,
    "Pretreatment.1": "Untreated",
}

# "hours": 17,

url = "http://localhost:9696/predict"
response = requests.post(url, json=payload)
result = response.json()
print(result)
