import pandas as pd

# Load transformed dataset
df = pd.read_csv("output/transformed_data.csv")

# Open report file
report = open("output/report.txt", "w")

report.write("STUDENT DATA ANALYSIS REPORT\n")
report.write("=" * 35 + "\n\n")

report.write(f"Total Students : {len(df)}\n")
report.write(f"Average Marks : {round(df['Marks'].mean(),2)}\n")
report.write(f"Highest Marks : {df['Marks'].max()}\n")
report.write(f"Lowest Marks : {df['Marks'].min()}\n")
report.write(f"Average Attendance : {round(df['Attendance'].mean(),2)}\n")
report.write(f"Average Study Hours : {round(df['StudyHours'].mean(),2)}\n")

report.close()

print("Report Generated Successfully")