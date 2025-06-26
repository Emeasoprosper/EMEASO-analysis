import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#so my first step is to import the libraries

try:
    csv_path = os.path.join(os.path.dirname(__file__), 'student_habits_performance.csv')
    data = pd.read_csv(csv_path)
    print(data.head())

    # to discribe our data
    print(data.describe(include='all'))

    # to check the data types of each column
    print(data.dtypes)

    #to check the shape of the data
    print(data.shape)

    # to check for missing values
    print(data.isnull().sum())


    
    # to Count the number of columns for each data type
    float_count = (data.dtypes == 'float64').sum()
    int_count = (data.dtypes == 'int64').sum()
    object_count = (data.dtypes == 'object').sum()
    
    print(f"Number of float columns: {float_count}")
    print(f"Number of integer columns: {int_count}")
    print(f"Number of object columns: {object_count}")


    #visualize missing value parterns  
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis') 
    plt.title('Missing Values Heatmap')
    plt.show()

    #distribution of key variables
    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    sns.histplot(data['study_hours_per_day'], bins=30, kde=True)
    plt.title('Study Time Distribution')

    plt.subplot(1,3,2)
    sns.histplot(data['social_media_hours'], bins=30, kde=True)
    plt.title('Social media time Distribution')

    plt.subplot(1,3,3)      
    sns.histplot(data['exam_score'], bins=30, kde=True)
    plt.title('Exam Score Distribution')

    plt.tight_layout()
    plt.show()

    #correlation matrix
    plt.pairplot(data[['exam_score', 'study_hours_per_day', 'social_media_hours']], diag_kind='kde')
    plt.suptitle('Pairplot of Key Variables', y=1.02)
    plt.show()


    #correlation matrix 
    plt.figure(figsize=(10, 6))
    correlation_matrix = data[['exam_score', 'study_hours_per_day', 'social_media_hours']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

    # Correlation Analysis
    # 1. Create a correlation matrix with all numeric columns
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = data[numeric_columns].corr()

    # 2. Visualize correlations with an improved heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap='coolwarm', 
                fmt='.2f',
                mask=np.triu(np.ones_like(correlation_matrix, dtype=bool)),
                square=True)
    plt.title('Correlation Matrix of Numeric Variables')
    plt.tight_layout()
    plt.show()

    # 3. Detailed pairplot for key variables
    sns.set_style("whitegrid")
    pair_plot = sns.pairplot(data[['exam_score', 'study_hours_per_day', 'social_media_hours']], 
                            diag_kind='kde',
                            plot_kws={'alpha': 0.6},
                            diag_kws={'linewidth': 2})
    pair_plot.fig.suptitle('Relationships Between Key Variables', y=1.02, size=16)
    plt.show()

    # 4. Print key correlations
    print("\nKey Correlations with Exam Score:")
    exam_correlations = correlation_matrix['exam_score'].sort_values(ascending=False)
    print(exam_correlations)

except FileNotFoundError:
    print("file not found")
except pd.errors.EmptyDataError:
    print("No data")
except pd.errors.ParserError:
    print("Parsing error")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print(f"\033[32mExecution completed\033[0m")






