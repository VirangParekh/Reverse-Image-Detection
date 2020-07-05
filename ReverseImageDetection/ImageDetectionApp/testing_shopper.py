# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os


# %%
args = {"model": r"F:\Virang ka Kaam\Reverse-Image-Detection\ReverseImageDetection\ImageDetectionApp\trainedshopper.h5",
        "labelbin": r"F:\Virang ka Kaam\Reverse-Image-Detection\ReverseImageDetection\ImageDetectionApp\labelbin",
       "input_img": r"C:\Users\Virang\Pictures\hackathon\corporate-t-shirts-500x500.jpeg"
       }


# %%
# load the image
image = cv2.imread(args["input_img"])
print(type(image))
output = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)


# %%
# load the trained convolutional neural network and the label
# binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())
# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)

label = lb.classes_[idx]
print(label)


