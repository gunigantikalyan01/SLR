'''
in this we are goint to write the backend code to load the model and give predictions
'''
import flask
import numpy as np
import pickle
from flask import Flask, render_template, request
app = Flask(__name__)

with open("SLR_model.pkl", "rb") as f:
    model = pickle.load(f)
@app.route('/')
def default_site():
    return render_template("index.html")
@app.route('/predict', methods = ['GET','POST'])
def predict():
    value = [float(x) for x in request.form.values()]
    value = np.array([value])
    result=model.predict(value)[0]
    result=round(float(result),3)
    return render_template("index.html", prediction_weight=result)
if __name__ == '__main__':
    app.run(debug=True)