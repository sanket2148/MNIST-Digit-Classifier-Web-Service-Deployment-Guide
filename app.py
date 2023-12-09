from asyncio import DatagramProtocol
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import mysql.connector
import json
from datetime import datetime
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('mnist_model.h5')

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Sanket@2148',
    'host': '10.32.4.177',
    'database': 'Ai_assignment'
}
def preprocess_data(data):
    # Convert the incoming data to a numpy array
    image_array = np.array(data, dtype=np.float32)
    # Normalize the data as the model was trained on normalized data
    image_array /= 255.0
    # Reshape the data to match the input shape of the model
    image_array = image_array.reshape(-1, 28, 28)
    return image_array
@app.route('/')
def home():
    
    return render_template('home.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Receive image data from the client
        # data = request.json['data']
        # preprocessed_data = preprocess_data(data)
        # # Perform prediction
        # predictions = model.predict(preprocessed_data)
        file = request.files['file']
        image = Image.open(file.stream).convert('L')  # Convert to grayscale
        image = image.resize((28, 28))  # Resize to 28x28
        image_array = np.array(image)
        preprocessed_data = preprocess_data(image_array)
        
        # Perform prediction
        predictions = model.predict(preprocessed_data)
        # Convert prediction result to JSON serializable format
        prediction_result = predictions.tolist()
        predicted_digit = np.argmax(predictions, axis=1)
        prediction_time = datetime.now()
        # Use context manager for database connection
        with mysql.connector.connect(**db_config) as conn:
            with conn.cursor() as cursor:
                # Log the prediction result in the database
                insert_query = "INSERT INTO predictions (request_data, prediction_result, prediction_time) VALUES (%s, %s, %s)"
                # cursor.execute(insert_query, (json.dumps(file), json.dumps(prediction_result), prediction_time))
                {"error":"Object of type FileStorage is not JSON serializable"}
                conn.commit()

        # Return the prediction result
        result = {'prediction': prediction_result, 'predicted_digit': int(predicted_digit[0])}
        return jsonify(result)
    except Exception as e:
        # Handle exceptions
        import traceback
        traceback.print_exc()  # This will print the full stack trace to stdout
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
