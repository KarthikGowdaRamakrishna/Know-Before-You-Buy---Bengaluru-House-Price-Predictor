import pandas as pd
import numpy as np
from flask import Flask, render_template,request
import pickle

app=Flask(__name__)
data=pd.read_csv("Data/Clean_data.csv")
pipe=pickle.load(open("Ridge_Model.pkl","rb"))

@app.route('/')
def index():

    locations=sorted(data["location"].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    locations=request.form.get('location')
    bhk = float(request.form.get('Bhk'))
    bath = float(request.form.get('bath'))
    sqft = float(request.form.get('total_sqft'))
    print(locations,bhk,bath,sqft)

    input=pd.DataFrame([[locations,sqft,bath,bhk]],columns=["location","total_sqft","bath","Bhk"])
    prediction=str(np.round((pipe.predict(input)[0]+0.2)/100,2)) # I have converted Lakhs into Crores. Since data set is old, so I have added 0.2(20lakhs to compansate inflation.
    return "As per your requirement the predicted house price is {} crore".format(prediction)

if __name__=="__main__":
    app.run(debug=True,port=5000)
