import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from flask import  jsonify
import json



class NeuralPredictor:

    scaler = None
    model = None


    def __init__(self):
        # Cargar los datos del archivo CSV
        data = pd.read_csv('./src/database/water_pollution.csv')

        # Separar los datos en conjuntos de entrenamiento y prueba
        X = data[['AirQuality', 'WaterPollution']]
        y = data[['AirQuality', 'WaterPollution']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        # Estandarizar los datos
        self.scaler = StandardScaler()   

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Crear la red neuronal
        self.model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(2, activation='sigmoid')
            ])

        # Compilar la red neuronal
        self.model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])    

        # Entrenar la red neuronal
        self.model.fit(X_train_scaled, y_train, epochs=100)


        # Evaluar la red neuronal
        loss, accuracy = self.model.evaluate(X_test_scaled, y_test)

        print('Loss:', loss)
        print('Accuracy:', accuracy)


    def get_prediction(self,data):

        data = self.scaler.transform(data)  
        predictions = self.model.predict(data)
        return predictions



    def get_prediction_text(self, y_pred):
        water_pollution_text = "Sin contaminación" if y_pred[0][0] < 0.5 else "Con contaminación"
        air_quality_text = "Mala" if y_pred[0][1] < 0.5 else "Buena"
        return {"Contaminación del agua": water_pollution_text, "Calidad del aire": air_quality_text}, 201


