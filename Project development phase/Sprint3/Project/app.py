
from flask import Flask, render_template, request
import os
import numpy as np
from tensorflow.keras.model import load_model
from tensorflow.keras.preprocessing import image
app = Flask(__name__, template_folder='templates')
print('Loaded model from disk')
model = load_model('Nutrition Analyzer.h5')
@app.route('/')
def home():
  return render_template('home.html')
@app.route('/image', methods = ['GET', 'POST'])
def image():
    return render_template('image.html')
@app.route('/route', methods = ['GET', 'POST'])
def launch():
  if request.method == 'POST':
    f=request.files['file']
    basepath = os.path.dirname('__file__')
    filepath = os.path.join(basepath, "uploads", f.filename)
    f.save(filepath)

    img = image.load_img(filepath, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    pred = np.argmax(model.predict(x), axis=1)
    print("prediction", pred)
    index = ['APPLES', 'BANANA', 'ORANGE', 'PINEAPPLE', 'WATERMELON']
    result = str(index[pred[0]])

    x = result
    print(x)
    print(result)
    return render_template("imageprediction.html", showcase=(result), showcase1=(x))
if __name__ == "__main__":
  app.run(debug=False)
