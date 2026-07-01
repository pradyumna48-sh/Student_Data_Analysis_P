import pandas as pd

# Load transformed dataset
df = pd.read_csv("output/transformed_data.csv")

# Export Final Dataset
df.to_csv("output/final_student_dataset.csv", index=False)

print("Final Dataset Exported Successfully")