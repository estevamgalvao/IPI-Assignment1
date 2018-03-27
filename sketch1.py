#cv2.imread(), cv2.imshow() , cv2.imwrite()



import numpy as np
import cv2

img = cv2.imread('Mars.bmp')

# blue = img[100,100,0]
# img.itemset((100,100,2), 65)

# = [.2126 * R^gamma + .7152 * G^gamma + .0722 * B^gamma
#print(blue)


for i in range(len(img)):
    for j in range(len(img[i])):
        blue_px = img[i,j,0]
        green_px = img[i, j, 1]
        red_px = img[i, j, 2]

        img[i, j, 0] = blue_px * 0.114
        img[i, j, 1] = green_px * 0.587
        img[i, j, 2] = red_px * 0.299
        img[i, j] = (blue_px+green_px+red_px)/3

        # img.itemset((i, j, 0),150)
        # img.itemset((i, j, 1),50)
        # img.itemset((i, j, 2),70)
cv2.imshow('Maars.bmp', img)
cv2.waitKey(0)
