from flask import Flask, render_template, Response
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# Vibrant colors for bars
COLORS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD',
          '#D4A5A5', '#9B6B6B', '#E9967A', '#66CDAA', '#4682B4']

app = Flask(__name__, 
           template_folder='templates',
           static_folder='static')
data = pd.read_csv('dataset/student_habits_performance.csv')

CHARTS_DIR = 'static/images/charts'
os.makedirs(CHARTS_DIR, exist_ok=True)

def create_bar_chart(x, y, title, xlabel, ylabel, figsize=(6,4)):
    plt.figure(figsize=figsize, facecolor='white')
    ax = plt.gca()
    ax.set_facecolor('white')
    
    # Create bars with solid colors
    bars = plt.bar(x, y, color=COLORS[:len(x)], alpha=1.0)
    
    # Style the title and labels
    plt.title(title, pad=20, fontsize=12, fontweight='bold', color='black')
    plt.xlabel(xlabel, fontsize=10, color='black')
    plt.ylabel(ylabel, fontsize=10, color='black')
    
    # Style the grid and ticks
    plt.grid(True, alpha=0.2, color='gray', linestyle='--')
    ax.tick_params(colors='black')
    plt.xticks(rotation=45 if len(x) > 6 else 0)
    
    # Style the spines
    for spine in ax.spines.values():
        spine.set_color('black')
    
    plt.tight_layout()

def save_chart(name):
    chart_path = f'static/images/charts/{name}.png'
    plt.savefig(chart_path, format='png', dpi=300, bbox_inches='tight', 
                facecolor='white')
    plt.close()
    return os.path.join('images/charts', f'{name}.png')

@app.route('/')
def home():
    charts = {}
    
    # Study Hours Chart
    study_hours = np.ceil(data['study_hours_per_day']).astype(int)
    create_bar_chart(study_hours.unique(), 
                    [data[data['study_hours_per_day'] == hrs]['exam_score'].mean() 
                     for hrs in study_hours.unique()],
                    'Impact of Study Hours on Exam Performance',
                    'Study Hours Per Day', 'Average Exam Score')
    charts['study_hours'] = save_chart('study_hours')
    
    # Screen Time Chart
    screen_time = np.ceil(data['social_media_hours'] + data['netflix_hours']).astype(int)
    screen_time_unique = sorted(screen_time.unique())
    create_bar_chart(screen_time_unique,
                    [data[screen_time == hrs]['exam_score'].mean() 
                     for hrs in screen_time_unique],
                    'Effect of Screen Time on Academic Performance',
                    'Screen Time (Hours/Day)', 'Average Exam Score')
    charts['screen_time'] = save_chart('screen_time')
    
    # Exercise Chart
    exercise_freq = sorted(data['exercise_frequency'].unique())
    create_bar_chart(exercise_freq,
                    [data[data['exercise_frequency'] == freq]['exam_score'].mean() 
                     for freq in exercise_freq],
                    'Impact of Exercise on Academic Performance',
                    'Exercise Frequency (Days/Week)', 'Average Exam Score')
    charts['exercise'] = save_chart('exercise')
    
    # Attendance Chart
    attendance = pd.cut(data['attendance_percentage'], 
                       bins=[0, 50, 60, 70, 80, 90, 100],
                       labels=['≤50', '51-60', '61-70', '71-80', '81-90', '91-100'])
    create_bar_chart(attendance.value_counts().index, 
                    data.groupby(attendance)['exam_score'].mean(),
                    'Attendance impact on Academic Performance',
                    'Attendance Range (%)', 'Average Exam Score')
    charts['attendance'] = save_chart('attendance')
    
    # Sleep Quality Chart
    sleep_hours = data['sleep_hours'].round(0)

    create_bar_chart(sleep_hours,
                    [data[data['sleep_hours'] == hrs]['exam_score'].mean() 
                     for hrs in sleep_hours],
                    'Sleep Quality Impact on Academic Performance',
                    'Sleep Hours per Night', 'Average Exam Score')
    charts['sleep_quality'] = save_chart('sleep_quality')
    
    # Mental Health Chart
    mental_health = sorted(data['mental_health_rating'].unique())
    create_bar_chart(mental_health,
                    [data[data['mental_health_rating'] == rating]['exam_score'].mean() 
                     for rating in mental_health],
                    'Mental Health Impact on Academic Performance',
                    'Mental Health Rating', 'Average Exam Score')
    charts['mental_health'] = save_chart('mental_health')
    
    # Diet Quality Chart
    diet_map = {'Poor': 1, 'Average': 2, 'Good': 3}
    diet_labels = ['Poor', 'Average', 'Good']
    create_bar_chart(diet_labels,
                    [data[data['diet_quality'] == quality]['exam_score'].mean() 
                     for quality in diet_labels],
                    'Diet Quality Impact on Academic Performance',
                    'Diet Quality', 'Average Exam Score')
    charts['diet_quality'] = save_chart('diet_quality')
    
    # Correlations Chart
    numeric_cols = ['study_hours_per_day', 'sleep_hours', 'mental_health_rating', 
                   'attendance_percentage', 'exercise_frequency']
    correlations = data[numeric_cols].corrwith(data['exam_score']).abs().sort_values(ascending=False)
    
    plt.figure(figsize=(8,6), facecolor='white')
    ax = plt.gca()
    ax.set_facecolor('white')
    
    bars = plt.bar(range(len(correlations)), correlations.values, color=COLORS[:len(correlations)])
    plt.xticks(range(len(correlations)), correlations.index, rotation=45)
    
    plt.title('Key Factors Influencing Exam Performance', pad=20, fontsize=12, fontweight='bold', color='black')
    plt.xlabel('Factors', fontsize=10, color='black')
    plt.ylabel('Correlation Strength', fontsize=10, color='black')
    
    ax.tick_params(colors='black')
    plt.grid(True, alpha=0.2, color='gray', linestyle='--')
    
    for spine in ax.spines.values():
        spine.set_color('black')
    
    plt.tight_layout()
    charts['correlations'] = save_chart('correlations')
    
    return render_template('index.html', charts=charts)



@app.route("/chart")
def chart():
    print("Chart route accessed!") 
    charts = {}
    
    # Study Hours Chart
    study_hours = np.ceil(data['study_hours_per_day']).astype(int)
    create_bar_chart(study_hours.unique(), 
                    [data[data['study_hours_per_day'] == hrs]['exam_score'].mean() 
                     for hrs in study_hours.unique()],
                    'Impact of Study Hours on Exam Performance',
                    'Study Hours Per Day', 'Average Exam Score')
    charts['study_hours'] = save_chart('study_hours')
    
    # Screen Time Chart
    screen_time = np.ceil(data['social_media_hours'] + data['netflix_hours']).astype(int)
    screen_time_unique = sorted(screen_time.unique())
    create_bar_chart(screen_time_unique,
                    [data[screen_time == hrs]['exam_score'].mean() 
                     for hrs in screen_time_unique],
                    'Effect of Screen Time on Academic Performance',
                    'Screen Time (Hours/Day)', 'Average Exam Score')
    charts['screen_time'] = save_chart('screen_time')
    
    # Exercise Chart
    exercise_freq = sorted(data['exercise_frequency'].unique())
    create_bar_chart(exercise_freq,
                    [data[data['exercise_frequency'] == freq]['exam_score'].mean() 
                     for freq in exercise_freq],
                    'Impact of Exercise on Academic Performance',
                    'Exercise Frequency (Days/Week)', 'Average Exam Score')
    charts['exercise'] = save_chart('exercise')
    
    # Attendance Chart
    attendance = pd.cut(data['attendance_percentage'], 
                       bins=[0, 50, 60, 70, 80, 90, 100],
                       labels=['≤50', '51-60', '61-70', '71-80', '81-90', '91-100'])
    create_bar_chart(attendance.value_counts().index, 
                    data.groupby(attendance)['exam_score'].mean(),
                    'Attendance impact on Academic Performance',
                    'Attendance Range (%)', 'Average Exam Score')
    charts['attendance'] = save_chart('attendance')
    
    # Sleep Quality Chart
    sleep_hours = data['sleep_hours'].round(0)

    create_bar_chart(sleep_hours,
                    [data[data['sleep_hours'] == hrs]['exam_score'].mean() 
                     for hrs in sleep_hours],
                    'Sleep Quality Impact on Academic Performance',
                    'Sleep Hours per Night', 'Average Exam Score')
    charts['sleep_quality'] = save_chart('sleep_quality')
    
    # Mental Health Chart
    mental_health = sorted(data['mental_health_rating'].unique())
    create_bar_chart(mental_health,
                    [data[data['mental_health_rating'] == rating]['exam_score'].mean() 
                     for rating in mental_health],
                    'Mental Health Impact on Academic Performance',
                    'Mental Health Rating', 'Average Exam Score')
    charts['mental_health'] = save_chart('mental_health')
    
    # Diet Quality Chart
    diet_map = {'Poor': 1, 'Average': 2, 'Good': 3}
    diet_labels = ['Poor', 'Average', 'Good']
    create_bar_chart(diet_labels,
                    [data[data['diet_quality'] == quality]['exam_score'].mean() 
                     for quality in diet_labels],
                    'Diet Quality Impact on Academic Performance',
                    'Diet Quality', 'Average Exam Score')
    charts['diet_quality'] = save_chart('diet_quality')
    
    # Correlations Chart
    numeric_cols = ['study_hours_per_day', 'sleep_hours', 'mental_health_rating', 
                   'attendance_percentage', 'exercise_frequency']
    correlations = data[numeric_cols].corrwith(data['exam_score']).abs().sort_values(ascending=False)
    
    plt.figure(figsize=(8,6), facecolor='white')
    ax = plt.gca()
    ax.set_facecolor('white')
    
    bars = plt.bar(range(len(correlations)), correlations.values, color=COLORS[:len(correlations)])
    plt.xticks(range(len(correlations)), correlations.index, rotation=45)
    
    plt.title('Key Factors Influencing Exam Performance', pad=20, fontsize=12, fontweight='bold', color='black')
    plt.xlabel('Factors', fontsize=10, color='black')
    plt.ylabel('Correlation Strength', fontsize=10, color='black')
    
    ax.tick_params(colors='black')
    plt.grid(True, alpha=0.2, color='gray', linestyle='--')
    
    for spine in ax.spines.values():
        spine.set_color('black')
    
    plt.tight_layout()
    charts['correlations'] = save_chart('correlations')
    
    return render_template('chartv2.html', charts=charts)
  


if __name__ == '__main__':
    app.run(debug=True)