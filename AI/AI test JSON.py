from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Tải mô hình đã lưu
model = joblib.load('D:/Đồ án NKD/random_forest_model.pkl')

# Tạo dữ liệu mẫu (bạn thay đổi dữ liệu thực tế của mình vào đây)
data = {
    "temperature": [38.5, 39.1, 37.9, 39.3],  # ví dụ về nhiệt độ
    "heart_rate": [160, 140, 120, 180],  # ví dụ về nhịp tim
    "breathing_rate": [15, 25, 20, 30],  # ví dụ về nhịp thở
    "age": [5, 8, 3, 10],  # ví dụ về tuổi
    "sex": [0, 1, 1, 0],  # 0: Đực, 1: Cái
    "race": [1, 2, 1, 2],  # 1: Chó lớn, 2: Chó nhỏ
    "Easily affected": [1, 0, 0, 1]  # nhãn mẫu
}

# Tạo DataFrame
df = pd.DataFrame(data)

# Xuất DataFrame ra file JSON
df.to_json("ai_input_data.json", orient="records")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Chuyển đổi dữ liệu từ JSON thành DataFrame
    df = pd.DataFrame(data)
    
    # Dự đoán
    predictions = model.predict(df)
    
    # Trả kết quả dưới dạng JSON
    return jsonify(predictions.tolist())

# Đọc dữ liệu từ file JSON
input_data = pd.read_json("ai_input_data.json")

# Hiển thị dữ liệu
print(input_data)

if __name__ == '__main__':
    app.run(debug=True)
