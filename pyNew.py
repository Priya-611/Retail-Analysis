import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  

file_path="C:\\Users\\HP\\OneDrive\\Documents\\Python programming(sem4)\\python files\\sample_-_superstore.xlsx"
df=pd.read_excel(file_path,sheet_name="Orders")
return_df=pd.read_excel(file_path,sheet_name="Returns")
# print(df)


print(df.head())
print(df.info())
print(df.isnull().sum())
print(df["Order ID"].duplicated().sum())


#CLEANING AND VISUALISATION

df.drop_duplicates(subset="Order ID",keep="first",inplace=True)
print(df["Order ID"].duplicated().sum())

df["Order Date"]=pd.to_datetime(df["Order Date"])
df["Ship Date"]=pd.to_datetime(df["Ship Date"])

print(df.columns)
numeric =["Quantity","Discount","Profit","Sales"]
df[numeric]=df[numeric].apply(pd.to_numeric)

df1=df[df["Profit"]>=0].copy()
print(df1)

# merging two sheet
df1=pd.merge(df1,return_df,on="Order ID",how="left")
print(df1)
df1["Returned"].replace(np.nan,"No",inplace=True)
print(df1)
print(df1.columns)

#removing outliers 

Q1 = df1["Profit"].quantile(0.25)
Q3 = df1["Profit"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_outliers = df1[(df1["Profit"] >= lower_bound) & (df1["Profit"] <= upper_bound)].copy()
print(df_no_outliers)

print(df_no_outliers.info())
print(df_no_outliers.describe())


