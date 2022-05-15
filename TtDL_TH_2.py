# Thực hành tách dữu liệu của một cột thành nhiều cột
import pandas as pd
from datetime import datetime
df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")
# lọc dữ liệu thành bảng dữ liệu mới với một số thuộc tính
# print(df.columns)
df = df[["date_collected","shop_location","response_time"]]
# print(df.head())

# Tách cột shop_location thành hai cột District và city
df["Dictrict"] = df["shop_location"].str.split(",").str[0]
df["City"] = df["shop_location"].str.split(",").str[1]


# Tách cột dữ liệu có kiểu ngày tháng, thời gian
# df["Day"] = df["date_collected"].str.split("-").str[2]
df["Day"] = pd.to_datetime(df["date_collected"],format = "%Y-%m-%d").dt.day
df["Month"] = pd.to_datetime(df["date_collected"],format = "%Y-%m-%d").dt.month
df["Year"] = pd.to_datetime(df["date_collected"],format = "%Y-%m-%d").dt.year
df["Hour"] = pd.to_datetime(df["response_time"],format = " %H:%M:%S").dt.hour
df["Minute"] = pd.to_datetime(df["response_time"],format =  ' %H:%M:%S').dt.minute
df["Second"] = pd.to_datetime(df["response_time"],format = " %H:%M:%S").dt.second



