# YC1: Đọc bộ dữ liệu, cho biết số dòng, số cột và kiểu dữ liệu của các thuộc tính.
import pandas as pd
import numpy as np
df = pd.read_csv("OnlineRetail.csv",encoding='ISO-8859-1')
# print("Số dòng của file là:",df.shape[0],"\nSố cột của file là:",df.shape[1])
print(df.info())

# YC2: Xây dựng bảng Pivot table, với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia. 
table_2 = df.pivot_table(values="Quantity",index="Country",columns="InvoiceNo",aggfunc="mean")
# print(table)

# YC3: Xây dựng bảng Pivot table, với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho.
table_3 = df.pivot_table(values="Quantity",index="CustomerID",columns="StockCode",aggfunc=["max","min"])

# YC4:Xây dựng bảng Pivot table, với mỗi Mã kho tính tổng số lượng các mặt hàng và trung bình cộng giá.
table_4 = df.pivot_table(values=["Quantity","UnitPrice"],index="StockCode",aggfunc={"Quantity":np.sum,"UnitPrice":"mean"})

# YC5: Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày.
table_5 = df.pivot_table(values="Quantity",index="InvoiceDate",aggfunc="sum")
print(table_5)






