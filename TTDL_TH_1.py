import pandas as pd
import numpy as np
df = pd.read_csv("shopeep_koreantop_clothing_shop_data.csv")

# Để đơn giản ta thực hiện lọc tập dữ liệu ban đầu theo các thuộc tính sau
df = df[["join_month",'join_day','join_year','shop_location','rating_bad','rating_good','rating_normal']]
print(df.info())
# print(df.columns)
print("*"*20)

# Tạo cột mới "rating" dựa vào các cột cho trước có kiểu dữ lệu số thông qua tính toán
df["rating"] = df["rating_good"]*2+df["rating_normal"]-3*df["rating_bad"]
# print(df.columns)

# Tạo cột mới từ các cột có kiểu dữ liệu chuỗi, chuyển từ int sang str dùng astype()
df["date"] = df["join_month"] +" " + df["join_day"].astype(str)+"-"+df["join_year"].astype(str)

# Thêm cột new nhận giá trị boolen, True nếu "join_year"==2021 - False nếu "join_year"!=2021
df["new"]=df["join_year"]==2021

##### Tạo cột mới với giá trị cột mới phụ thuộc vào điều kiện
# Nếu có hai lựa chọn sử dụng hàm where ở pagkage numpy
# Thêm cột rate có giá trị good nếu rating_good >= 50000,  bad trong trường hợp còn lại
df["rate"] = np.where(df["rating_bad"]>=50000,"good","bad")
# print(df)

# Nếu có nhiều hơn 2 giá trị sử dụng hàm select của numpy
# Thêm cột flag tặng cờ cho các cửa hàng, flag nhận các giá trị như sau:
# blue khi rating_good >= 30000 và rating_bad <= 100
# yellow khi 10000 <= rating_good < 30000 và 100 < rating_bad <= 1000
# red khi rating_good < 10000
# black đối với các trường hợp còn lại
conditions = [(df["rating_good"]>=30000) & (df["rating_bad"]<=100),
(df["rating_good"]<30000)&(df["rating_good"]>=10000)&(df["rating_bad"]>100)&(df["rating_bad"]<=1000), (df["rating_good"]<10000)]
choices = ["blue","yellow","red"]
df["flag"] = np.select(conditions, choices, default = "black")
print(df)







