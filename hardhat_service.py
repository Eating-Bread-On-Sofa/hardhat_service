from nameko.rpc import rpc

import cv2

import os

import base64

class HardhatService:

    name = "hardhat_service"

    @rpc
    def detect(self,stream):

        img_stream = stream

        deimg_stream = base64.b64decode(img_stream)

        imgpath = "/home/wangxuanzhe/image/test.jpg"

        with open(imgpath,'wb') as fp:

            fp.write(deimg_stream)

        #imgpath = path

        img = cv2.imread(imgpath)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        detector = cv2.CascadeClassifier('hardhat.xml')

        hardhats = detector.detectMultiScale(gray, 1.2, 5)

        for (x,y,w,h) in hardhats:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #cv2.imshow('frame',img)

        #cv2.waitKey(500)

        cv2.imwrite(imgpath,img)

        with open(imgpath, 'r') as img_f:
            
            img_stream = img_f.read()
            
            img_stream = base64.b64encode(img_stream)

        return img_stream

        

