# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:21:14 2020

@author: shiba


"""
import cv2
import pyautogui as pgui
import time
import os
from PIL import ImageGrab

def start(savefileb,dire):    
    img = cv2.imread(savefileb,0)
    
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    contours2 = contours[0]
    x_bigin = contours2[1,0,0]
    print(x_bigin)
    x_end = contours2[3,0,0]
    print(x_end)
    y_bigin = contours2[0,0,1]
    print(y_bigin)
    y_end = contours2[1,0,1]
    print(y_end)
    
    
    return x_bigin,x_end,y_bigin,y_end

