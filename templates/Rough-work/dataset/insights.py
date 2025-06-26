import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#1 Load the dataset
data = pd.read_csv('PROJECT3/dataset/student_habits_performance.csv')
analysis_data = data.copy()

#2 Display the first few rows of the dataset            
####print(data.head())

####print(data.columns)

#QUETION 1. What is the sum_total of the students population?
sum_total = data['student_id'].nunique()
####print(f"Total number of students: {sum_total}")


male = data['gender']=="Male"
#print(f"Total number of male students: {male.sum()}")   

female = data['gender']=="Female"
#print(f"Total number of female students: {female.sum()}")

sum_gender = female + male
####print(f"total number of all genders: {sum_gender}")

new_survived = pd.Categorical(data["gender"])
###print(new_survived.describe())

genderNanValues = data['gender'].isnull().sum()
###print(f"Number of missing values in gender column: {genderNanValues}")

#finding other genders that are not Male or Female:
#step 1: convert gender column to a sting type
otherGender = data['gender']
otherGender = otherGender.astype(str)

#step 2: ###print the characters that are not Mlae and Female
unusual_genders = otherGender[~otherGender.isin(['Male', 'Female'])]
#print(f"Other values not Male or Female:{unusual_genders.unique()}")

#step 3: count them to verify
#print(len(unusual_genders))


#QUESTION 3. Sum_total of students who have pertime jobs? 
#total number of students in the part_time_job column
Full_student_jobs_column = len(data['part_time_job'])
#print(f"Total number of students in the part_time_job column: {Full_student_jobs_column}")

 #step 1: ###print out the column for students who have jobs
students_with_jobs = data[data['part_time_job'] == 'Yes']
changedStudentWithJobs = students_with_jobs.shape[0]
#print(f"Number of students with part-time jobs: {changedStudentWithJobs}")

students_with_jobs_count = len(students_with_jobs)
###print(f"number of students with part_time_jobs are: {students_with_jobs_count}")
#or this way
students_with_jobs2 = (data['part_time_job'] == 'Yes').sum()
###print(f"Number of students with part-time jobs (using sum): {students_with_jobs2}")

workingStudents = pd.Categorical(data['part_time_job'])
####print(workingStudents.describe())

#QUESTION 4:Sum_total of students who don't work at all?
students_without_jobs = (data['part_time_job']=='No').sum()
#print(students_without_jobs) 
# we're sticking with the above method


#QUESTION 5. what gender has the highest attendance_percentage?


#step 2: find the average male attendance percentage
male_attendance = data[data['gender'] == 'Male']['attendance_percentage'].mean()
#print(f"\nAverage male attendance: {male_attendance:.2f}%")

#step 3: find the average female attendance percentage
female_attendance = data[data['gender'] == 'Female']['attendance_percentage'].mean()
###print(f"Average female attendance: {female_attendance:.2f}%")

#or
attendance = data.groupby("gender")['attendance_percentage'].mean()
attendance = attendance.round(2)
#print(f"\nAverage attendance percentage {attendance}%") 


################ASSIGNMENT CONTINUITY ###################

#QUESTION 6. How does average study time relate to exam scores?
#step 1: Calculate the average study time
average_study_time = data["study_hours_per_day"].mean()
####print(f"\nAverage study time: {average_study_time:.2f} hours/day")

#step 2: Calculate the average exam score
average_exam_score = data["exam_score"].mean()
####print(f"Average exam score: {average_exam_score:.2f}")



#7. What is the average exam score of students with mental health issues vs exam_score?
mental_health_issues = data['mental_health_rating'].describe()
####print(mental_health_issues)

#step 1: what does the highest mental health rating score in exam?
max_mental_health_rating = data['mental_health_rating'].max()
####print(f"Maximum mental health rating: {max_mental_health_rating}")

#step 2: what does the minimum mental health rating score in exam?
min_mental_health_rating = data['mental_health_rating'].min()
####print(f"Minimum mental health rating: {min_mental_health_rating}")

#step 3: what does the average mental health rating score in exam?
average_mental_health_rating = data['mental_health_rating'].mean()
####print(f"Average mental health rating: {average_mental_health_rating:.2f}")

sns.scatterplot(data=data, x='mental_health_rating', y='exam_score')
plt.title('Mental Health Rating vs Exam Score')
plt.xlabel('Mental Health Rating')
plt.ylabel('Exam Score')
#plt.show()
#Conclusion: The scatter plot shows the relationship between mental health rating and exam score and
#show that there is no direct correlation between the two variables.

#find correlation between mental health rating and exam score
correlation = data['mental_health_rating'].corr(data['exam_score'])
####print(f"Correlation between mental health rating and exam score: {correlation:.2f}")

#QUESTION . Does poor diet quality correlate with lower exam performance?
diet_quality = data['diet_quality'].describe()
####print(diet_quality)
####print(f"Diet quality categories:\n{diet_quality}")

#replace the renamed diet_quality column with the original column
data['diet_quality'] = diet_quality
####print(f"Diet quality summary:\n{diet_quality.describe()}")

diet_quality = data["diet_quality"].corr(data['exam_score'])
####print(f"Correlation between diet quality and exam score: {diet_quality:.2f}")

sns.scatterplot(data=data, x='diet_quality', y='exam_score')
plt.title('diet_quality vs Exam Score')
plt.xlabel('diet_quality')
plt.ylabel('Exam Score')
#plt.show()
#conclusion: there's no positive correlation beteween the diet quality and exam score.

#QUESTION 9. What percentage of students spend more than 4 hours daily on social media?

#round the social media hours to the nearest whole number
data['social_media_hours'] = np.ceil(data['social_media_hours']).astype(int)
####print(data['social_media_hours'])
cus = pd.Categorical(data['social_media_hours'])
#print(f"Social media hours categories:\n{cus.describe()}")
percent_cus = (data['social_media_hours'] >4).sum() / len(data)*100
#print(f"Percentage of student socila median hour:{percent_cus}%")

#bellow is the scatter plot code
sns.scatterplot(data=data, x='social_media_hours', y='exam_score')
plt.title('Social Media Hours vs Exam Score')
plt.xlabel('Socila Media Hours')
plt.ylabel('Exam Score')
#plt.show()
# Conclusion: student who spend more time in social media tend to have higher exam scores

#social_media_hours = pd.Categorical(data['social_media_hours']).describe()
####print(f"Social media hours categories:\n{social_media_hours}")



# QUESTION 10. How does Netflix usage correlate with exam scores?

####print(f"heres the discription \n{np.ceil(data['netflix_hours'])}")

#netflix_hours = np.correlate(data['netflix_hours'] , data['exam_score']).
netflix_hours = data['netflix_hours'].corr(data['exam_score'])
#print(f"Correlation between Netflix hours and exam score: {netflix_hours:.2f}")

sns.scatterplot(data=data, x='netflix_hours', y='exam_score')
plt.title('Netflix Hours vs Exam Score')
plt.xlabel('Netflix Hours')
plt.ylabel('Exam Score')
#plt.show()
####print(netflix_hours)
#  Conclusion: there's no possitive correlation between two variables


#################### HERES THE TOUGH PART ####################
#Question 12. How many students use Netflix for more than 5 hours a day?

#students_using_netflix = data[data['netflix_hours']]
#add = []
#for i in range(len(students_using_netflix)):
#    if students_using_netflix['netflix_hours'][i] >= 5:
 #       i += 1
  #      add = add.append(i)
####print(f"Number of students using Netflix for more than 5 hours a day: {len(add)}")

###print(pd.Categorical(data['netflix_hours']).describe())
change = pd.Categorical(np.ceil(data['netflix_hours'])).describe()
changeTotal = 0
for i in range(len(change)):
    if i >= 5:
        changeTotal += 1

##print(changeTotal)

# Calculate students spending 5+ hours on Netflix
netflix_high_users = data[data['netflix_hours'] >= 5].shape[0]
#print(f"Number of students using Netflix for 5 or more hours: {netflix_high_users}")

# Optional: Create a visualization
plt.figure(figsize=(10, 6))
netflix_categories = ['< 5 hours', '≥ 5 hours']
netflix_counts = [
    data[data['netflix_hours'] < 5].shape[0],
    netflix_high_users
]

plt.bar(netflix_categories, netflix_counts, color=['#3498db', '#e74c3c'])
plt.title('Distribution of Netflix Usage Among Students')
plt.ylabel('Number of Students')
plt.xlabel('Daily Netflix Hours')

# Add value labels on top of bars
for i, v in enumerate(netflix_counts):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.tight_layout()
#plt.show()

# Create bins for Netflix hours with correct boundaries
bins = [0, 2, 4, 5, float('inf')]
labels = ['0-2 hours', '2-4 hours', '4-5 hours', '5+ hours']

# Convert netflix_hours to numeric type first to ensure proper binning
data['netflix_hours'] = pd.to_numeric(data['netflix_hours'], errors='coerce')

# Create categories without rounding
data['netflix_category'] = pd.cut(data['netflix_hours'], 
                                bins=bins, 
                                labels=labels, 
                                include_lowest=True, 
                                right=False)  # This makes the bins left-inclusive

# Get descriptive statistics
netflix_stats = pd.Categorical(data['netflix_category']).describe()
##print("\nNetflix Usage Statistics:")
##print(netflix_stats)

# Count students in each category
netflix_counts = data['netflix_category'].value_counts().sort_index()
##print("\nNumber of students in each Netflix category:")
##print(netflix_counts)


################## ABOVE IS A BIT TOUGH ######################

#QUESTION 13. What is the attendance distribution among students?
#avarage attendance percentage
attendance_percentage = data['attendance_percentage'].mean()
##print(f"Average attendance percentage: {attendance_percentage:.2f}%")
# Create a histogram for attendance percentage
plt.figure(figsize=(10, 6))
sns.histplot(data['attendance_percentage'], bins=20, kde=True, color='skyblue')
plt.title('Attendance Percentage Distribution')
plt.xlabel('Attendance Percentage')
plt.ylabel('Number of Students')
plt.xlim(0, 100)  # Set x-axis limits to 0-100%
plt.xticks(np.arange(0, 101, 10))  # Set x-ticks at every 10%
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
#plt.show()
  #ive encountered so many problems and ive come to realise that if you make all th plottings...
  #...and after that you finish all with just one union plt.show() it will show all together at once.
#CONCLUTION: Students that are frequent in class are over 84 percent.

#QUESTION 14. Which gender has the highest average attendance percentage?
#answer = female with over 84.37 percent
 
#QUESTION 15. How many students score above average based on parental education?
# Calculate the average exam score
average_exam_score = data['exam_score'].mean()
###print(f"Average exam score: {average_exam_score:.2f}")
#parents education lavel categories
parental_education = pd.Categorical(data['parental_education_level']).describe()
##print("\nParental Education Level Categories:")
###print(parental_education)
#???It turns out we have nan values???NEEDS TO BE RECTIFIED!

#calculating how many students score above average with their parental education level
above_average_students = data[data['exam_score'] > average_exam_score]
above_average_counts = above_average_students['parental_education_level'].value_counts()
print("\nNumber of students scoring above average by parental education level:")
print(above_average_counts)
#in this can see that those with higher popultions had parents with bachelor's degree.

#QUESTION 16. What is the average number of sleep hours for top-performing students? 
sleep_hours = pd.Categorical(data['sleep_hours']).describe()
##print("\nSleep Hours Categories:")
##print(sleep_hours)
#i'm affraid of rounding them up because of time...

#comparing studenst who score above average with their sleep hours
#for average student performance see QUESTION 15.
average_sleep_hours = above_average_students['sleep_hours'].mean()
average_sleep_hours = np.ceil(average_sleep_hours)  
##print(f"\nAverage sleep hours for top-performing students: {average_sleep_hours:.2f} hours")
# Create a SCATTER for sleep hours of top-performing students
plt.figure(figsize=(10, 6))
sns.scatterplot(data=above_average_students, x='sleep_hours', y='exam_score', color='purple')
plt.title('Sleep Hours vs Exam Score for Top-Performing Students')
plt.xlabel('Sleep Hours')
plt.ylabel('Exam Score')
plt.xlim(0, 12)  # Set x-axis limits to a reasonable range
plt.xticks(np.arange(0, 13, 1))  # Set x-ticks at every hour
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
#plt.show()
#CONCLUSION: there's no positive corelation. 
#...students can score anything irrespective of their sleep hour.

#QUESTION 17. What percentage of students who sleep less than 6 hours score below average?
low_sleep_mask = data['sleep_hours'] < 6
low_sleep_categories = pd.Categorical(low_sleep_mask)
##print(low_sleep_categories.describe())
##print(f"\nNumber of students with low sleep: {low_sleep_mask.sum()}")

#calculating the averatge score
low_average_score = data['exam_score'] < average_exam_score
low_sleep_low_score = data[(low_sleep_mask) & (low_average_score)]
##print(f"Students with low sleep and low score: {len(low_sleep_low_score)}")

#calculating percentage of students with low sleep and low score
Total_percentage = len(low_sleep_low_score) / low_sleep_mask.sum() * 100
##print(f"Percentage od student that sleep less and have low score: {(Total_percentage):.2f}%")
#CONCLUTION:Students that sleep less than 6hrs tends to score below average. 
#SUGGESTION: Try sleeping more. 

#QUESTION 18. Are students with high attendance more likely to study more?
students_attendance = pd.Categorical(data['attendance_percentage']).describe()
##print("\nAttendance Percentage Categories:")
##print(students_attendance)

#comparing students with attendance >=80 with study_hours_per_day
#checking fro number of students that scored over 80 and above
high_attendace_count = data['attendance_percentage'] >= 80
high_attendance_mask = pd.Categorical(high_attendace_count).describe()
##print(f"\nNumber of students with high exam_score (>=80%): {high_attendance_mask}")

#checking number of students study hours
study_hours = data['study_hours_per_day'] >= 3.5
high_read_hours = pd.Categorical(study_hours).describe()
#print(f"\nNumber of students with high study hours (>=3.5 hours): {high_read_hours}")

#comparing the two categories
high_attendance_study = data[high_attendace_count & study_hours]  
high_attendance_study_count = high_attendance_study.shape[0]
#print(f"\nNumber of students with high attendance and high study hours: {high_attendance_study_count}")

#corelating total high attendance against total student study hour
correlation_attendance_study = high_attendace_count.corr(data['study_hours_per_day'])
#print(f"\nCorrelation between high attendance and high study hours: {correlation_attendance_study:.2f}")

#scatter plot between high attendance and study hours
sns.scatterplot(data=data, x = data['study_hours_per_day'], y =data['attendance_percentage'] )
plt.title("High Attendance vs Study Hours")
plt.xlabel("Attendance Percentage")
plt.ylabel("Study Hours per Day")
#plt.show()
################ WORKING ON IT #############################3

#checking percentage of students with high attendance and high study hours
#attendance_study_hours = (high_attendance_study_count / ) *100
##print(f"""percentage of students with both high attendance and 
      #high study hours from the entire school: {attendance_study_hours}%""")




#QUESTION 19. How many students have excellent mental health but still perform poorly?
describe_mental_health = pd.Categorical(data['mental_health_rating']).describe()
##print("\nMental Health Rating Categories:")
##print(describe_mental_health)
#from the description lets say mental health is from 5 and above is excellent
#step 2: show the students that mental healths are >= 5
excellent_mental_health = data['mental_health_rating'] >=5 
describe_excell_ment_health = pd.Categorical(excellent_mental_health).describe()
#print(f"\nTrue represnts the excelent metal health:")
#print(describe_excell_ment_health)
#step 3: check number of students that perform poorly:
poor_performance = data['exam_score'] <= 50
describe_poor_perform = pd.Categorical(poor_performance).describe()
#print(f"\n'True' bellow shows number of students perform poor:")
#print(describe_poor_perform)

#step 4: compare in the popullation if students thathave high mentall health...
# ... also score high all in percentage 
sum_poorPerf_excelMentHealth = (poor_performance & excellent_mental_health).sum()
percentage_tot = (sum_poorPerf_excelMentHealth/len(data))*100
excel_mental_poor_exam = pd.Categorical(poor_performance & excellent_mental_health).describe()
print(f"Number of students with excellent mental health et low score: {excel_mental_poor_exam }")
print(f"Therefore, their percentage is over: {percentage_tot}%")
#CONCLUSION: 4.7% has excellent mental health but perform poorly


#QUESTION 20. What gender combination of study hours and sleep patterns leads to best results?
#MEANING: WHICH GENDER DO MORE OR LESS OF STUDY AND SLEEP MORE AND STILL GETS HIGH SCORE THE MOST.

#step 1:check number of male and female
print(f"Total number of male students: {male.sum()}") #check QUESTION 1
print(f"Total number of female students: {female.sum()}")#same

#step 2: calculate how many male and female study more
##FOR MALE:
study_description = (data['study_hours_per_day']).describe()
print(study_description.round(1))
max_male_study_time = ((data['gender'] == 'Male') & (data['study_hours_per_day'] >3.5))
print(f"number of MALE who study MORE are: {max_male_study_time.sum()}")
average_male_study_time = ((data['gender'] == 'Male') & (data['study_hours_per_day'] ==3.5))
print(f"number of MALE who study AVERAGE are: {average_male_study_time.sum()}")  
min_male_study_time = ((data['gender'] == 'Male') & (data['study_hours_per_day'] <3.5))
print(f"number of MALE who study LESS are: {min_male_study_time.sum()}")

#combining Male study time with sleep patter.
describe_sleep = (data['sleep_hours']).describe()
print(f"student sleep_hours description:")
print(describe_sleep.round(1))#discription

# 1. Males who study MORE (>3.5hrs) and sleep MORE (>6.7hrs)
high_sleep_study = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] > 3.5) & 
    (data['sleep_hours'] > 6.7)
]
print(f"Number of males who study MORE (>3.5hrs) and sleep MORE (6.7-10hrs): {len(high_sleep_study)}")

# 2. Males who study MORE (>3.5hrs) and sleep AVERAGE (6.5hrs)
avg_sleep_study = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] > 3.5) & 
    (data['sleep_hours'].between(6.5, 6.7))
]
print(f"Number of males who study MORE (>3.5hrs) and sleep AVERAGE (6.5-6.7hrs): {len(avg_sleep_study)}")

# 3. Males who study MORE (>3.5hrs) and sleep LESS (3.5-6.5hrs)
low_sleep_study = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] > 3.5) & 
    (data['sleep_hours'] < 6.5)
]
print(f"Number of males who study MORE (>3.5hrs) and sleep LESS (3.5-6.5hrs): {len(low_sleep_study)}")

print("\n=== MALES WITH AVERAGE STUDY HOURS (3.5hrs) ===")
# 1. Males who study AVERAGE and sleep MORE
avg_study_high_sleep = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] == 3.5) & 
    (data['sleep_hours'] > 6.7)
]
print(f"Number of males who study AVERAGE (3.5hrs) and sleep MORE (6.7-10hrs): {len(avg_study_high_sleep)}")

# 2. Males who study AVERAGE and sleep AVERAGE
avg_study_avg_sleep = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] == 3.5) & 
    (data['sleep_hours'].between(6.5, 6.7))
]
print(f"Number of males who study AVERAGE (3.5hrs) and sleep AVERAGE (6.5-6.7hrs): {len(avg_study_avg_sleep)}")

# 3. Males who study AVERAGE and sleep LESS
avg_study_low_sleep = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] == 3.5) & 
    (data['sleep_hours'] < 6.5)
]
print(f"Number of males who study AVERAGE (3.5hrs) and sleep LESS (3.5-6.5hrs): {len(avg_study_low_sleep)}")

print("\n=== MALES WITH LOW STUDY HOURS (<3.5hrs) ===")
# 1. Males who study LESS and sleep MORE
low_study_high_sleep = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] < 3.5) & 
    (data['sleep_hours'] > 6.7)
]
print(f"Number of males who study LESS (<3.5hrs) and sleep MORE (6.7-10hrs): {len(low_study_high_sleep)}")

# 2. Males who study LESS and sleep AVERAGE
low_study_avg_sleep = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] < 3.5) & 
    (data['sleep_hours'].between(6.5, 6.7))
]
print(f"Number of males who study LESS (<3.5hrs) and sleep AVERAGE (6.5-6.7hrs): {len(low_study_avg_sleep)}")

# 3. Males who study LESS and sleep LESS
low_study_low_sleep = data[
    (data['gender'] == 'Male') & 
    (data['study_hours_per_day'] < 3.5) & 
    (data['sleep_hours'] < 6.5)
]
#print(f"Number of males who study LESS (<3.5hrs) and sleep LESS (3.5-6.5hrs): {len(low_study_low_sleep)}")

#print("\n=== ANALYSIS OF TOP PERFORMERS BY GENDER ===")

# Find the highest scoring male and female students
top_male = data[data['gender'] == 'Male'].nlargest(1, 'exam_score')
top_female = data[data['gender'] == 'Female'].nlargest(1, 'exam_score')

# Analyze top male student
#print("\nTOP MALE STUDENT:")
#print(f"Exam Score: {top_male['exam_score'].values[0]}")
#print(f"Study Hours: {top_male['study_hours_per_day'].values[0]} hours")
#print(f"Sleep Hours: {top_male['sleep_hours'].values[0]} hours")

# Categorize top male's habits
male_study_category = (
    "MORE" if top_male['study_hours_per_day'].values[0] > 3.5
    else "AVERAGE" if top_male['study_hours_per_day'].values[0] == 3.5
    else "LESS"
)

male_sleep_category = (
    "MORE" if top_male['sleep_hours'].values[0] > 6.7
    else "AVERAGE" if 6.5 <= top_male['sleep_hours'].values[0] <= 6.7
    else "LESS"
)

#print(f"Study Pattern: {male_study_category}")
#print(f"Sleep Pattern: {male_sleep_category}")

# Analyze top female student
#print("\nTOP FEMALE STUDENT:")
#print(f"Exam Score: {top_female['exam_score'].values[0]}")
#print(f"Study Hours: {top_female['study_hours_per_day'].values[0]} hours")
#print(f"Sleep Hours: {top_female['sleep_hours'].values[0]} hours")

# Categorize top female's habits
female_study_category = (
    "MORE" if top_female['study_hours_per_day'].values[0] > 3.5
    else "AVERAGE" if top_female['study_hours_per_day'].values[0] == 3.5
    else "LESS"
)

female_sleep_category = (
    "MORE" if top_female['sleep_hours'].values[0] > 6.7
    else "AVERAGE" if 6.5 <= top_female['sleep_hours'].values[0] <= 6.7
    else "LESS"
)

#print(f"Study Pattern: {female_study_category}")
#print(f"Sleep Pattern: {female_sleep_category}")

#CONCLUSION: It turns out that the male sutdy more and sleep more to get a very high score.
#...while the females study more and sleep less to get a very high score.

#QUESTION 21: Are students with full parental education support more likely to have part-time jobs?
description_parental_education = pd.Categorical(data['parental_education_level']).describe()
#print("\nParental Education Level Categories:")
#print(description_parental_education)

#chcking students with part-time jobs
students_with_jobs = data[data['part_time_job'] == 'Yes']
students_with_jobs_count = students_with_jobs.shape[0]
#print(f"\nNumber of students with part-time jobs: {students_with_jobs_count}")

# checking the number of sudents with part-time jobs and have parents with Bachelor, High School and Master
#students_job_pSupport = (data[data['part_time_job'] == 'Yes']) & ([data['parental_education_level'] != 'NaN'])
#print(f"NUMBER OF PARTIME STUDENTS WHOES PARENTS ARE EDUCATED ARE: {len(students_job_pSupport)}")

# Analyze students with part-time jobs by parental education level
students_job_education = data[
    (data['part_time_job'] == 'Yes') & 
    (data['parental_education_level'].notna())
].groupby('parental_education_level').size()

#print("\nStudents with part-time jobs by parental education:")
#print(students_job_education)

total_working_students = data['part_time_job'].value_counts()['Yes']
education_percentages = (students_job_education / total_working_students * 100).round(1)

#print("\nPercentage distribution:")
#print(education_percentages)
#print(f"\nTotal working students with educated parents: {students_job_education.sum()}")


#find the percent of studets with partime job , with parenst with education and  with the highest exam scores
job_pEdu_student_perform = data[(data['part_time_job'] == 'Yes') & (data['parental_education_level'].notna()) & (data['exam_score'] >= 80 )]
#print(f" student with partime job and parent edu support who score 80 and above:{len(job_pEdu_student_perform)}")

#print("\n=== HIGH ACHIEVERS WITH PART-TIME JOBS AND EDUCATED PARENTS ===")

# Find students meeting all criteria
job_pEdu_student_perform = data[
    (data['part_time_job'] == 'Yes') & 
    (data['parental_education_level'].notna()) & 
    (data['exam_score'] >= 80)
]

# Calculate total count and percentage
total_students = len(data)
qualifying_students = len(job_pEdu_student_perform)
percentage = (qualifying_students / total_students) * 100

#print(f"Students with part-time job, educated parents, and high scores (≥80): {qualifying_students}")
#print(f"Percentage of total student population: {percentage:.2f}%")

# Calculate average scores more accurately
average_scores = {
    'exam_score': job_pEdu_student_perform['exam_score'].mean(),
    'attendance': job_pEdu_student_perform['attendance_percentage'].mean(),
    'study_hours': job_pEdu_student_perform['study_hours_per_day'].mean()
}

#print("\nTheir average performance metrics:")
#print(f"Exam Score: {average_scores['exam_score']:.2f}")
#print(f"Attendance: {average_scores['attendance']:.2f}%")
#print(f"Study Hours: {average_scores['study_hours']:.2f} hours/day")

#Conclution: OUt of 196 students whoes parents has eductaion satificate...
#..only 53 (5.30% of poppulation) have a better achievements in class.
#Parental education don't realy affect accademiccs performance.

#QUESTION 22: Does job status (working vs non-working) significantly affect sleep duration?
num_student_workers = data[data['part_time_job'] == 'Yes'].shape[0]
num_student_non_workers = data[data['part_time_job'] == 'No'].shape[0]
#print(f"\nNumber of working students: {num_student_workers}")
#print(f"Number of non-working students: {num_student_non_workers}")
# Calculate average sleep hours for working and non-working students
avg_sleep_working = data[data['part_time_job'] == 'Yes']['sleep_hours'].mean()
avg_sleep_non_working = data[data['part_time_job'] == 'No']['sleep_hours'].mean()
#print(f"\nAverage sleep hours for working students: {avg_sleep_working:.2f} hours")
#print(f"Average sleep hours for non-working students: {avg_sleep_non_working:.2f} hours")
#calculate the maximum and minimum sleep hours for both groups
max_sleep_working = data[data['part_time_job'] == 'Yes']['sleep_hours'].max()
max_sleep_non_working = data[data['part_time_job'] == 'No']['sleep_hours'].max()
#print(f"\nMaximum sleep hours for working students: {max_sleep_working:.2f} hours")
#print(f"Maximum sleep hours for non-working students: {max_sleep_non_working:.2f} hours")

min_sleep_working = data[data['part_time_job'] == 'Yes']['sleep_hours'].min()
min_sleep_non_working = data[data['part_time_job'] == 'No']['sleep_hours'].min()
#print(f"\nMinimum sleep hours for working students: {min_sleep_working:.2f} hours")
#print(f"Minimum sleep hours for non-working students: {min_sleep_non_working:.2f} hours")
#CONCLUSION: its seems working or not working dont realy affect sleping partern.

#QUESTION 23. What is the impact of screen time on sleep quality and exam performance?
#step 1: calculate the total screen time.
total_screen_time = data['social_media_hours'] + data['netflix_hours']
#print(f"\nTotal screen time (Social Media + Netflix): {total_screen_time.mean():.2f} hours/day")

# Calculate screen time for average-performing students
average_performers = data[(data['exam_score'] >= 50) & (data['exam_score'] < 80)]
average_performers_screen_time = average_performers['social_media_hours'] + average_performers['netflix_hours']

#print(f"Number of average performers: {len(average_performers)}")
#print(f"Average daily screen time: {average_performers_screen_time.mean():.2f} hours")
#print(f"Maximum screen time: {average_performers_screen_time.max():.2f} hours")
#print(f"Minimum screen time: {average_performers_screen_time.min():.2f} hours")
# Optional: Show distribution of screen time
#print("\nScreen time distribution for average performers:")
#print(average_performers_screen_time.describe().round(2))

#calculating that of high_performing students
high_performers = data[data['exam_score'] >= 80]
high_performers_screen_time = high_performers['social_media_hours'] + high_performers['netflix_hours']

#print(f"Number of high performers: {len(high_performers)}")
#print(f"Average daily screen time: {high_performers_screen_time.mean():.2f} hours")
#print(f"Maximum screen time: {high_performers_screen_time.max():.2f} hours")
#print(f"Minimum screen time: {high_performers_screen_time.min():.2f} hours")
# Optional: Show distribution of screen time
#print("\nScreen time distribution for high performers:")
#print(high_performers_screen_time.describe().round(2))

#calculating that of low-performing students
low_performers = data[data['exam_score'] <= 50]
low_performers_screen_time = low_performers['social_media_hours'] + low_performers['netflix_hours']

#print("\n=== SCREEN TIME ANALYSIS FOR LOW PERFORMERS (Score ≤50) ===")
#print(f"Number of low performers: {len(low_performers)}")
#print(f"Average daily screen time: {low_performers_screen_time.mean():.2f} hours")
#print(f"Maximum screen time: {low_performers_screen_time.max():.2f} hours")
#print(f"Minimum screen time: {low_performers_screen_time.min():.2f} hours")

# Show distribution of screen time
#print("\nScreen time distribution for low performers:")
#print(low_performers_screen_time.describe().round(2))

# Create subplots for screen time distribution
plt.figure(figsize=(15, 5))

# Histogram for low performers
plt.subplot(131)
sns.histplot(data=low_performers_screen_time, bins=20, color='red', alpha=0.6)
plt.title('Low Performers\nScreen Time Distribution')
plt.xlabel('Screen Hours/Day')
plt.ylabel('Number of Students')

# Histogram for average performers
plt.subplot(132)
sns.histplot(data=average_performers_screen_time, bins=20, color='blue', alpha=0.6)
plt.title('Average Performers\nScreen Time Distribution')
plt.xlabel('Screen Hours/Day')

# Histogram for high performers
plt.subplot(133)
sns.histplot(data=high_performers_screen_time, bins=20, color='green', alpha=0.6)
plt.title('High Performers\nScreen Time Distribution')
plt.xlabel('Screen Hours/Day')

# Add vertical lines for mean values
plt.axvline(x=low_performers_screen_time.mean(), color='red', linestyle='--', alpha=0.8)
plt.axvline(x=average_performers_screen_time.mean(), color='blue', linestyle='--', alpha=0.8)
plt.axvline(x=high_performers_screen_time.mean(), color='green', linestyle='--', alpha=0.8)

plt.tight_layout()
#plt.show()

#print("\n=== SCREEN TIME SUMMARY ===")
#print(f"Low Performers (≤50):")
#print(f"Mean: {low_performers_screen_time.mean():.2f} hours")
#print(f"Max: {low_performers_screen_time.max():.2f} hours")
#print(f"Min: {low_performers_screen_time.min():.2f} hours")

#print(f"\nAverage Performers (50-79):")
##print(f"Mean: {average_performers_screen_time.mean():.2f} hours")
#print(f"Max: {average_performers_screen_time.max():.2f} hours")
#print(f"Min: {average_performers_screen_time.min():.2f} hours")

#print(f"\nHigh Performers (≥80):")
#print(f"Mean: {high_performers_screen_time.mean():.2f} hours")
#print(f"Max: {high_performers_screen_time.max():.2f} hours")
#print(f"Min: {high_performers_screen_time.min():.2f} hours") 
#CONCLUSION: Screen time affects accademics performance. reducing screen time that will boost accademic perfomane

#QUESTION 24. How do male and female students differ in average study hours per week?
# Calculate average study hours for males
average_study_male = data[data['gender'] == 'Male']['study_hours_per_day'].mean()
#print(f"Average male study time: {average_study_male:.2f} hours/day")

# Calculate average study hours for females
average_study_female = data[data['gender'] == 'Female']['study_hours_per_day'].mean()
#print(f"Average female study time: {average_study_female:.2f} hours/day")

# Show the difference
difference = abs(average_study_male - average_study_female)
#print(f"Difference in study time: {difference:.2f} hours/day")
#CONCLUSION: Female tends to study more than the Male with just 0.07hrs/day in difference

#QUESTION 25. What is the average exam score for students who use social media less than 2 hours?
#print("\n=== EXAM SCORES FOR STUDENTS WITH LOW SOCIAL MEDIA USE (<2 hours) ===")

# Filter students with less than 2 hours of social media
low_social_media = data[data['social_media_hours'] < 2]

# Calculate statistics
stats = {
    'average_score': low_social_media['exam_score'].mean(),
    'count': len(low_social_media),
    'max_score': low_social_media['exam_score'].max(),
    'min_score': low_social_media['exam_score'].min()
}

# Print results
#print(f"Number of students using social media <2 hours: {stats['count']}")
#print(f"Average exam score: {stats['average_score']:.2f}")
#print(f"Highest score: {stats['max_score']:.2f}")
#print(f"Lowest score: {stats['min_score']:.2f}")

# Optional: Compare with overall average
overall_average = data['exam_score'].mean()
difference = stats['average_score'] - overall_average
#print(f"\nComparison to overall average:")
#print(f"Overall average exam score: {overall_average:.2f}")
#print(f"Difference: {difference:.2f} points")

#print("\n=== ANALYSIS OF STUDENTS WITH LOW SOCIAL MEDIA USE (<2 hours) ===")

# Filter students with less than 2 hours social media use
low_social_media_users = data[data['social_media_hours'] < 2]

# Calculate exam score distribution
exam_stats = low_social_media_users['exam_score'].describe().round(2)
#print("\nExam Score Statistics for Low Social Media Users:")
#print(exam_stats)

# Calculate high performers among low social media users
high_performers = low_social_media_users[low_social_media_users['exam_score'] >= 80]
high_performers_percentage = (len(high_performers) / len(low_social_media_users)) * 100

#print(f"\nDetails for students using social media <2 hours:")
#print(f"Total students with low social media use: {len(low_social_media_users)}")
#print(f"Number scoring 80 or above: {len(high_performers)}")
#print(f"Percentage scoring 80 or above: {high_performers_percentage:.2f}%")

# Compare with overall class average
overall_average = data['exam_score'].mean()
low_social_difference = low_social_media_users['exam_score'].mean() - overall_average
#print(f"\nComparison to class average:")
#print(f"Low social media users average: {low_social_media_users['exam_score'].mean():.2f}")
#print(f"Overall class average: {overall_average:.2f}")
#print(f"Difference: {low_social_difference:.2f} points")
#CONCLUSION: Over 39.29 percent score 80 percent and above in class. average score is 73.94

#QUESTION 26. How many students fall into low, medium, and high score categories?
#print("\n=== STUDENT PERFORMANCE CATEGORIES ===")

# Define score categories
score_bins = [0, 50, 79, 100]
score_labels = ['Low (0-50)', 'Medium (51-79)', 'High (80-100)']

# Categorize students
data['score_category'] = pd.cut(data['exam_score'], 
                              bins=score_bins, 
                              labels=score_labels, 
                              include_lowest=True)

# Calculate distribution
score_distribution = data['score_category'].value_counts().sort_index()
percentages = (score_distribution / len(data) * 100).round(2)

# Print results
#print("\nNumber of students in each category:")
#for category, count in score_distribution.items():
    #print(f"{category}: {count} students ({percentages[category]}%)")

# Show basic statistics for each category
#print("\nAverage scores by category:")
#for category in score_labels:
    #avg = data[data['score_category'] == category]['exam_score'].mean()
    #print(f"{category}: {avg:.2f}")

#CONCLUSION: 131 students fall under low. 583 fall under medium . 286 fall under high.
#student are doing well.

#QUESTION 27. What lifestyle combination yields top 10% results?
#print("\n=== LIFESTYLE ANALYSIS OF TOP 10% PERFORMERS ===")

# Calculate the 90th percentile score to identify top 10%
top_score_threshold = data['exam_score'].quantile(0.9)
top_performers = data[data['exam_score'] >= top_score_threshold]

# Calculate lifestyle metrics
lifestyle_stats = {
    # Academic Habits
    'Study Hours': top_performers['study_hours_per_day'].mean(),
    'Attendance': top_performers['attendance_percentage'].mean(),
    
    # Screen Time
    'Social Media Hours': top_performers['social_media_hours'].mean(),
    'Netflix Hours': top_performers['netflix_hours'].mean(),
    'Total Screen Time': top_performers['social_media_hours'].add(top_performers['netflix_hours']).mean(),
    
    # Health Factors
    'Sleep Hours': top_performers['sleep_hours'].mean(),
    'Exercise Frequency': top_performers['exercise_frequency'].mean(),
}

# Calculate participation percentages
participation_stats = {
    'Extracurricular': (top_performers['extracurricular_participation'] == 'Yes').mean() * 100,
    'Part-time Job': (top_performers['part_time_job'] == 'Yes').mean() * 100
}

# Diet quality distribution
diet_distribution = top_performers['diet_quality'].value_counts(normalize=True) * 100

# Print results
print(f"\nTop 10% Score Threshold: {top_score_threshold:.2f}")
print(f"Number of top performers: {len(top_performers)}")
print(f"Average exam score: {top_performers['exam_score'].mean():.2f}")

#print("\nDAILY HABITS:")
print(f"• Study: {lifestyle_stats['Study Hours']:.2f} hours")
print(f"• Sleep: {lifestyle_stats['Sleep Hours']:.2f} hours")
print(f"• Screen time: {lifestyle_stats['Total Screen Time']:.2f} hours")
print(f"• Attendance: {lifestyle_stats['Attendance']:.2f}%")

#print("\nPARTICIPATION RATES:")
print(f"• Extracurricular activities: {participation_stats['Extracurricular']:.1f}%")
print(f"• Part-time work: {participation_stats['Part-time Job']:.1f}%")

print("\nHEALTH METRICS:")
print(f"• Exercise frequency: {lifestyle_stats['Exercise Frequency']:.2f}")

#RANKING THEM
print("\n=== TOP 10 LIFESTYLE FACTORS RANKED BY EFFECTIVENESS ===")

# Get top 10% performers
top_score_threshold = data['exam_score'].quantile(0.9)
top_performers = data[data['exam_score'] >= top_score_threshold]

# Calculate all metrics as percentages or averages (excluding categorical data)
metrics = {
    'Attendance Rate': top_performers['attendance_percentage'].mean(),
    'Study Hours': top_performers['study_hours_per_day'].mean(),
    'Sleep Quality': top_performers['sleep_hours'].mean(),
    'Exercise Frequency': top_performers['exercise_frequency'].mean(),
    'Extracurricular': (top_performers['extracurricular_participation'] == 'Yes').mean() * 100,
    'Part-time Work': (top_performers['part_time_job'] == 'Yes').mean() * 100,
    'Diet Quality': top_performers['diet_quality'].map({'Poor': 1, 'Average': 2, 'Good': 3}).mean(),
    'Mental Health': top_performers['mental_health_rating'].mean(),
    'Screen Time Control': 24 - (top_performers['social_media_hours'] + top_performers['netflix_hours']).mean(),
}

# Sort metrics by their values
sorted_metrics = dict(sorted(metrics.items(), keylambda= x: x[1], reverse=True))

print(f"\nTop performers threshold score: {top_score_threshold:.2f}")
print(f"Number of top performers analyzed: {len(top_performers)}")
print("\nTOP LIFESTYLE FACTORS RANKED BY EFFECTIVENESS:")
print("-" * 50)
for i, (factor, value) in enumerate(sorted_metrics.items(), 1):
    print(f"{i}. {factor:<20}: {value:.2f}")

#checking internet quality 
print("\nINTERNET QUALITY RATE")
print("-" * 50)
print("Internet Quality Distribution:")
internet_dist = top_performers['internet_quality'].value_counts(normalize=True) * 100
for quality, percentage in internet_dist.items():
    print(f"• {quality}: {percentage:.1f}%")


#CONCLUSION: the lifestyle that yealds top 10% results is the attendance rate...
#...as it makes maximum effect on accademic performance that the rest