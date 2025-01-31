#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from sklearn.datasets import load_iris

iris = load_iris()


class Irisrequest(BaseModel):
    sepal_length : float
    sepal_width: float
    petal_length: float
    petal_width: float


model = joblib.load('iris_model.pkl')
app = FastAPI()


@app.get('/')
def welcome():
    return 'Iris APP'


@app.post('/predict/')
def predict(Iris_data:Irisrequest):
    data = [[Iris_data.sepal_length,Iris_data.sepal_width,Iris_data.petal_length,Iris_data.petal_width]]
    prediction = model.predict(data)
    predicted_class = iris.target_names[prediction[0]]
    return 'prediction',predicted_class
   




