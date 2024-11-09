Car Price Preditor Link[https://car-price-predictor-yjjr.onrender.com]

This project uses a linear regression model to predict the price of a car based on its features like the company, model, year of purchase, fuel type, and kilometers driven. 
The model is trained using a cleaned and transformed dataset of cars, with the objective to help estimate the price of a used car accurately.

The dataset used for training the model is a cleaned and transformed collection of car data containing the following columns:
-company: The company that manufactures the car.
-name: The model name of the car.
-year: The year the car was manufactured.
-fuel_type: The type of fuel the car uses (e.g., Petrol, Diesel, Electric).
-kms_driven: The number of kilometers the car has been driven.
-price: The price of the car (target variable).

Technologies Used
-Python: Main programming language used.
-Pandas: Data manipulation and analysis library.
-Scikit-learn: Machine learning library to train the linear regression model.
-Flask: Web framework to serve the model and interact with users.
-Bootstrap: For styling the web interface.
-Pickle: For saving and loading the trained model.

Model Performance
The trained Linear Regression model achieves an R-squared (R²) accuracy of 89%, meaning that 89% of the variance in the car prices can be explained by the model.
This suggests that the model performs well in predicting car prices based on the input features.
