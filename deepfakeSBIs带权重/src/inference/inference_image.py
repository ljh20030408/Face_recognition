import os
import gc
import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
from torchvision import datasets,transforms,models,utils
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from PIL import Image
import sys
import random
import shutil
from model import Detector
import argparse
from datetime import datetime
from tqdm import tqdm
from retinaface.pre_trained_models import get_model
from preprocess import extract_face
import warnings
import time

warnings.filterwarnings('ignore')

def main(weight_name,input_image):
    
    #2.6S#
    model=Detector()
    model=model.to(device)

    cnn_sd=torch.load(weight_name)["model"]
    model.load_state_dict(cnn_sd)
    model.eval()

    frame = cv2.imread(input_image)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
#1.5S#
    print(frame.shape)
    face_detector = load_state_dict(torch.load('/home/shum/mapooon/SelfBlendedImages/src/preprocess/crop_retina_ff.py'))
    #face_detector = get_model("resnet50_2020-07-20", max_size=max(frame.shape),device=device)
    face_detector.eval()

    face_list=extract_face(frame,face_detector)
    
    #0.4S#	
    with torch.no_grad():
        
        img=torch.tensor(face_list).to(device).float()/255
       
        # torchvision.utils.save_image(img, f'test.png', nrow=8, normalize=False, range=(0, 1))
        pred=model(img).softmax(1)[:,1].cpu().data.numpy().tolist()
        
    print(f'fakeness: {max(pred):.4f}')

def a(weight_name,input_image):
    seed=1
    random.seed(seed)
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    device = torch.device('cuda')

    parser=argparse.ArgumentParser()
    #parser.add_argument('-w',dest='weight_name',type=str)
    #parser.add_argument('-i',dest='input_image',type=str)
    #args=parser.parse_args()
    
    #2.6S#
    a=time.time()
    model=Detector()
    model=model.to(device)
    
    cnn_sd=torch.load(weight_name)["model"]
    model.load_state_dict(cnn_sd)
    model.eval()

    image = cv2.imread(input_image)
    size = 512
# 获取原始图像宽高。
    height, width = image.shape[0], image.shape[1]
# 等比例缩放尺度。
    scale = height/size
# 获得相应等比例的图像宽度。
    width_size = int(width/scale)
# resize
    frame = cv2.resize(image, (width_size, size))
    #cout=frame.shape[1]*frame.shape[0]
    #print(cout)
    #if cout>250000:
        #cv2.resize(frame,(0,0),fx=250000/cout,fy=250000/cout)
        #print(frame.shape)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
#1.5S#
    #a=time.time()
    print(frame.shape)
    face_detector = get_model("resnet50_2020-07-20", max_size=max(frame.shape),device=device)
    #print(f'coast:{time.time() - a:.4f}s')
    face_detector.eval()
    #print(f'coast:{time.time() - a:.4f}s')
    face_list=extract_face(frame,face_detector)
    #print(f'coast:{time.time() - a:.4f}s')
    #0.4S#	
    with torch.no_grad():
        
        img=torch.tensor(face_list).to(device).float()/255
       
        # torchvision.utils.save_image(img, f'test.png', nrow=8, normalize=False, range=(0, 1))
        pred=model(img).softmax(1)[:,1].cpu().data.numpy().tolist()
        
    #print(f'fakeness: {max(pred):.4f}')
    t=time.time()-a
    d=dict()
    d['fakeness']=pred
    d['time']=t
    return (d)
    
def b(weight_name,input_image):
    seed=1
    random.seed(seed)
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    device = torch.device('cuda')

    parser=argparse.ArgumentParser()

    a=time.time()
    model=Detector()
    model=model.to(device)
    
    cnn_sd=torch.load(weight_name)["model"]
    model.load_state_dict(cnn_sd)
    model.eval()
    cap = cv2.VideoCapture(input_image)
    cout=40
    sum=0
    frame=cap.read()
    while (cap.isOpened ):

        sum+=1

        (frameState, frame) = cap.read()  # 记录每帧及获取状态

        if frameState == True and (sum % cout==0):
            #r,g,b,a=frame.split()              
            #frame=Image.merge("RGB",(r,g,b))
            frame=Image.fromarray(frame) 
            #filepic = r'/home/shum/mapooon/SelfBlendedImages/src/inference/pics/test.jpg'
            #cv2.imwrite(filepic, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            break
    image = cv2.imread(input_image)
    size = 512

    height, width = image.shape[0], image.shape[1]
# 等比例缩放尺度。
    scale = height/size
# 获得相应等比例的图像宽度。
    width_size = int(width/scale)
# resize
    frame = cv2.resize(image, (width_size, size))

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    
#1.5S#
    #a=time.time()
    print(frame.shape)
    face_detector = get_model("resnet50_2020-07-20", max_size=max(frame.shape),device=device)

    face_detector.eval()

    face_list=extract_face(frame,face_detector)

    with torch.no_grad():
        
        img=torch.tensor(face_list).to(device).float()/255
       
        # torchvision.utils.save_image(img, f'test.png', nrow=8, normalize=False, range=(0, 1))
        pred=model(img).softmax(1)[:,1].cpu().data.numpy().tolist()
        

    t=time.time()-a
    d=dict()
    d['fakeness']=pred
    d['time']=t
    return (d)




