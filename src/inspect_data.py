import pandas as pd

# load csv file
df = pd.read_csv("data/student_dataset_v2.csv")

#Missing values in the dataframe
print("Missing values in the dataframe:", df.isnull().sum())

#Duplicate rows in the dataframe
print("Duplicate rows in the dataframe:", df.duplicated().sum())

#Summary statistics of the dataframe
print("Summary statistics of the dataframe:", df.describe(include='all'))

#Memory usage of the dataframe
print("Memory usage of the dataframe:", df.memory_usage(deep=True))

#Information about the dataframe
print("Information about the dataframe:",df.info())



 
