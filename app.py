from distutils.log import debug
import os
# import model_load
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)           

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
#             p = model_load.predict_label(f_path)
            return render_template("success.html", prediction = p, f_path=f_path)  
        
    except:
        return "Firstly choose a file then press predict button!"



if __name__ == "__main__":
    app.run(debug=True)

