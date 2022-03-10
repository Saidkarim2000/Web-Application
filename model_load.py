import numpy as np
import pickle
from keras.preprocessing import image

model_pkl = pickle.load(open('cats_vs_dogs_model.pkl','rb'))

def predict_label(f_path):
    img = image.load_img(f_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model_pkl.predict(images, batch_size=10)
    print(classes[0])
    if classes[0]>0.5:
        return (" Dog")
    else:
        return (" Cat") 