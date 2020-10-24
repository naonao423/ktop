# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:14:53 2020

@author: shiba
"""

import cv2
import numpy as np
import scipy
from scipy import signal
import math
s = "C:/Users/shiba/Pictures/11/1.png"
colors = (0,255,0), (255,0,255)
max_dist_between_points = .25

# Get contours
img = cv2.imread(s)
gray = 255-cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 123, 123)
f,contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

def distance(a,b): return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def max_dist(points):
    max_dist = 0
    for i in range(len(points)-1):
        dist = distance(points[i], points[i+1])
        if dist > max_dist: max_dist = dist
    return max_dist
def interpolate(points):
    interpolated = [points[0]]
    for i in range(len(points)-1):
        a,b = points[i], points[i+1]
        dist = distance(a,b)
        if dist >= max_dist_between_points:
            midpoint = (a[0]+b[0])/2, (a[1]+b[1])/2
            interpolated.append(midpoint)
        interpolated.append(b)
    return interpolated


# Iterate through each contour
print(contours)
for contour in contours:

    # Reformat the contour into two lists of X and Y values
    points, new_points = list(contour), []
    for point in points: new_points.append(tuple(point[0]))
    points = new_points

    # Interpolate the contour points so that they aren't spread out
    while max_dist(points) > 2:
        print(len(points))
        points = interpolate(points)
    X, Y = zip(*points)

    # Define smoothing parameters
    window_length, polyorder = 5, 3
    # Smoooth
    X = signal.savgol_filter(X, window_length, polyorder)
    Y = signal.savgol_filter(Y, window_length, polyorder)
    # Re zip and iterate through the points
    smooth = list(zip(X,Y))
    for point in range(len(smooth)):
        a,b = smooth[point-1], smooth[point]
        a,b = tuple(np.array(a, int)), tuple(np.array(b, int))
        cv2.line(img, a, b, colors[contours.index(contour)], 2)   

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()