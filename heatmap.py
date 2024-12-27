import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read file
data = pd.read_csv('data2.csv')

# Chuyển cột 'Date' sang kiểu datetime
data['Date'] = pd.to_datetime(data['Date'])

# Tính toán các giá trị trung bình theo thành phố
city_means = data.groupby('City').mean(numeric_only=True)

# Các cột quan tâm để vẽ biểu đồ
columns_of_interest = [
    "aqi", "co", "dew", "humidity", "no2", "o3", "pm10",
    "pm25", "precipitation", "pressure", "so2", "temperature", "wind speed"
]

# Đặt ngưỡng ô nhiễm mẫu (có thể điều chỉnh theo từng chỉ số)
thresholds = {
    "aqi": 100, "co": 1, "dew": 10, "humidity": 60, "no2": 50, "o3": 100,
    "pm10": 50, "pm25": 25, "precipitation": 5, "pressure": 1010, "so2": 20,
    "temperature": 25, "wind speed": 5
}

# Tạo bảng riêng cho mỗi chỉ số
for column in columns_of_interest:
    # Tạo bảng dữ liệu cho từng chất
    city_column = city_means[column].reset_index()

    # Vẽ biểu đồ cột cho từng chất
    city_column.plot(kind='bar', x='City', y=column, color=sns.color_palette("Set2", n_colors=len(city_column)))

    # Thêm đường ngang thể hiện mức ngưỡng ô nhiễm
    threshold = thresholds.get(column, None)
    if threshold is not None:
        plt.axhline(y=threshold, color='red', linestyle='--', label=f'Threshold ({threshold})')

    plt.title(f"Average {column.upper()} by City", fontsize=16)
    plt.xlabel("City", fontsize=14)
    plt.ylabel(column.upper(), fontsize=14)
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.show()

city_means_selected = city_means[columns_of_interest]
# Plot the data
city_means_selected.plot(kind="bar", figsize=(16, 8), colormap="viridis", width=0.8)
plt.title("Average Environmental Indicators by City", fontsize=16)
plt.xlabel("City", fontsize=14)
plt.ylabel("Average Value", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title="Indicators", fontsize=10)
plt.axhline(y=50, color='red', linestyle='--', label='Example Threshold (50)')
plt.legend()
plt.tight_layout()
plt.show()

# Thêm cột 'Month' để tính toán trung bình theo tháng
data['Month'] = data['Date'].dt.to_period('M')
monthly_means = data.groupby(['City', 'Month']).mean(numeric_only=True).reset_index()

# Pivot dữ liệu để vẽ biểu đồ đường
pivot_aqi = monthly_means.pivot(index='Month', columns='City', values='aqi')

# Biểu đồ đường: Chỉ số AQI theo từng tháng
plt.figure(figsize=(12, 6))
for city in pivot_aqi.columns:
    plt.plot(pivot_aqi.index.astype(str), pivot_aqi[city], label=city)

plt.title("Monthly Average AQI by City", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("AQI", fontsize=14)
plt.axhline(y=100, color='red', linestyle='--', label='AQI Threshold (100)')
plt.xticks(rotation=45, fontsize=10)
plt.legend(title="City", fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Compute the correlation matrix for numeric columns
correlation_matrix = data.corr(numeric_only=True)

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# Create a heatmap with a visually appealing color palette and annotations
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar_kws={"shrink": 0.8, "aspect": 20},
    square=True
)

# Customize the plot for better aesthetics
plt.title("Heatmap of Attribute Correlations", fontsize=16, pad=20)
plt.xticks(fontsize=10, rotation=45, ha='right')
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
