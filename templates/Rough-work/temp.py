# ------------------------------
# Linear and Logistic Regression Training + Flask App
# ------------------------------

from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression, make_classification

app = Flask(__name__)

# ------------------------------
# TRAINING LINEAR REGRESSION MODEL
# ------------------------------
# Generate sample regression data
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Train linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train_reg, y_train_reg)

# Save linear model
with open("linear_model.pkl", "wb") as f:
    pickle.dump(linear_model, f)

# ------------------------------
# TRAINING LOGISTIC REGRESSION MODEL
# ------------------------------
# Generate sample classification data
X_cls, y_cls = make_classification(n_samples=100, n_features=1, n_classes=2, n_informative=1, n_redundant=0, random_state=42)
X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

# Train logistic regression model
logistic_model = LogisticRegression()
logistic_model.fit(X_train_cls, y_train_cls)

# Save logistic model
with open("logistic_model.pkl", "wb") as f:
    pickle.dump(logistic_model, f)

# ------------------------------
# FLASK ROUTES
# ------------------------------
@app.route('/', methods=["GET", "POST"])
def index():
    linear_prediction = None
    logistic_prediction = None
    error = None
    if request.method == 'POST':
        try:
            input_value = float(request.form.get('input_value'))
            input_array = np.array([[input_value]])

            # Load and predict with linear regression
            with open("linear_model.pkl", "rb") as f:
                loaded_linear_model = pickle.load(f)
                linear_prediction = loaded_linear_model.predict(input_array)[0]

            # Load and predict with logistic regression
            with open("logistic_model.pkl", "rb") as f:
                loaded_logistic_model = pickle.load(f)
                logistic_prediction = loaded_logistic_model.predict(input_array)[0]

        except ValueError:
            error = "Please enter a valid number."
        except Exception as e:
            error = f"An error occurred: {e}"

    return render_template('temp.html', 
                           linear_prediction=linear_prediction,
                           logistic_prediction=logistic_prediction,
                           error=error)

if __name__ == '__main__':
    app.run(debug=True)

