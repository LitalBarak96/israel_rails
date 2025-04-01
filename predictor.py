import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

class DelayPredictor:
    def __init__(self, df):
        self.df = df.copy()
        self.model = None
        self.le_station = LabelEncoder()

    def prepare_data(self):
        # Fit encoder on all station names, not just delays
        self.le_station.fit(self.df['train_station'])

        # Filter only delay records
        df = self.df[self.df['train_status'] == 'Delay'].copy()

        # Encode station names based on full fit
        df['station_code'] = self.le_station.transform(df['train_station'])

        self.X = df[['station_code', 'year', 'month']]
        self.y = df['count']

    def train(self):
        self.prepare_data()
        X_train, X_test, y_train, y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate model
        y_pred = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        print(f"Model MAE: {mae:.2f}")
        print(f"Model R² Score: {r2:.2f}")



    def predict(self, station, year, month):
        if station not in self.le_station.classes_:
            raise ValueError(f"Station '{station}' was not seen during training.")
        code = self.le_station.transform([station])[0]
        input_df = pd.DataFrame([{
            "station_code": code,
            "year": year,
            "month": month
        }])
        return self.model.predict(input_df)[0]

    def save_model(self, path="delay_model.pkl"):
        joblib.dump((self.model, self.le_station), path)

    def load_model(self, path="delay_model.pkl"):
        self.model, self.le_station = joblib.load(path)