#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import pickle
import gradio as gr
import pandas as pd 
import numpy as np
import os

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def load_model():
    current_dir = os.getcwd()
    global_path = current_dir + "\BestModel\BestModule"
    model = pickle.load(open(global_path, 'rb'))
    return model

def predict_survival(Age, Sex, ChestPain, RestingBloodPressure, Cholesterol, FastingBloodSugar, RestEcg, MaxHeartRateAch, ExcersiseInducedAngina, StDepression, StSlope, NumMajorVessels, Thalassemia):
    df = pd.DataFrame({'Sex': [Sex], 'Age': [Age], 'ChestPain': [ChestPain], 'RestingBloodPressure': [RestingBloodPressure], 'Cholesterol': [Cholesterol], 'FastingBloodSugar': [FastingBloodSugar], 'RestEcg': [RestEcg], 
                        'MaxHeartRateAch': [MaxHeartRateAch], 'ExcersiseInducedAngina': [ExcersiseInducedAngina], 'StDepression': [StDepression], 'StSlope': [StSlope], 'NumMajorVessels': [NumMajorVessels],'Thalassemia': [Thalassemia]})
    
    model = load_model()
    predi = model.predict_proba(df)[0]
    return {'Perishes': predi[1], 'Survives': predi[0]}
    
Sex                    = gr.inputs.Radio([0, 1 ], label="Sex - Male = 1 | Female = 0")
Age                    = gr.inputs.Slider(minimum=0, maximum=100, default=20, label="Age")
ChestPain              = gr.inputs.Slider(minimum=0, maximum=10,  default=0, label="ChestPain")
RestingBloodPressure   = gr.inputs.Slider(minimum=0, maximum=200, default=100, label="Resting Blood Pressure")
Cholesterol            = gr.inputs.Slider(minimum=0, maximum=500, default=120, label="Cholesterol")
FastingBloodSugar      = gr.inputs.Slider(minimum=0, maximum=10,  default=0, label="Fasting Blood Sugar")
RestEcg                = gr.inputs.Slider(minimum=0, maximum=10,  default=0, label="Rest Ecg") 
MaxHeartRateAch        = gr.inputs.Slider(minimum=0, maximum=200, default=100, label="Max Heart RateAch")
ExcersiseInducedAngina = gr.inputs.Slider(minimum=0, maximum=10, default=0, label="Excersise Induced Angina")
StDepression           = gr.inputs.Slider(minimum=0, maximum=2.0, default=0, label="St Depression")
StSlope                = gr.inputs.Slider(minimum=0, maximum=10, default=0, label="St Slope")
NumMajorVessels        = gr.inputs.Slider(minimum=0, maximum=10, default=0, label="Num Major Vessels")
Thalassemia            = gr.inputs.Slider(minimum=0, maximum=10, default=0, label="Thalassemia")

def runGR():     
    gr.Interface(predict_survival, [Age, Sex, ChestPain, RestingBloodPressure, Cholesterol, FastingBloodSugar, RestEcg, MaxHeartRateAch, ExcersiseInducedAngina, StDepression, StSlope, NumMajorVessels, Thalassemia],
             "label", live=True).launch(inbrowser = True)

button = tk.Button(text='Click Me', command=runGR, bg='brown', fg='white')

canvas1.create_window(150,150,window=button)

root.mainloop()

