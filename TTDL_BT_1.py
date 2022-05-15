# YC1: Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
import pandas as pd 
import numpy as np
df = pd.read_excel("house_price_dong-da.xlsx")
# print("Số dòng của file data là:",df.shape[0],"\nSố cột của file data là:",df.shape[1])
# print(df.info())

# YC2: Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
# df = df[(df["ward_name"]=="Phường Trung Liệt")|(df["ward_name"]=="Phường Khâm Thiên")]
# print(df["ward_name"].value_counts())

print(df.columns)

# Yc3: Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
# df = df[(df["land_certificate"]!=np.nan)&(df["bedroom"]>=3)].reset_index()
# target = df.loc[:,["address","price","house_direction","balcony_direction"]]
# target = df[["address","price","house_direction","balcony_direction"]]
# print(target)

# YC4: Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
print(df[df["type_of_land"]=="Bán nhà mặt phố\n"])
# df["type_of_land"].replace({"Bán nhà mặt phố\n":"Bán nhà mặt phố","Bán nhà riêng\n":"Bán nhà riêng","Bất động sản khác\n":"Bất động sản khác"},inplace=True)
print(df["type_of_land"].value_counts())
mean_price = df.groupby(by="type_of_land")["price"].mean()
max_price = df.groupby(by="type_of_land")["price"].max()
min_price = df.groupby(by="type_of_land")["price"].min()
table_4 = df.pivot_table(values = "price",index = "type_of_land",aggfunc=["mean","max","min"])
print(table_4)

# YC5: Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
# table_5 = df.pivot_table(values=["bedroom","toilet","floor"],index="ward_name",aggfunc={"bedroom":"mean","toilet":"mean","floor":"mean"})
# print(table_5)