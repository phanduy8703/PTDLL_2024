import pandas as pd
import numpy as np

def summarize_numeric_columns(file_path, output_path):
    # Đọc dữ liệu từ file CSV
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
        return
    # Lọc các cột có kiểu số
    numeric_cols = df.select_dtypes(include=[np.number])
    #Tính toán các chỉ số
    summary = pd.DataFrame()
    summary['count'] = numeric_cols.count()
    summary['mean'] = numeric_cols.mean()
    summary['std'] = numeric_cols.std()
    summary['min'] = numeric_cols.min()
    summary['q1 (25%)'] = numeric_cols.quantile(0.25)
    summary['q2 (50%)'] = numeric_cols.median()
    summary['q3 (75%)'] = numeric_cols.quantile(0.75)
    summary['max'] = numeric_cols.max()
    summary['mode'] = numeric_cols.mode().iloc[0]
    summary['median'] = numeric_cols.median()

    print("Thống kê các thuộc tính kiểu số:")
    print(summary)
    try:
        summary.to_csv(output_path, index=True)
        print(f"Kết quả đã được lưu vào file: {output_path}")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

file_path = 'data2.csv'
output_path = 'sum_data.csv'
summarize_numeric_columns(file_path, output_path)

