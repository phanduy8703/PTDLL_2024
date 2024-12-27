import pandas as pd

df = pd.read_csv("data1.csv")
exclude_columns = ["precipitation", "wind gust"]

columns_to_fill = [col for col in df.columns if col not in exclude_columns + ["aqi"] and df[col].dtype != 'object']
# Điền giá trị thiếu bằng trung bình theo cột City
for col in columns_to_fill:
    df[col] = df.groupby("City")[col].transform(lambda x: x.fillna(x.mean()))

# Xử lý dữ liệu thiếu trong cột aqi
def fill_aqi(row):
    if pd.notna(row['aqi']):
        return row['aqi']  # Giữ nguyên giá trị nếu đã có
    aqi_pm10 = calculate_aqi(row['pm10'], breakpoints_pm10) if pd.notna(row['pm10']) else None
    aqi_pm25 = calculate_aqi(row['pm25'], breakpoints_pm25) if pd.notna(row['pm25']) else None

    if aqi_pm10 is not None and aqi_pm25 is not None:
        return max(aqi_pm10, aqi_pm25)
    elif aqi_pm10 is not None:
        return aqi_pm10
    elif aqi_pm25 is not None:
        return aqi_pm25
    else:
        # Nếu thiếu cả pm10 và pm25, lấy trung bình AQI của thành phố đó
        return city_aqi_means.get(row['City'], None)

# Các ngưỡng tính AQI
breakpoints_pm25 = [
    {'low': 0.0, 'high': 12.0, 'aqi_low': 0, 'aqi_high': 50},
    {'low': 12.1, 'high': 35.4, 'aqi_low': 51, 'aqi_high': 100},
    {'low': 35.5, 'high': 55.4, 'aqi_low': 101, 'aqi_high': 150},
    {'low': 55.5, 'high': 150.4, 'aqi_low': 151, 'aqi_high': 200}
]

breakpoints_pm10 = [
    {'low': 0.0, 'high': 54.0, 'aqi_low': 0, 'aqi_high': 50},
    {'low': 55.0, 'high': 154.0, 'aqi_low': 51, 'aqi_high': 100},
    {'low': 155.0, 'high': 254.0, 'aqi_low': 101, 'aqi_high': 150},
    {'low': 255.0, 'high': 354.0, 'aqi_low': 151, 'aqi_high': 200}
]

def calculate_aqi(pm_value, breakpoints):
    for bp in breakpoints:
        if bp['low'] <= pm_value <= bp['high']:
            return (bp['aqi_high'] - bp['aqi_low']) / (bp['high'] - bp['low']) * (pm_value - bp['low']) + bp['aqi_low']
    return None

# Tính trung bình AQI theo từng thành phố
city_aqi_means = {city: round(aqi_mean if pd.notna(aqi_mean) else 0) for city, aqi_mean in
                  df.groupby("City")['aqi'].mean().to_dict().items()}

# Điền giá trị thiếu cho cột AQI
df['aqi'] = df.apply(fill_aqi, axis=1)
df['aqi'] = df['aqi'].round()

# Lưu kết quả xử lý vào tệp mới
df.to_csv("data2.csv", index=False)

