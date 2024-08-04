import cv2,time
from datetime import datetime
import argparse
import os
 
 
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
Video=cv2.VideoCapture(0)
while True:
    check,frame=Video.read()
    if frame is not None:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10)
        for x, y, w, h in face:
            img=cv2.rectangle(frame,(x,y),(x*w,y*h),(0,255,0),3)
        exact_time=datetime.now().strftime("%Y-%m-%d-%H-%s-%f")
        cv2.imwrite("face detected",str(exact_time),".jpg",img)    
        cv2.imshow("face detected",frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            ap=argparse.ArgumentParser()
            ap.add_argument("-ext","--extension",required=False,default='jpg')
            ap.add_argument("-0","--output",required=False,default='output.mp4')
            args=vars(ap.parse_args())
            
            dir_path=''
            ext=args['extension']
            output=args['output']
            image=[]
            for f in os.listdir(dir_path):
                image.append(f)
                
            image_path=os.path.join(dir_path,image[0])
            frame=cv2.imread(image_path)
            height,width,channels=frame.shape
            
            force=cv2.VideoWriter_force("mp4v")
            out=cv2.VideoWriter_force(output,force,5.0,(width,height))
            
            for image in image:  
                image_path=os.path.join(dir_path,image)
                frame=cv2.imread(image_path)
                out.write(frame) 
                
            break
        
        
Video.realeas() 
cv2.destroyAllWindows            
            
                
    
