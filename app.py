from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model
model = prod_predictor

# Create a Flask app
app = Flask(__name__)

# Define the POST API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the text input from the request body
    text = request.get_json()['text']

    # Make a prediction on the text
    prediction = model.predict([text])

    # Save the prediction and text to a CSV file
    df = pd.DataFrame({'text': [text], 'prediction': [prediction]})
    df.to_csv('predictions.csv', mode='a', header=False, index=False)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
