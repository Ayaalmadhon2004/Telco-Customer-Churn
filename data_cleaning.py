# -------------------------
# 1️ Importing Libraries
print("\n========== 1️ Importing Libraries ==========")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("Libraries imported successfully!")

# -------------------------
# 2️ Reading the Dataset
print("\n========== 2️ Reading the Dataset ==========")
data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv") 
print("Dataset loaded successfully!")

# -------------------------
# 3️ General Information About the Data
print("\n========== 3️ General Information ==========")
print("Data shape before cleaning:", data.shape)
print("\nColumn information:")
print(data.info())
print("\nNumber of missing values per column:")
print(data.isnull().sum())

# -------------------------
# 4️ Cleaning the TotalCharges Column
print("\n========== 4️ Cleaning 'TotalCharges' Column ==========")
data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors='coerce')
data["TotalCharges"].fillna(data["TotalCharges"].mean(), inplace=True)
print("TotalCharges cleaned and missing values replaced with the mean.")

# -------------------------
# 5️ Removing Duplicate Rows
print("\n========== 5️ Removing Duplicate Rows ==========")
before = data.shape[0]
data.drop_duplicates(inplace=True)
after = data.shape[0]
print(f"Removed {before - after} duplicate rows.")

# -------------------------
# 6️ Dropping Unnecessary Columns
print("\n========== 6️ Dropping Unnecessary Columns ==========")
data.drop("customerID", axis=1, inplace=True)
print("Column 'customerID' has been removed.")

# -------------------------
# 7️ Checking Data After Cleaning
print("\n========== 7️ Checking Data After Cleaning ==========")
print("Data shape after cleaning:", data.shape)
print("Number of missing values after cleaning:\n", data.isnull().sum())
print("First 5 rows after cleaning:")
print(data.head())

# -------------------------
# 8️ Exploratory Data Analysis (EDA)
print("\n========== 8️ Churn Distribution ==========")
plt.figure(figsize=(6,4))
sns.countplot(x="Churn", data=data)
plt.title("Customer Distribution: Churn vs Not Churn")
plt.show()

print("\n========== 9️ Tenure vs Churn ==========")
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="tenure", data=data)
plt.title("Tenure vs Customer Churn")
plt.show()

print("\n========== 10️ TotalCharges vs Churn ==========")
plt.figure(figsize=(8,5))
sns.boxplot(x="Churn", y="TotalCharges", data=data)
plt.title("Total Charges vs Customer Churn")
plt.show()

# -------------------------
# 11 General Statistics for Numeric Columns
print("\n========== 11 General Statistics ==========")
print(data.describe())

# -------------------------
# 12 Checking Class Balance
print("\n========== 12 Checking Class Balance ==========")
print(data["Churn"].value_counts())
print("\nPercentage of each class:")
print(data["Churn"].value_counts(normalize=True))

# -------------------------
print("\n The dataset is now cleaned and ready for further analysis or building predictive models (ML).")
