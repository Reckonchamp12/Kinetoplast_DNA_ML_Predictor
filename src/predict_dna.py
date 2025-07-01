# Uses trained models to predict kinetoplast DNA deformation characteristics.
import joblib
import pandas as pd

def predict_from_features(feature_dict, model_type='rf'):
    model_path = f'models/{ "random_forest" if model_type=="rf" else "gradient_boost" }.pkl'
    model = joblib.load(model_path)

    input_df = pd.DataFrame([feature_dict])
    prediction = model.predict(input_df)

    return prediction[0]
