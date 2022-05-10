import pandas as pd
df = pd.read_csv("FoodPrice_in_Turkey.csv")
# print(df.head())

# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, giữ chỉ số ban đầu của các dòng
df = df.drop_duplicates(["ProductId"],keep = "last").reset_index(drop=True)
# print(df.head())

# Tách file chứa thông tin sản phẩm
df_product = df[["ProductId","ProductName","UmId","UmName"]]
# print(df_product.head())

# Tách file chauws thông tin giá 
df_price = df[["ProductId","Place","Month","Year","Price"]]
# print(df_price)


# Tách file chứa thông tin giá với số dòng từ bản ghi 10 đến 20
df_price_1020 = df.loc[10:20,["ProductId","Place","Month","Year","Price"]]
# print(df_price_1020)

# Ghép các file có cột thuộc tính chung ProductId
#df_new = pd.merge(df_product,df_price,on="ProductId")
df_new = pd.concat([df_product,df_price],axis=1)
print(df_new)