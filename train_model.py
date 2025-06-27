# Bước 1: Import thư viện
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Bước 2: Tạo dữ liệu CSV (nếu chưa có sẵn file)
data = """Area,Price
50,800
60,1000
70,1200
80,1400
90,1600
100,1800
"""
with open("house_data.csv", "w") as file:
    file.write(data)

# Bước 3: Đọc dữ liệu từ file CSV
df = pd.read_csv("house_data.csv")
print("Dữ liệu đầu vào:")
print(df)

# Bước 4: Chuẩn bị dữ liệu train
X = df[['Area']]   # đầu vào: diện tích
y = df['Price']    # đầu ra: giá nhà

# Bước 5: Tạo và huấn luyện model
model = LinearRegression()
model.fit(X, y)

# Bước 6: Dự đoán giá nhà mới
area_moi = [[75]]  # 75m2
price_du_doan = model.predict(area_moi)
print(f"Dự đoán giá nhà cho 75m² là: {price_du_doan[0]:,.0f} triệu VNĐ")

# Bước 7: Vẽ biểu đồ
plt.scatter(X, y, color='blue', label='Dữ liệu thật')
plt.plot(X, model.predict(X), color='red', label='Đường dự đoán')
plt.xlabel('Diện tích (m²)')
plt.ylabel('Giá (triệu VNĐ)')
plt.title('Dự đoán giá nhà bằng Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
