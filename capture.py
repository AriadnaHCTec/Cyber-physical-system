#!/usr/bin/env python

import cv2
from datetime import datetime
  
vid = cv2.VideoCapture(0)
#vid.set(cv2.CAP_PROP_AUTOFOCUS, 0) # turn the autofocus off
while(True):
      
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	#400:660, 400:1190
	#cv2.rectangle(frame,(0,0),(100,200),(0,255,0),3)
	cut = frame[450:660, 400:1090].copy()
	cv2.rectangle(frame,(400,450),(1030,660),(0,255,0),3)
	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	key = cv2.waitKey(1) & 0xFF
	if key == ord('s'):
		cv2.imwrite("good/"+str(datetime.now())+".png",cut)		
		print("saving good image")
	elif key == ord('n'):
		cv2.imwrite("wrong/"+str(datetime.now())+".png",cut)
		print("saving bad image")
	elif key == ord('q'):
		break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()