#### TEST FILE ONLY - NO RELEVANT CODE HERE ###


import pickle
from flask import Flask, request, jsonify
from surprise.prediction_algorithms import SVD

app = Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

@app.route('/predict', methods=['POST'])
def predict():


    new_user = request.get_json()

    with open('../model_files/svd_model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()

    preds = model.test(new_user)

    result = {'movie_preds':  list(preds)}

    return jsonify(result)

import requests


test_new_user = [('1000', '1', 2), ('1000', '3', 5),
                ('1000', '6', 2.5), ('1000', '47', 4.5),
                ('1000', '50', 3)]

url = “http://localhost:5000/predict"
r = requests.post(url, json = test_new_user)
r.text.strip()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)