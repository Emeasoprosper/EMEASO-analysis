from flask import Flask, render_template, Response, request, jsonify
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
import pickle

model = LinearRegression()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template ("index.html")

@app.route('/calculation', methods=['GET', 'POST'])
def calculation():
    return render_template("calculation.html")

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    return render_template("chartv2.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    print("started")
    linear_prediction = None
    logistic_prediction = None
    error = None
    input_value = None
    if request.method == 'POST':
        try:
            print("step 1")
            input_value = float(request.form['input_value'])
            cacl_type = request.form['model_type']
            print(cacl_type)
            print(input_value)
            input_array = np.array([[input_value]])
            print("got data successfully")

            if cacl_type == "SCREEN TIME":
                print(True)
                with open('models/screen_time.pkl', 'rb') as f:
                    loaded = pickle.load(f)
                    linear_model = loaded['model']
                print("loaded model well")
                linear_prediction = linear_model.predict(input_array)[0]
                linear_prediction = int(linear_prediction)
                if linear_prediction >= 100:
                    linear_prediction = 100
                print(linear_prediction)

            elif cacl_type == "STUDY HOURS":
                print(True)
                with open('models/study hours.pkl', 'rb') as f:
                    loaded = pickle.load(f)
                    linear_model = loaded['model']
                print("loaded model well")
                linear_prediction = linear_model.predict(input_array)[0]
                linear_prediction = int(linear_prediction)
                if linear_prediction >= 100:
                    linear_prediction = 100
                print(linear_prediction)

            elif cacl_type == "MENTAL HEALTH":
                with open('models/mental_health_rating.pkl', 'rb') as f:
                    loaded = pickle.load(f)
                    linear_model = loaded['model']
                print("loaded model well")
                linear_prediction = linear_model.predict(input_array)[0]
                linear_prediction = int(linear_prediction)
                if linear_prediction >= 100:
                    linear_prediction = 100
                print(linear_prediction)

            elif cacl_type == "EXERCISE FREQUENCY":
                with open('models/exercise_frequency.pkl', 'rb') as f:
                    loaded = pickle.load(f)
                    linear_model = loaded['model']
                print("loaded model well")
                linear_prediction = linear_model.predict(input_array)[0]
                linear_prediction = int(linear_prediction)
                if linear_prediction >= 100:
                    linear_prediction = 100
                print(linear_prediction)

            elif cacl_type == "DIET QUALITY":
                with open('models/diet_qualityy.pkl', 'rb') as f:
                    loaded = pickle.load(f)
                    linear_model = loaded['model']
                print("loaded model well")
                linear_prediction = linear_model.predict(input_array)[0]
                linear_prediction = int(linear_prediction)
                if linear_prediction >= 100:
                    linear_prediction = 100
                print(linear_prediction)

        except ValueError:
            error = "Invalid input. Please enter a numeric value."
        except Exception as e:
            error = str(e)

    return render_template('prediction.html', linear_prediction=linear_prediction, error=error, input_value=input_value)

@app.route('/show-data')
def show_data():
    df = pd.read_csv('dataset/student_habits_performance.csv')
    # Limit rows for performance, or remove .head(100) to show all
    return render_template('show_data.html', table=df.head(100).to_html(classes='data', index=False, border=0))

@app.route('/api/predict', methods=['POST'])
def api_predict():
    input_value = request.json.get('input_value')
    model_type = request.json.get('model_type')
    linear_prediction = None
    error = None

    try:
        input_value = float(input_value)
        input_array = np.array([[input_value]])

        if model_type == "SCREEN TIME":
            model_path = 'models/screen_time.pkl'
        elif model_type == "STUDY HOURS":
            model_path = 'models/study hours.pkl'
        elif model_type == "MENTAL HEALTH":
            model_path = 'models/mental_health_rating.pkl'
        elif model_type == "EXERCISE FREQUENCY":
            model_path = 'models/exercise_frequency.pkl'
        elif model_type == "DIET QUALITY":
            model_path = 'models/diet_qualityy.pkl'
        else:
            return jsonify({'error': 'Invalid model type.'}), 400

        with open(model_path, 'rb') as f:
            loaded = pickle.load(f)
            linear_model = loaded['model']
        linear_prediction = linear_model.predict(input_array)[0]
        linear_prediction = int(round(linear_prediction))
        if linear_prediction > 100:
            linear_prediction = 100
        if linear_prediction < 0:
            linear_prediction = 0

    except ValueError:
        error = "Invalid input. Please enter a numeric value."
    except Exception as e:
        error = str(e)

    return jsonify({'prediction': linear_prediction, 'input': input_value, 'error': error})

if __name__ == '__main__':
    app.run(debug=True)
