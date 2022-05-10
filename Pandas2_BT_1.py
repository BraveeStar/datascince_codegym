#YC1: ọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
import pandas as pd
import numpy as np
df =  pd.read_csv("GDPlist.csv",encoding ="ISO-8859-1")
print("Số dòng bộ dữ liệu là:",df.shape[0],"\nSố cột của bộ dữ liệu là:",df.shape[1])
print("Kiểu dữ liệu của cột Country:",df["Country"].dtype)
print("Kiểu dữ liệu của cột Continent:",df["Continent"].dtype)
print("Kiểu dữ liệu của cột GDP (millions of US$):",df["GDP (millions of US$)"].dtype)

#YC2: Tính giá trị lớn nhất và giá trị nhỏ nhất của GDP
print("Giá trị lớn nhất của GDP là:",df["GDP (millions of US$)"].max())

# #YC3: Hãy cho biết xu hướng phân bố dữ liệu của GDP.
print(df.describe())


# YC4: Hãy cho biết châu lục nàu xuất nhiện nhiều nhất
target = df.groupby(by="Continent").count()
target = df["Continent"].mode()
print("Châu lục xuất hiện nhiều nhất là:",target)

# YC5: Với mỗi châu lục tổng GDP, trung bình cộng GDP, 
# tagert = df.groupby(by="Continent").
table_tong_GDP = df.pivot_table(values="GDP (millions of US$)",index="Continent",aggfunc = "sum")
table_tong_GDP.rename(columns={"GDP (millions of US$)":"Tông GDP"},inplace=True)
table_tb_GDP = df.pivot_table(values="GDP (millions of US$)",index="Continent",aggfunc = "mean")
table_tb_GDP.rename(columns={"GDP (millions of US$)":"TBC GDP"},inplace=True)
table_total = pd.concat([table_tong_GDP,table_tb_GDP],axis=1)
print(table_total)





