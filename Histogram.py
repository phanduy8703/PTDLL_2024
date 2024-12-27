import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data2.csv', sep=';')
sns.set(style="whitegrid")
palette = sns.color_palette("husl", len(df.columns)) 

columns_to_plot = ['aqi', 'co', 'dew', 'humidity', 'no2', 'o3', 'pm10', 'pm25', 'pressure', 'so2', 'temperature', 'wind speed']

def plot_histogram(df, columns):
    for column in columns:
        if column in df.columns:
            # Chuyển cột về kiểu số (numeric)
            df[column] = pd.to_numeric(df[column], errors='coerce')
            
            # Đảm bảo không có giá trị NaN sau khi chuyển đổi
            df_clean = df[column].dropna()

            plt.figure(figsize=(8, 6))
            sns.histplot(df_clean, bins=20, kde=True, color='skyblue', edgecolor='black')
            display_column_name = column.replace('co', 'CO').replace('aqi', 'AQI').replace('pm10', 'PM10') \
                                        .replace('pm25', 'PM2.5').replace('no2', 'NO2').replace('o3', 'O3') \
                                        .replace('so2', 'SO2').replace('humidity', 'Humidity') \
                                        .replace('temperature', 'Temperature').replace('wind speed', 'Wind Speed') \
                                        .replace('pressure', 'Pressure').replace('dew', 'Dew Point')
            plt.title(f'Histogram of {display_column_name}', fontsize=16, fontweight='bold', color='#4C4C6C', 
                      pad=20, loc='center', fontname='Comic Sans MS')
            plt.xlabel(display_column_name, fontsize=14)
            plt.ylabel('Frequency', fontsize=14)
            
            # Cấu hình trục X để hiển thị giá trị từ min đến max chia thành 10 khoảng
            min_value = df_clean.min()
            max_value = df_clean.max()
            xticks = [round(min_value + (max_value - min_value) * i / 10, 2) for i in range(11)]
            plt.xticks(xticks, fontsize=12)

            plt.grid(True)
            plt.tight_layout()
            plt.show()
plot_histogram(df, columns_to_plot)
