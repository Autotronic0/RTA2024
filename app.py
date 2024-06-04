from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('perceptron_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/predict', methods=['GET'])
def predict():

    features = request.args.getlist('features')
    
    features = np.array(features, dtype=float).reshape(1, -1)
    
    prediction = model.predict(features)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
