import base64
from flask import request
from flask import Flask
import os
import a
import inference_image
from flask_sqlalchemy import SQLAlchemy
import configs
import time as TIME
import pymysql
from flask_cors import CORS
import cv2
from PIL import Image
import numpy as np
app=Flask(__name__)
CORS(app,resources=r'/*')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:clz1515@101.43.93.152:3306/face_info?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy()
db.init_app(app)
class records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    authenticity = db.Column(db.Integer)
    time = db.Column(db.String)
    confidence=db.Column(db.String)
    ip = db.Column(db.String)


# 定义路由
@app.route("/photo", methods=['POST'])
def photo():


    # 接收图片
    upload_file = request.files['file']
    data = request.get_data()
    #print (request.form)
    ips= request.form['ipaddr']
    print(ips)
    # 获取图片名
    file_name = upload_file.filename
    #ips= upload_file.ipaddr
    # 文件保存目录（桌面）
    file_path=r'/home/shum/mapooon/SelfBlendedImages/src/inference/pics'
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        # 随便打开一张其他图片作为结果返回，
       # with open(r'C:/Users/Administrator/Desktop/1001.jpg', 'rb') as f:
            #res = base64.b64encode(f.read())
            #return res
    di=dict()
    di=inference_image.a('../../weights/FFraw.tar',file_paths)        
    #return(inference_image.a('/home/shum/mapooon/SelfBlendedImages/weights/FFraw.tar',file_paths))
    os.remove(file_paths)
    print(request)
    #ips = request.remote_addr
    now = int(round(TIME.time()*1000))
    now02 = TIME.strftime('%Y-%m-%d %H:%M:%S',TIME.localtime(now/1000))
    #ips ='1'
    key='1'
    conf=di['fakeness']
    #print(conf)
    
    if conf[0]> 0.6:
        key='0'
    record=records(authenticity=key,time=now02,confidence=di['fakeness'],ip=ips)
    db.session.add(record)
    db.session.commit()
    return(di)
@app.route("/video", methods=['POST'])
def video():
    
    upload_file = request.files['file']
    

    
    data = request.get_data()
    ips= request.form['ipaddr']
    # 获取图片名
    file_name = upload_file.filename
    # 文件保存目录（桌面）
    file_path=r'/pics'
    filepic=r''
    if upload_file:
        File_paths = os.path.join(file_path, file_name)
        upload_file.save(File_paths)

		  
    di=dict()
    di=inference_image.b('../../weights/FFraw.tar',File_paths)        
    os.remove(filepic)
    print(request)
    now = int(round(TIME.time()*1000))
    now02 = TIME.strftime('%Y-%m-%d %H:%M:%S',TIME.localtime(now/1000))
    key='1'
    conf=di['fakeness']
    
    if conf[0]> 0.6:
        key='0'
    record=records(authenticity=key,time=now02,confidence=di['fakeness'],ip=ips)
    db.session.add(record)
    db.session.commit()
    return(di)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)