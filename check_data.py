import pandas as pd

# Đọc dữ liệu từ các file CSV
df_hanoi = pd.read_csv('Ha_Noi.csv')
df_halong = pd.read_csv('Ha_Long.csv')
df_haiphong = pd.read_csv('Hai_Phong.csv')
df_hue = pd.read_csv('Hue.csv')
df_hochiminh = pd.read_csv('Ho_Chi_Minh.csv')
df = pd.read_csv('data1.csv')

# Hàm kiểm tra tỷ lệ dữ liệu thiếu và số lượng trùng lặp
def check(df):
    # Kiểm tra tỷ lệ dữ liệu thiếu
    missing_data = df.isnull().mean(axis=0)
    # Kiểm tra số lượng dữ liệu trùng lặp
    duplicate_data = df.duplicated().sum()
    return missing_data, duplicate_data

# Kiểm tra các DataFrame
check_all = check(df)
check_ha_noi = check(df_hanoi)
check_ha_long = check(df_halong)
check_hai_phong = check(df_haiphong)
check_hue = check(df_hue)
check_ho_chi_minh = check(df_hochiminh)

# In kết quả tỷ lệ dữ liệu thiếu và số lượng dữ liệu trùng lặp
print("Tỷ lệ dữ liệu rỗng trên df tổng:")
print(check_all[0])
print(f"Số lượng dữ liệu trùng lặp trên df tổng: {check_all[1]}")

print("Tỷ lệ dữ liệu rỗng ở df Hà Nội:")
print(check_ha_noi[0])
print(f"Số lượng dữ liệu trùng lặp ở df Hà Nội: {check_ha_noi[1]}")

print("Tỷ lệ dữ liệu rỗng ở df Hạ Long:")
print(check_ha_long[0])
print(f"Số lượng dữ liệu trùng lặp ở df Hạ Long: {check_ha_long[1]}")

print("Tỷ lệ dữ liệu rỗng ở df Hải Phòng:")
print(check_hai_phong[0])
print(f"Số lượng dữ liệu trùng lặp ở df Hải Phòng: {check_hai_phong[1]}")

print("Tỷ lệ dữ liệu rỗng ở df Huế:")
print(check_hue[0])
print(f"Số lượng dữ liệu trùng lặp ở df Huế: {check_hue[1]}")

print("Tỷ lệ dữ liệu rỗng ở df Hồ Chí Minh:")
print(check_ho_chi_minh[0])
print(f"Số lượng dữ liệu trùng lặp ở df Hồ Chí Minh: {check_ho_chi_minh[1]}")
