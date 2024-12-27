import pandas as pd

df = pd.read_csv('aqi_airqualitydata_2020_en.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df['Specie'] = df['Specie'].replace(
    {'wind-speed': 'wind speed', 'wind-gust': 'wind gust', 'Ho Chi Minh City': 'Ho Chi Minh'})
df['City'] = df['City'].replace({'Ho Chi Minh City': 'Ho Chi Minh'})
df = df.drop_duplicates()

# Các cột cần giữ lại trong bảng cuối cùng
required_columns = ['temperature', 'humidity', 'wind speed', 'wind gust', 'pm25', 'dew', 'pressure',
                    'co', 'pm10', 'so2', 'no2', 'o3', 'aqi', 'precipitation']

# Lọc các dòng có giá trị thuộc các chỉ số cần thiết từ cột 'Specie'
filtered_data = df[df['Specie'].isin(required_columns)]
filtered_data = filtered_data[['Date', 'City', 'Specie', 'median']]

# Dùng pivot_table để chuyển các giá trị của 'Specie' thành các cột riêng biệt
pivoted_data = filtered_data.pivot_table(index=['Date', 'City'], columns='Specie', values='median', aggfunc='first')
pivoted_data.reset_index(inplace=True)
pivoted_data.to_csv('data1.csv', index=False)

cities = ['Ha Noi', 'Ha Long', 'Hai Phong', 'Hue', 'Ho Chi Minh']
city_dataframes = {}

for city in cities:
    city_df = pivoted_data[pivoted_data['City'] == city].drop(columns='City')
    city_dataframes[city] = city_df
    city_df.to_csv(f'{city.replace(" ", "_")}.csv', index=False)
