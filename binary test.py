# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:17:22 2020

@author: shiba
"""
import cv2

img = cv2.imread("C:/Users/shiba/Pictures/7/binary.png",0)
img2 = cv2.imread("C:/Users/shiba/Pictures/7/binary.png")
print(img.shape[1])
#ここは高速化の余地ある
for i in range(img.shape[1]):
    if (img[1,i] != 0):
        img[1,i] = 255


img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
# 輪郭の検出

# 全ての輪郭を書き込んで出力
im_con = img2.copy()
cv2.drawContours(im_con, contours, -1, (0,255,0), 2)
cv2.imwrite("C:/Users/shiba/Pictures/7/binary_s.png", im_con)