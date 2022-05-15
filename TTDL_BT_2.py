# YC1: Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
import pandas as pd
import numpy as np
df = pd.read_csv("OnlineRetail.csv",encoding="ISO-8859-1")
# print("Số dòng của file data là:",df.shape[0],"\nSố cột của file data là:",df.shape[1])
print(df.info())

# YC2: Tạo cột mới có tên quý –  ‘Previous’ nhận giá trị 1 nếu ngày lập hóa đơn nằm trong các tháng 1,2,3; nhận giá trị 2 nếu ngày lập hóa đơn nằm trong các tháng 4,5,6; nhận giá trị 3 nếu ngày lập hóa đơn nằm trong các tháng 7,8,9;  nhận giá trị 4 nếu ngày lập hóa đơn nằm trong các tháng 10,11,12;
df["Date"] = pd.to_datetime(df["InvoiceDate"],format="%m/%d/%Y %H:%M").dt.day
conditions = [(df["Date"]==1)|(df["Date"]==2)|(df["Date"]==3),(df["Date"]== 4)|(df["Date"]==5)|(df["Date"]==6),(df["Date"]==7)|(df["Date"]==8)|(df["Date"]==9),(df["Date"]==10)|(df["Date"]==11)|(df["Date"]==12)]
choices= [1,2,3,4]
df["Previous"] = np.select(conditions,choices,default="black")
# print(df.head())

# YC3: Tạo một cột mới có tên ‘Amount’ có giá trị bằng Quantity * UnitPrice
df["Amount"] = df["Quantity"]*df["UnitPrice"]

# YC4: Tạo cột mới ‘Discount’ nhận giá trị 10% nếu Country là ‘United Kingdom’ và thuộc quý 4, 5% nếu là ‘France’ ngược lại là 0%.
df["Discount"] = np.where((df["Country"]=="United Kingdom")&(df["Previous"]==4),0.1,np.where((df["Country"]=="France"),0.05,0))

# YC5: Tạo cột mới ‘Total’ nhận giá trị bằng: Amount – Discount.
df["Total"] = df["Amount"] - df["Discount"]*df["Amount"]
print(df.head())








