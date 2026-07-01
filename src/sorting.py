import pandas as pd

# Load transformed dataset
df = pd.read_csv("output/transformed_data.csv")

# 1. Students sorted by Marks (Highest to Lowest)
sorted_marks = df.sort_values(by="Marks", ascending=False)

print("Students Sorted by Marks")
print(sorted_marks.head())

# Save file
sorted_marks.to_csv("output/sorted_by_marks.csv", index=False)


# 2. Students sorted by Attendance (Highest to Lowest)
sorted_attendance = df.sort_values(by="Attendance", ascending=False)

print("\nStudents Sorted by Attendance")
print(sorted_attendance.head())

# Save file
sorted_attendance.to_csv("output/sorted_by_attendance.csv", index=False) 


# 3. Students sorted by Study Hours (Highest to Lowest)
sorted_study = df.sort_values(by="StudyHours", ascending=False)
#yha jo false hai wai descending order mai data ko print karayegi 
#or iskai through hm pehle highest find karenge and then lowest 

print("\nStudents Sorted by Study Hours")
print(sorted_study.head())

# Save file
sorted_study.to_csv("output/sorted_by_studyhours.csv", index=False)

print("\nSorting Completed Successfully")