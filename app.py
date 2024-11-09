from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)
model = pickle.load(open('Car_LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned car data.csv')

@app.route('/', methods=['GET'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()
    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    company = data.get('company')
    car_model = data.get('car_models')
    year = int(data.get('year'))
    fuel_type = data.get('fuel_type')
    driven = int(data.get('kilo_driven'))

    input_data = pd.DataFrame([[car_model, company, year, driven, fuel_type]], 
                              columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    prediction = model.predict(input_data)
    return jsonify(prediction=np.round(prediction[0], 2))

if __name__ == '__main__':
    app.run(debug=True)
