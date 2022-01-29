import cv2
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('pariwar.jpg')
greyscale_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinate=trained_face_data.detectMultiScale(greyscale_image)
for (x,y,w,h) in face_coordinate:
#(x,y,w,h)=face_coordinate[1]
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
cv2.imshow('Smriti app',img)
cv2.waitKey()