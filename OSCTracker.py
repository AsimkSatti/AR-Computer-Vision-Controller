import cv2
import numpy as np

import argparse
import random
import time

import time
from pythonosc import osc_message_builder
from pythonosc import udp_client

#A UDP connection to Unity with OSC; running locally at port 8050
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8050, help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)



#Identifies Face
face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Identifies Eyes
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

# When Testing leave camera on
#But remember no two applications can use the simultaneously camera,
cap=cv2.VideoCapture(0)

 
        
#Class as we may want to send data about multiple faces     
class face:
    def __init__(self):
        #Ultimately want to find the center
        self.width_center=0
        self.height_center=0
        
    def set_width_center(self,x,w):
        self.width_center=(x+w)/2
    
    def set_height_center(self,y,h):
         self.height_center=(y+h)/2
    
    def get_width_center(self):
        return width_center
    
    def get_height_center(self):
        return height_center
    
    def FindFace(self):
        while True:
            #Convert to gray scale
            ret, img= cap.read()
            gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #Size of detection
            faces=face_cascade.detectMultiScale(gray, 1.2,5)

            for(x,y,w,h) in faces:
                #Visual
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,120,0),2)
                roi_gray=gray[y:y+h, x:x+w]
                roi_color=img[y:y+h , x:x+w]

                #Sets our data for Center
                self.set_width_center(x,w)
                self.set_height_center(x,w)

                
                #Sends our data as strings
                client.send_message("/filter",str(self.get_width_center))
                client.send_message("/filter",str(self.get_height_center))
                 

                #If you Like Eyes
                eyes=eye_cascade.detectMultiScale(roi_gray)
                for(ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (120,255,0), 1)
            #Output
            cv2.imshow('img', img)
            breaker=cv2.waitKey(30) &0xff
            #Destroy program with space key
            if breaker==32:
                break
        cap.release()
        cv2.destroyAllWindows


        
 


        
if __name__ == "__main__":
    my_face=face()
    my_face.FindFace()
 
    
