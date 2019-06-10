from datetime import datetime
import numpy as np
import cv2


path = '/home/antoniogarcia/anaconda3/lib/python3.6/site-packages/cv2/data/haarcascades/'
faceCascade = cv2.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height


def fr_light(ms, callback):

    min_time = ms / 1000 # set minimum required time in milliseconds
    count = 0

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )

        if faces == ():
            detect_face = False
        else:
            # Set start timestamp
            if not detect_face:
                detect_face = True
                start = datetime.now()
            # Set end, total timestamp
            end = datetime.now()
            total_time = end - start
        
            # Draw a rectangle around the face
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            
            for index in range(len(faces)):
                # Wait N seconds for callback
                if total_time.seconds >= min_time:
                    count += 1
                    # Return path and image
                    path_img =  ("dataset/User." + str(index) + '.' + str(count) + ".jpg")
                    face_img = gray[y:y+h,x:x+w]
                    callback(path_img, face_img)
            
        cv2.imshow('video',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
    cap.release()
    cv2.destroyAllWindows()