import cv2
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam=cv2.VideoCapture(0)
while True:
    sucessfull_frame_read,frame=webcam.read()
    grey_scale_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_coordinate=trained_face_data.detectMultiScale(grey_scale_frame)
    for (x,y,w,h) in frame_coordinate:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(225,0,0),3)
    cv2.imshow('Smriti FaceDetector',frame)
    key= cv2.waitKey(1)
    if key==81 or key==113:
        break;
