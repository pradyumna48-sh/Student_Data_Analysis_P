import pandas as pd

# Load transformed dataset
df = pd.read_csv("output/transformed_data.csv")

# Average Marks by Grade
average_marks = df.groupby("Grade")["Marks"].mean()
print("Average Marks by Grade:\n", round(average_marks, 2))

# Number of Students in Each Grade
student_count = df.groupby("Grade")["Grade"].count()
print("Number of Students in Each Grade:", student_count)

# Average Attendance by Grade
average_attendance = df.groupby("Grade")["Attendance"].mean()
print("Average Attendance by Grade:", round(average_attendance, 2))

#file save 
average_marks.to_csv("output/grade_average_marks.csv")

student_count.to_csv("output/grade_student_count.csv")

average_attendance.to_csv("output/grade_average_attendance.csv")

print("\nGrouping Data Saved Successfully")

