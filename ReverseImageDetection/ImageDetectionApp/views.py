from django.shortcuts import render, redirect
from .models import *
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, FormView
from .forms import UploadForm
import time
#import templates.ImageDetectionApp

trained_model=r"F:\Virang ka Kaam\Reverse-Image-Detection\ReverseImageDetection\ImageDetectionApp\trainedshopper.h5"
label_bin=r"F:\Virang ka Kaam\Reverse-Image-Detection\ReverseImageDetection\ImageDetectionApp\labelbin"

upper_range = 0
lower_range = 0


def label_extraction(image_file_path):
    image = cv2.imread(image_file_path)
    output = image.copy()
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    print("[INFO] loading network...")
    model = load_model(trained_model)
    lb = pickle.loads(open(label_bin, "rb").read())
    # classify the input image
    print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)
    label = lb.classes_[idx]
    print(type(label))
    return label


class UploadFormView(FormView):
    template_name='upload.html'
    form_class=UploadForm
    success_url='/app/results/'

    def form_valid(self, form):
        global upper_range, lower_range
        upper_range = form.cleaned_data.get('upper_range')
        lower_range = form.cleaned_data.get('lower_range')
        image=form.cleaned_data.get('image')
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        #extracted_label=label_extraction(uploaded_file_url)
        extracted_label='trousers'
        time.sleep(5)
        self.success_url=self.success_url + '%s'%(extracted_label)
        return super().form_valid(form)



def ResultView(request, label):
    #coats, dresses, pullover, sandals, shirts, sneaker, trousers, tshirts
    global upper_range, lower_range
    upper = upper_range
    lower = lower_range
    print(lower)
    print(upper)
    if label == 'trousers':
        trouser=Trouser.objects.filter(price__range=(lower, upper))
        #print(type(item_obj))
        return render(request, 'search_result.html', {'item_obj':trouser})
    elif label == 'tshirts':
        tshirt=TopAndTshirt.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':tshirt})
    elif label == 'sneaker':
        sneaker=Sneaker.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':sneaker})
    elif label == 'shirts':
        shirt=Shirt.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':shirt})
    elif label == 'sandals':
        sandal=Sandal.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':sandal})
    elif label == 'pullover':
        pullover=Pullover.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':pullover})
    elif label == 'dresses':
        dress=Dress.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':dress})
    elif label == 'coats':
        coat=Coat.objects.filter(price__range=(lower, upper))
        return render(request, 'search_result.html', {'item_obj':coat})
    
    return render(request, 'search_result.html', {'label': label})



