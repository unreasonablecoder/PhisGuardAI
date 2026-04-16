from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import re

app = Flask(__name__)
CORS(app) # Allows your React app to talk to this API

# Load the "Brain" we trained earlier
model = joblib.load('../02_Processed_Data/phishing_model.pkl')

def extract_features(url):
    # This must match the exact number of features (30) in your dataset
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if "-" in url else 0)
    features.append(url.count('.'))
    # Padding to 30 features so the model doesn't crash
    while len(features) < 30: features.append(0)
    return features

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')
    
    features = extract_features(url)
    prediction = model.predict([features])
    
    # Return 1 for Safe, -1 for Phishing
    result = "Safe" if prediction[0] == 1 else "Phishing"
    return jsonify({"status": result, "url": url})

if __name__ == '__main__':
    app.run(port=5000)