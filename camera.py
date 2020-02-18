import numpy as np
import cv2

cap = cv2.VideoCapture(0)
for  x in range(8,16):
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',frame)
		img_item = str(x) + ".png"
		if cv2.waitKey(20) & 0xFF == ord('q'):
			cv2.imwrite(img_item,frame)
			break
cap.release()
cv2.destroyAllWindows()
