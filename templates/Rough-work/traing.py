from sklearn.linear_model import LinearRegression, LogisticRegression     
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the data
data = pd.read_csv('dataset/student_habits_performance.csv')
print("Data loaded successfully")
print("Original data:")
print(data.head())

# Initialize the model
model = LinearRegression()



# Prepare features (X) and target (y)
x = data[['mental_health_rating']]  # Define feature variable
y = data['exam_score']  # Define target variable

# Train the model
model.fit(x, y)
print("\nModel trained successfully")

# Save the model and encoder
with open('models/mental_health_rating.pkl', 'wb') as f:
    pickle.dump({'model': model}, f)
print("Model and encoder saved as 'mental_health_rating.pkl'")


test = model.predict([[2]])
print(test)