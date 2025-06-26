from flask import Flask, render_template, Response
import io
import base64
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('PROJECT3/dataset/student_habits_performance.csv')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Loads the HTML page from the templates folder


@app.route('/barchart')
def chart():
    data['study_hours_per_day'] = np.ceil(data['study_hours_per_day']).astype(int)
    # Plot the bar chart
    plt.figure(figsize=(6,4))
    plt.bar(x=data['study_hours_per_day'], height=data['exam_score'], color='skyblue')
    plt.xlabel('Study Hours Per Day')
    plt.ylabel('Exam Score')
    plt.title('Study Hours vs Exam Score')
    plt.tight_layout()

    # Convert plot to PNG image for display
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode()
    return render_template('index.html', chart_url=chart_url)


if __name__ == '__main__':
    app.run(debug=True)