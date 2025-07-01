# Trains Random Forest and Gradient Boosting models on extracted features.
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

# Placeholder dataset path
DATA_PATH = 'data/kinetoplast_features.csv'

def train_models():
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=['target'])
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    rf = RandomForestRegressor()
    gb = GradientBoostingRegressor()

    rf.fit(X_train, y_train)
    gb.fit(X_train, y_train)

    joblib.dump(rf, 'models/random_forest.pkl')
    joblib.dump(gb, 'models/gradient_boost.pkl')

    print("Models trained and saved.")

if __name__ == "__main__":
    train_models()
