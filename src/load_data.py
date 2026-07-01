import pandas as pd
# load csv file
df = pd.read_csv("data/student_dataset_v2.csv")
#First 5 rows of the dataframe
print("First 5 rows of the dataframe:", df.head())

#Last 5 rows of the dataframe
print("Last 5 rows of the dataframe:", df.tail())

# Shape of the dataframe
print("Shape of the dataframe:", df.shape)

# Column names of the dataframe
print("Column names of the dataframe:", df.columns.tolist())

# Data types of the columns
print("Data types of the columns:", df.dtypes)


