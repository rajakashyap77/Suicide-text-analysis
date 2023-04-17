from flask import Flask, request, jsonify,render_template
from keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model('trained_model.h5')  # Load the trained model

@app.route('/')
def index():
    return render_template('index.html')  # Serve the index.html file

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('text')  # Get the input text from the request form
    # Perform any necessary preprocessing on the text (e.g., tokenization, padding, etc.)
    
    # Make prediction
    prediction = model.predict(np.array([text]))
    prediction_label = np.argmax(prediction)  # Get the predicted label (0 or 1)
    
    # Map the predicted label to the corresponding class
    classes = ['suicide', 'non-suicide']
    prediction_class = classes[prediction_label]
    
    return jsonify({'prediction': prediction_class})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
