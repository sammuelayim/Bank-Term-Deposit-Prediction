
from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the logistic regression model
with open("logistic_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define a route for predictions
@app.route("/predict", methods=["POST"])
def predict():
    # Get data from the request
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    
    # Make predictions
    prediction = model.predict(features)
    probability = model.predict_proba(features)[:, 1]
    
    # Return the response
    return jsonify({
        "prediction": int(prediction[0]),
        "probability": float(probability[0])
    })

if __name__ == "__main__":
    app.run(debug=True)
