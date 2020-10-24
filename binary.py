# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:12:35 2020

@author: shiba
"""

import cv2
import os

def start(path,dire):
    img = cv2.imread(path,0)
    #cv2.imwrite("C:/Users/shiba/Pictures/16/2_r.png", img)
    #ここで背景色の色を取得。
    print("ここで背景の色を取得します。")
    #イメージの左端の色を取得する。
    background = img[1,1]
    print("背景の色（255値）:",background)
    cl = 0
    if (background < 100):
        cl = cl + 1
        print("おそらくテキストタイプの本ではない（背景が暗い）タイプなので\n別のトリミング方法を実施します")
        for i in range(img.shape[1]):
            if (img[1,i] > background):
                print(i,"ここが画像の一番左の部分です")
                break
        for j in range(img.shape[1]):
            if (img[1,(img.shape[1] - j - 41)] > background):
                print(img.shape[1] - j - 41,"ここが画像の一番右の部分です")
                p = img.shape[1] - j - 42
                break
    # 閾値の設定
    print("背景の色を閾値にします")
    threshold = background + 1
    
    # 二値化(閾値100を超えた画素を255にする。)
    ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    
    # 二値化画像の表示
    savefileb = os.path.join(dire,"binary.png")
    cv2.imwrite(savefileb, img_thresh)
    if (cl==0):
        i = 0
        p = 0
    return savefileb, i, p, cl
