
import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_eye.xml
# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# capture frames from a camera
cap = cv2.VideoCapture(1)
b=[0,0,0,0]
# loop runs if capturing has been initialized.
while True:


	ret, img = cap.read()

	# convert to gray scale of each frames
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detects faces of different sizes in the input image
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		c=[x,y,w,h]
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		r=[0,0,0,0]
		for i in range(4):
			r[i]=c[i]-b[i]
		print(r)
		b=[x,y,w,h]
		time.sleep(0.01)







	cv2.imshow('img',img)
	cv2.waitKey(1)


# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
