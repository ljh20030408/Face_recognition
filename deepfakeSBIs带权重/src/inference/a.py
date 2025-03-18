import os 
import time
import inference_image
import cv2 as cv
def predict(a):
	t = time.time()
	path =a
	#image= cv.imread(path)
	#cout=image.shape[1]*image.shape[0]
	#if cout>250000:
		#cv.resize(image,(0,0),fx=250000/cout,fy=250000/cout)
		
	return(inference_image.a('/home/shum/mapooon/SelfBlendedImages/weights/FFraw.tar',path))
	#image = cv.imread(path) 
	#os.system('CUDA_VISIBLE_DEVICES=0 python3 /home/shum/mapooon/SelfBlendedImages/src/inference/inference_image.py -w /home/shum/mapooon/SelfBlendedImages/weights/FFraw.tar -i '+path)
	print(f'coast:{time.time() - t:.4f}s')

#predict('/home/shum/mapooon/SelfBlendedImages/data/Celeb-DF-v2/2.jpg')	
