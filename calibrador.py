import cv2 as cv
import numpy as np

"""
Estos valores sirven para hacer un filtrado c
# HSV values for the mask
HH, SH, VH  = 182, 255, 134
HL, SL, VL = 0, 5, 0

    for i in range (0, 15):
        # Using cv2.erode() method 
        img_proce = cv.dilate(img_range, kernel) 
    cv.imshow("dilate", img_proce)

    for i in range (0, 5):
        # Using cv2.erode() method 
        img_proce = cv.erode(img_proce, kernel2)
    cv.imshow("erode", img_proce)
"""

# HSV values for the mask
HH, SH, VH  = 255, 255, 107
HL, SL, VL = 0, 108, 73

# Actions for the slider
# each slider modifies a hsv high or low value
def val_HH(value):
	global HH
	HH = value

def val_HL(value):
	global HL
	HL = value
    
def val_SH(value):
	global SH
	SH = value
    
def val_SL(value):
	global SL
	SL = value

def val_VH(value):
	global VH
	VH = value
    
def val_VL(value):
	global VL
	VL = value
               
               
# Create a window
img = cv.imread('C:/Users/52563/Desktop/7mo_semestre/sistemas_ciber_fisicos_2/computo_cognitivo/reto/codigos/good.png')
#img = np.zeros((1920,1080,3),np.uint8)
print ("leido")
img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    
cv.imshow("Imagen HSV Filtro",img)
print ("convertido")

# Create a slider for each HSV high and low value
cv.createTrackbar("H HIGH", "Imagen HSV Filtro", 0, 255, val_HH)
cv.createTrackbar("H LOW", "Imagen HSV Filtro", 0, 255, val_HL)
cv.createTrackbar("S HIGH", "Imagen HSV Filtro", 0, 255, val_SH)
cv.createTrackbar("S LOW", "Imagen HSV Filtro", 0, 255, val_SL)
cv.createTrackbar("V HIGH", "Imagen HSV Filtro", 0, 255, val_VH)
cv.createTrackbar("V LOW", "Imagen HSV Filtro", 0, 255, val_VL)

# Creating kernel
kernel = np.ones((6, 6), np.uint8)
kernel2 = np.ones((5, 5), np.uint8)
               
while True:
    cv.imshow("Imagen Original", img)
    
    img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    img_range = cv.inRange(img, (HL, SL, VL),(HH, SH, VH))
    cv.imshow("Imagen HSV Filtro", img_range)
    cv.imshow("Imagen range", img_range)

    
    for i in range (0, 5):
        # Using cv2.erode()method 
        img_proce = cv.erode(img_range , kernel2)
    cv.imshow("erode", img_proce)
    
    for i in range (0,12):
        # Using cv2.erode() method 
        img_proce = cv.dilate(img_proce, kernel) 
    cv.imshow("dilate", img_proce)
    
    img_wuuu = cv.bitwise_and(img,img,mask = img_proce)
    
    cv.imshow("wuuu", img_wuuu)
    
    if cv.waitKey(1) &0xFF == ord("q"):
        print ("q")
        break



