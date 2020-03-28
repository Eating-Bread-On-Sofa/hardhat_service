#!/usr/bin/env python
# coding=utf-8
 
import os
import cv2
import base64
from flask import Flask
from flask import render_template
from flask import request
#from nameko.standalone.rpc import ClusterRpcProxy
 
#UPLOAD_FOLDER = '/mine/hardhat_service/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
#app.config = ['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
def detect(img_path):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    detector = cv2.CascadeClassifier('hardhat.xml')
    hardhats = detector.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in hardhats:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #cv2.imshow('frame',img)
    #cv2.waitKey(500)
    cv2.imwrite(img_path,img)
    with open(img_path, 'r') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream

@app.route('/hardhat',methods = ['GET','POST'])
def front_page():
    img_path = './test.jpg'
    if request.method == 'POST':
        f = request.files['the_file']
        f.save(img_path)
        img_stream = detect(img_path)
        return render_template('index.html',
                               img_stream=img_stream)
     
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
