import pandas as pd 
#load file 
df = pd.read_csv("output/transformed_data.csv")

#mean
print("Mean:", df.mean(numeric_only=True))
#mean file save 
df.mean(numeric_only=True).to_csv("output/mean.csv")

#median
print("Median:", df.median(numeric_only=True))
#median file save 
df.median(numeric_only=True).to_csv("output/median.csv")

#mode
print("Mode:", df.mode())
#mode file save 
df.mode().to_csv("output/mode.csv", index=False)


#standard deviation
print("Standard Deviation:", df.std(numeric_only=True))
#standard deviation file save 
df.std(numeric_only=True).to_csv("output/standard_deviation.csv")

#variance
print("Variance:", df.var(numeric_only=True))
#variance file save 
df.var(numeric_only=True).to_csv("output/variance.csv")

#matrix 
print("Correlation Matrix:\n", df.corr(numeric_only=True))
#matrix file save 
df.corr(numeric_only=True).to_csv("output/correlation_matrix.csv")

