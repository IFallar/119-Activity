import os
import pandas as pd
import researchpy as rp

# Determine current directory
print("\n")
print(os.getcwd())
print("\n")

# Open file: "ExperimentTwo.xlsx"
df = pd.read_excel("ExperimentTwo.xlsx")

# Viewing the dataframe
print(df)
print("\n\n")


# Viewing the first 7 rows
print(df.head(7))
print("\n\n")

# Viewing the last 7 rows
print(df.tail(7))
print("\n\n")


# SLICING THE DATAFRAME

# Slice the second column with all of its observations
print(df.iloc[:, 1])
print("\n\n")


# Slice the data frame to only include observations ID of 5 to 20
print(df.iloc[4:20, :])
print("\n\n")


# Slice DF to only include column ID and pretest with observation ID 7 to 25
print(df.iloc[6:25, :2])
print("\n\n")


# Checking the structure of the dataframe
print(df.info())
print("\n\n")


# Checking for NAs or missing cases
print(df.isnull().values.any())
print("\n\n")


# Getting a simple Descriptives
print(df.iloc[:, 1].describe())
print("\n\n")

# MACHINE PROBLEM 2

# Loading .Sav file and assigning it to a variable
# Open and work on "sales.sav"
df = pd.read_spss("sales.sav")

# Viewing the dataframe
print(df)
print("\n\n")

# Viewing the first 15 rows
print(df.head(15))
print("\n\n")

# Viewing the last 15 rows
print(df.tail(15))
print("\n\n")

# Checking the structure of the dataframe
print(df.info())
print("\n\n")

# Slicing the dataframe

# Slice column to include 'hiqualty', 'satinfo', 'salesrep' with all of its observations
print(df.loc[:, ['hiqualty', 'satinfo', 'salesrep']])
print("\n\n")

# Slice the data frame to only include observations index of 15 to 35
print(df.iloc[15:36])
print("\n\n")

# Change the column named 'hiqualty' to 'hiquality'
df = df.rename(columns={'hiqualty': 'hiquality'})
print("\n\n")

# Checking for NAs or missing cases
print(df.isnull().values.any())
print("\n\n")

# Subset dataframe to include all rows with missing cases
missing_df = df[df.isnull().any(axis=1)]
print(missing_df)
print("\n\n")

# Subset dataframe to include all rows with complete cases
complete_df = df[df.notnull().all(axis=1)]
print(complete_df)
print("\n\n")

# Getting a simple Descriptives
print(df.describe())
print("\n\n")

print(df.astype('object').describe())

