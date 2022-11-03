#!/usr/bin/env python

import cv2
from datetime import datetime
  
vid = cv2.VideoCapture(0)

while(True):
      
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
		
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	key = cv2.waitKey(1) & 0xFF
	if key == ord('s'):
		cv2.imwrite("good/"+str(datetime.now())+".png",frame)		
		print("saving good image")
	elif key == ord('n'):
		cv2.imwrite("wrong/"+str(datetime.now())+".png",frame)
		print("saving good image")
	elif key == ord('q'):
		break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()