#skimage.io.imread()
#skimage.color.rgb2gray()
import os
import inference_image
data_dir = 'lfw/'#文件地址/名称
classes = os.listdir(data_dir)
a=0
b=0
import time
t=time.time()
for cls in classes:
    files = os.listdir(data_dir+cls)
    for f in files:        
        print(data_dir+cls+"/"+f)
        d=dict()
        d=inference_image.a('/home/shum/mapooon/SelfBlendedImages/weights/FFraw.tar',data_dir+cls+"/"+f)
        a=a+1
        if d['fakeness'][0]>0.4:
            b=b+1
    if a==1000:
        break 
print(a,b,time.time()-t)
