from distutils.log import debug
import os
import pickle
import numpy as np
from keras.preprocessing import image
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)


model_pkl = pickle.load(open('cats_vs_dogs_model.pkl','rb'))

def predict_label(f_path):
    img = image.load_img(f_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model_pkl.predict(images, batch_size=32)
    print(classes[0])
    if classes[0]>0.5:
        return (" Dog")
    else:
        return (" Cat")            

path = app.config["UPLOADED_IMAGES"] = "static"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])  
def submission():  
    try:
        if request.method == 'POST':  
            f = request.files['file']  
            f_path = "static/" + f.filename
            f.save(f_path) 
            p = predict_label(f_path)
            return render_template("success.html", prediction = p, f_path=f_path)  
        
    except:
        return "Firstly choose a file then press predict button!"



if __name__ == "__main__":
    app.run(debug=True)

