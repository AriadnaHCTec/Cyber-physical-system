import os
import cv2
import random
from datetime import datetime

#1280 x 960
entries = os.listdir('/home/arihc/Cyber-physical-system/wrong/')
for i in entries:
    path = r'/home/arihc/Cyber-physical-system/wrong/'+str(i)    
    src = cv2.imread(path)
    cropped_image = src[400:660, 400:1190]
    cv2.imwrite("/home/arihc/Cyber-physical-system/wrong_cut/cropped"+str(datetime.now())+".png",cropped_image)
