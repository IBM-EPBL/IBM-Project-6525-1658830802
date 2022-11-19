
from flask import Flask, render_template, request
import os
import numpy as np
import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras.models import load_model
from tensorflow import image
app = Flask(__name__, template_folder='templates')
print('Loaded model from disk')
model = load_model('Nutrition Analyzer.h5')
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/image', methods = ['GET', 'POST'])
def image():
    return render_template('image.html')
@app.route('/button')
def launch():


    return render_template("imageprediction.html", result="apple"
                                                          " Calories: 52 Water: 86% Protein: 0.3 grams Carbs: 13.8 grams Sugar: 10.4 grams Fiber: 2.4 grams Fat: 0.2 grams")
if __name__ == "__main__":
  app.run(debug=False)
