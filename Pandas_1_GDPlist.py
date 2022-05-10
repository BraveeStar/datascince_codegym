import pandas as pd
import numpy as np
df = pd.read_csv("GDPlist.csv",encoding = "ISO-8859-1")

### 1: Đọc bộ dữ liệu, cho biết số dòng số cột và các kiểu thuộc tính
# print("Số cột là:",df.shape[1],"\nSố dòng là:",df.shape[0])
print(df.info())

### 2: Vệt hóa các cột
df.rename(columns = {"Country":"Nuoc","Continent":"Chauluc","GDP (millions of US$)":"GDP (trieu $)"},inplace = True)
print(df.info())

# print(df["Nuoc"].to_list())
### 3: Chèn thêm một cột “Thanhpho” vào sau cột “Nuoc”, giá trị ban đầu là giá trị của cột “Nuoc”
# df.insert(1,"Thanhpho",pd.Series(df["Nuoc"].to_list(),index = df.index))
df.insert(1,"Thanhpho",df.loc[:,"Nuoc"])
# print(df.head())
### 4: Trong cột Thành phố thay việt nam thành hà nội
df["Thanhpho"].replace(" Vietnam","Hanoi",inplace = True)
# print(df.to_string)
print(df[df["Chauluc"]=="Asia"])
# print(df.loc[:,"Chauluc"=="Asia"])
df.drop(df[df["Chauluc"]=="Asia"].index,axis = 0, inplace = True)
print("*"*10)
# print(df["Chauluc"].value_counts())
df.drop(df[df["GDP (trieu $)"]<300000].index,axis = 0, inplace = True )
print(df)