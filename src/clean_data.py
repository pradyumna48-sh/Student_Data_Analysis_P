import pandas as pd


# Load dataset
df = pd.read_csv("data/student_dataset_v2.csv")

# 1. Remove duplicate records
df.drop_duplicates(inplace=True)

# 2. Handle missing values
# Numeric columns ke missing values mean se fill
df["Marks"] = df["Marks"].fillna(df["Marks"].mean().round(2))

# 3. Remove invalid entries

# Validate attendance values
df = df[df["Attendance"].between(0, 100)]

# Validate study hours
df = df[df['StudyHours'].between(0, 24)]

# Validate marks
df = df[df['Marks'].between(0, 100)]

# Save cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)

print("\nData Cleaning Completed Successfully")

