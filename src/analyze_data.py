import pandas as pd

# Load transformed dataset
df = pd.read_csv("output/transformed_data.csv")

# Average Marks
average_marks = df["Marks"].mean()
print("Average Marks:", round(average_marks, 2))

# Highest Marks
highest_marks = df["Marks"].max()
print("Highest Marks:", highest_marks)

# Lowest Marks
lowest_marks = df["Marks"].min()
print("Lowest Marks:", lowest_marks)

# Average Attendance
average_attendance = df["Attendance"].mean()
print("Average Attendance:", round(average_attendance, 2))

# Average Study Hours
average_study_hours = df["StudyHours"].mean()
print("Average Study Hours:", round(average_study_hours, 2))

# Pass Percentage
pass_percentage = (df["Result"] == "Pass").mean() * 100
print("Pass Percentage:", round(pass_percentage, 2), "%")

# Fail Percentage
fail_percentage = (df["Result"] == "Fail").mean() * 100
print("Fail Percentage:", round(fail_percentage, 2), "%")

# Grade Distribution
grade_distribution = df["Grade"].value_counts()

print("\nGrade Distribution")
print(grade_distribution)