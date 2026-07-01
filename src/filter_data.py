import pandas as pd

# Load transformed dataset
df = pd.read_csv("output/transformed_data.csv")

# Top Performing Students
top_students = df[df["Marks"] >= 85]
top_students.to_csv("output/top_students.csv", index=False)

# Failed Students
failed_students = df[df["Result"] == "Fail"]
failed_students.to_csv("output/failed_students.csv", index=False)

# Attendance Below 75%
low_attendance = df[df["Attendance"] < 75]
low_attendance.to_csv("output/low_attendance.csv", index=False)

# Students Studying More Than 8 Hours
high_study = df[df["StudyHours"] > 8]
high_study.to_csv("output/high_study_hours.csv", index=False)

print("Filtering Completed Successfully")

print("\nTop Performing Students")
print(top_students.head())

print("\nFailed Students")
print(failed_students.head())

print("\nLow Attendance Students")
print(low_attendance.head())

print("\nHigh Study Hours Students")
print(high_study.head())