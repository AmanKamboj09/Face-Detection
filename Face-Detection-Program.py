# Import cv2 and numpy
import cv2
import numpy as np

#Include the harcascade file
facesDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Open the camera
cam = cv2.VideoCapture(0)

# Infinite Loop
while(True):

    # Reading the live video
    ret,img = cam.read()

    #Convert the image into gray scale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Detect the faces in the image
    faces = facesDetect.detectMultiScale(gray,1.3,5)

    #Drawing rectangle of blue color on the faces
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    #Showing the image in another window
    cv2.imshow("Window",img)

    # To close the new window by pressing ESC key
    if cv2.waitKey(1) == 27:
        cam.release()
        cv2.destroyAllWindows()


