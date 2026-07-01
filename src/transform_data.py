import pandas as pd

df = pd.read_csv("output/cleaned_data.csv")
# Result 
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

#Grade 
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)

#Performance 
def performance(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    elif marks >= 50:
        return "Average"
    else:
        return "Poor"

df["PerformanceScore"] = df["Marks"].apply(performance)
df.to_csv("output/transformed_data.csv", index=False)

print("Data Transformation Completed Successfully")
