import pandas as pd

def prediction(data, encoder, model):

    df = pd.DataFrame(data, index=[0])

    if isinstance(df['P_temp'][0], str):
        df['P_temp'][0] = 25
    if isinstance(df['P_time'][0], str):
        df['P_time'][0] = 0.00  
    df['P_temp'] = df['P_temp'].astype(float)
    df['P_time'] = df['P_time'].astype(float) 
    
    features_categorical = ['Variety', 'Technique', 'Pretreatment',] 
    features_numerical = ['Vel', 'Temp', 'P_temp', 'P_time','RH',]

    X = df[features_categorical + features_numerical]
    X_en = encoder.transform(X)
    y_pred = model.predict(X_en)
    return y_pred