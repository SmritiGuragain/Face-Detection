import cv2
cat_face_data=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
img=cv2.imread('5.jpg')
gray_scale_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_coordinate=cat_face_data.detectMultiScale(gray_scale_image)
for(x,y,w,h) in face_coordinate:
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),3)
cv2.imshow('SujuCuteapp',img)
cv2.waitKey()
print('Done')