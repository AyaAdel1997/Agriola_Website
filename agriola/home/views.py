from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
import numpy as np
from django.views.generic.edit import FormView
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import base64
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf


TEMPLATES_DIRS = (
    'os.path.join(BASE_DIRS, "templates"),'
)

def index(request) :
   
    return render(request, "index.html")

def home2(request) :
   
    return render(request, "home2.html")

def about(request) :
    return render(request, "about.html")

def pricing(request) :
    return render(request, "pricing.html")

def features(request) :
    return render(request, "features.html")


def demo(request) :
    return render(request, "demo.html")

def Try_detect_Change(request) :
    if request.method=='POST' :
        f = request.FILES.getlist('images')
        fs = FileSystemStorage()
        
        ctx = {}
        SIZE=512
        path = '/home/fatma/Desktop/frontend/agriola/media/img'     
        filename = fs.save(f[0].name, f[0])
        file_url = fs.path(filename)
        print('absolute file path', file_url)    
        image1 = cv2.imread(file_url)
        
        #print(type(image1))
        image1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
        image1=cv2.resize(image1,(SIZE,SIZE),interpolation=cv2.INTER_AREA)
        image1=image1/255.0
        filename2 = fs.save(f[1].name, f[1])
        file_url2 = fs.path(filename2)
        #print('absolute file path', file_url)    
        image2 = cv2.imread(file_url2)
        
        #print(type(image1))
        image2=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
        image2=cv2.resize(image2,(SIZE,SIZE),interpolation=cv2.INTER_AREA)
        image2=image2/255.0
        im=np.concatenate((image1,image2),axis=2)
        im=np.expand_dims(im,axis=0)
        result = model.predict(im)
        x=result[0].squeeze(axis=2)
        plt.imsave('{}/result.jpg'.format(path),x)
        url = '{}/result.jpg'.format(path)
        
        

        with open( url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        ctx["image"] = image_data

        return render(request, 'Try_detect_Change1.html', ctx) 
    return  render(request, "Try_detect_Change1.html")






model= tf.keras.models.load_model("/home/fatma/Desktop/frontend/agriola/ml_model/unet_resnet34.h5",
 compile= False)

def test3(request) :
    if request.method == "POST" :
        f = request.FILES.getlist('images')
        fs = FileSystemStorage()
        ctx = {}
        SIZE=512
        path = '/home/fatma/Desktop/frontend/agriola/media/img'     
        filename = fs.save(f[0].name, f[0])
        file_url = fs.path(filename)
        print('absolute file path', file_url)    
        image1 = cv2.imread(file_url)
        
        #print(type(image1))
        image1=cv2.cvtColor(image1,cv2.COLOR_BGR2RGB)
        image1=cv2.resize(image1,(SIZE,SIZE),interpolation=cv2.INTER_AREA)
        image1=image1/255.0
        #print(image1.shape)

        filename2 = fs.save(f[1].name, f[1])
        file_url2 = fs.path(filename2)
        #print('absolute file path', file_url)    
        image2 = cv2.imread(file_url2)
        
        #print(type(image1))
        image2=cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
        image2=cv2.resize(image2,(SIZE,SIZE),interpolation=cv2.INTER_AREA)
        image2=image2/255.0
        

        im=np.concatenate((image1,image2),axis=2)
        im=np.expand_dims(im,axis=0)
        result = model.predict(im)
        x=result[0].squeeze(axis=2)
        plt.imsave('{}/image2.jpg'.format(path),x)
        url = '{}/image2.jpg'.format(path)
        
        

        with open( url, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')

        ctx["image"] = image_data

        return render(request, 'test3.html', ctx) 
    else : return  render(request, "test3.html")



