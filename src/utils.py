# Contains helper functions for data preprocessing and validation.
import pandas as pd

def normalize_features(df):
    return (df - df.mean()) / df.std()

def validate_data(df):
    # Simple validation
    assert not df.isnull().any().any(), "Data contains nulls!"
    return True
