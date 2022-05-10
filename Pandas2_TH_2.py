import pandas as pd
df = pd.read_csv("FoodPrice_in_Turkey.csv")

# Tách thành file con thứ nhất từ file gốc
df_1 = df[:100]

# Tách thành file con thứ 2 từ file gốc
df_2 = df[100:400]

# Tách thành file con thứ 3 từ file gốc và lấy một số cột về thông tin sản phẩm
df_3 = df.loc[400:500,["ProductId","ProductName","UmId","UmName"]]

# Ghép các dòng từ các file
# df_4 = df_1.append(df_2)
df_5 = pd.concat([df_1,df_2,df_3],axis = 0) 
print(df_5)
