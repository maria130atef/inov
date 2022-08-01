from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=request.form.values()
   
    
   # prediction=model.predict_proba(final)
    output=int_features

   # if output==str(0):
    return  render_template('index.html',pred='Non Promter {}'.format(output))
   
if __name__ == '__main__':
    app.run(debug=True ,port=9500)