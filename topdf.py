# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 18:03:29 2020

@author: shiba
"""

    
from PIL import Image
import os
import cv2
import shutil

ct ="C:/Users/shiba/Pictures"

def topdf(k,dire,title):
    imagelist = [0]*(k-1)
    savename = str(1) + ".png"
    savename1 = os.path.join(dire,"re",savename)
    imsize = cv2.imread(savename1)
    height = imsize.shape[0]
    width = imsize.shape[1]
    im1 = Image.open(savename1).convert('RGB')
    for i in range(k-1):
        i = i + 2
        savename = str(i) + ".png"
        savename1 = os.path.join(dire,"re",savename)
        image = Image.open(savename1).convert('RGB')
        imagelist[i-2] = image
        pdfname = title + ".pdf"
        savepdf = os.path.join(ct,pdfname)
    print(imagelist)
    print("保存ディレクトリ",savepdf)
    im1.save(savepdf,save_all=True, append_images=imagelist, resolution=72)
    print("ファイル書き出し完了")
    im1.close()
    shutil.rmtree(dire)