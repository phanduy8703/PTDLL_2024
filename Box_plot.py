import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data2.csv', sep=';')
sns.set(style="whitegrid")
palette = sns.color_palette("husl", len(df.columns)) 

columns_to_plot = ['aqi', 'co', 'dew', 'humidity', 'no2', 'o3', 'pm10', 'pm25', 'pressure', 'so2', 'temperature', 'wind speed']

def box_plot(df, columns):
    for column in columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors='coerce')
            
            # Kiểm tra lại nếu có giá trị NaN sau khi chuyển đổi
            if df[column].isnull().all():
                print(f"Column {column} does not have any valid numeric data.")
                continue 
            
            plt.figure(figsize=(8, 8))
            sns.boxplot(x='City', y=column, data=df, palette="husl",width=0.4)
            display_column_name = column.replace('co', 'CO').replace('aqi', 'AQI').replace('pm10', 'PM10') \
                                        .replace('pm25', 'PM2.5').replace('no2', 'NO2').replace('o3', 'O3') \
                                        .replace('so2', 'SO2').replace('humidity', 'Humidity') \
                                        .replace('temperature', 'Temperature').replace('wind speed', 'Wind Speed') \
                                        .replace('pressure', 'Pressure').replace('dew', 'Dew Point')
            plt.title(f'Box Plot of {display_column_name}', fontsize=20, fontweight='bold', color='#4C4C6C', 
                      pad=20, loc='center', fontname='Comic Sans MS')
            plt.xlabel('City', fontsize=14, color='#333333')
            plt.ylabel(column, fontsize=14, color='#333333')

            plt.xticks(fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.tight_layout()
            plt.show()
box_plot(df, columns_to_plot)
