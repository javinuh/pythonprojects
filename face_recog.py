import cv2
import numpy as np
import face_recognition
import os

path = "imagefolder"
images = []
className = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    className.append(os.path.splitext(cl)[0])
def findEncoding(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeListknown = findEncoding(images)

cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    FaceCurFrame = face_recognition.face_locations(imgS)
    encodesFrame = face_recognition.face_encodings(imgS,FaceCurFrame)
    for encodeface,faceloc in zip(encodesFrame,FaceCurFrame):
        matches = face_recognition.compare_faces(encodeListknown,encodeface)
        facedis = face_recognition.face_distance(encodeListknown,encodeface)
        matchindex = np.argmin(facedis)
        if matches[matchindex]:
            name = className[matchindex].upper()
            y1,x2,y2,x1 = faceloc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    
   
    cv2.imshow('javinuh',img)
    k = cv2.waitKey(1)
    if k == 113: #113 = q
        break
cap.release()
cv2.destroyAllWindows()