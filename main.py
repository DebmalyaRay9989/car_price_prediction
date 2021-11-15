from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    temp_array = list()
    if request.method == 'POST':
        Hardness = float(request.form['Hardness'])
        Conductivity=float(request.form['Conductivity'])
        Organic_carbon=float(request.form['Organic_carbon'])
        Turbidity=float(request.form['Turbidity'])
        ph=float(request.form['ph'])
        Sulfate=float(request.form['Sulfate'])
        temp_array = temp_array + [Hardness, Conductivity, Organic_carbon, Turbidity, ph, Sulfate]
        data = np.array([temp_array])
        prediction = int(model.predict(data)[0])

        if prediction == 0:
            return render_template('index.html',prediction_text="The Water Is Safe For Drinking ! {}".format(prediction))
        elif prediction == 1:
            return render_template('index.html',prediction_text="The Water Is Not Safe For Drinking! {}".format(prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

