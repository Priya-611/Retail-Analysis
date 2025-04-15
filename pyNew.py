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

#EDA


#OBJECTIVES:->
#1 Examine monthly or yearly patterns in sales to identify peak periods and seasonal trends.

df_no_outliers["Year"]=df_no_outliers["Order Date"].dt.year
df_no_outliers["Month"]=df_no_outliers["Order Date"].dt.month_name()
#print(df_no_outliers)


month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

gb_m=df_no_outliers.groupby("Month")["Profit"].sum().reindex(month_order).reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(x="Month",y="Profit",data=gb_m,color='m')
plt.xticks(rotation=45)
plt.grid(True)
plt.title('Analyze Profit Trends Over Month')
plt.show(block=False)

gb_y=df_no_outliers.groupby("Year")["Profit"].sum().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(x="Year",y="Profit",data=gb_y,color='r')
plt.grid(True)
plt.title('Analyze Profit Trends Over Year')
plt.show()

#2 average profit per order across different regions to identify high and low-performing areas.



region_p=df_no_outliers.groupby("Region")["Profit"].mean().reset_index()
br=sns.barplot(x="Region",y="Profit",data=region_p,hue="Region",palette='dark:pink',legend=False)
br.bar_label(br.containers[0],fmt='%.2f')
br.bar_label(br.containers[1],fmt='%.2f')
br.bar_label(br.containers[2],fmt='%.2f')
br.bar_label(br.containers[3],fmt='%.2f')
plt.title('Average Sales across Region')
plt.grid(False)
plt.show()


