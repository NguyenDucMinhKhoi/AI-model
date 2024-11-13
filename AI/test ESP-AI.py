from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('D:\\Đồ án NKD\AI\\random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Receive data from ESP8266 as JSON
    data = request.get_json(force=True)
    
    # Check if data was received
    if data is None:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        # Print the received data (showing it on the terminal)
        print("Received data from ESP8266:", data)
        
        # Convert data from JSON to DataFrame (wrap `data` in a list to create a DataFrame)
        df = pd.DataFrame([data])
        
        # Make a prediction
        predictions = model.predict(df)
        
        # Print the prediction result on the terminal
        print("Prediction result:", predictions)
        
        # Return the result as JSON
        return jsonify(predictions.tolist())
    
    except Exception as e:
        # Handle any unexpected error
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run server on all IPs to allow connection from ESP8266
    app.run(debug=True, host='0.0.0.0', port=5000)
