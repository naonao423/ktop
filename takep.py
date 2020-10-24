import subprocess
import time
import win32gui
import win32process
import win32api
import pyautogui as pgui
import os
from pywinauto import Application
from PIL import ImageGrab
import cv2
import numpy as np


import click
import triming
import binary

global endnum

def start(hw1,dire):  
    #アクティブ化   
    page = 1
    (left, top, right, bottom) = win32gui.GetWindowRect(hw1)
    print("left:",left, "  top:",top,"  right:", right,"  bottom:", bottom)
    
    #表紙に移動
    print("表紙に持っていきます")
    click.click(left, top, right, bottom, 40, 15)
    time.sleep(0.1)
    pgui.press('alt')
    pgui.press('right')
    pgui.press('right')
    pgui.press('enter')
    pgui.press('down')
    pgui.press('enter')

    #右送りか左送りかを判定
    print("ここで右送りか左送りかの検証を行います。")
    for i in range(2):
        click.click(left, top, right, bottom, 40, 15)
        pgui.press('right')
        time.sleep(0.5)
        savename = str(i) + ".png"
        savename1 = os.path.join(dire,savename)
        ImageGrab.grab().save(savename1)
    im1 = cv2.imread(os.path.join(dire,"0.png"))
    im2 = cv2.imread(os.path.join(dire,"1.png"))   
    if (np.array_equal(im1, im2) == True):
        print("右にはめくれなかったので左にめくります。")
        page = 1
    else:
        print("右にめくれました")
        page = 0
    pgui.press('left')
    pgui.press('left')
    os.remove(os.path.join(dire,"0.png"))
    os.remove(os.path.join(dire,"1.png"))
    
    #全画面にします（理由としてはそのあとのクリップに役立ちそうなので）
    print("全画面にします")
    pgui.press('f11')
    time.sleep(5)
    
    #トリミング領域の決定
    print("トリミングする領域を設定します")
    if (page == 1):
        pgui.press('left')
        time.sleep(1)
        pgui.press('left')
        time.sleep(1)
        pgui.press('left')
        time.sleep(1)
    else:
        pgui.press('right')
        time.sleep(1)
        pgui.press('right')
        time.sleep(1)
        pgui.press('right')
        time.sleep(1)   
    savename = "test" + ".png"
    savename1 = os.path.join(dire,savename)
    ImageGrab.grab().save(savename1)
    imgsz = cv2.imread(savename1)
    heights = imgsz.shape[0]
    savefileb,x_bigin,x_end,cl = binary.start(savename1,dire)
    if (cl == 1):
        print("binary.pyのほうの幅を参考にします")
        x_bigin1,x_end1,y_bigin,y_end = triming.start(savefileb, dire)
        y_bigin = 0
        y_end = heights
    else:    
        x_bigin,x_end,y_bigin,y_end = triming.start(savefileb, dire)
    print(x_bigin)
    print(x_end)
    print(y_bigin)
    print(y_end)
    if (page == 0):
        pgui.press('left')
        time.sleep(1)
        pgui.press('left')
        time.sleep(1)
        pgui.press('left')
        time.sleep(1)
    else:
        pgui.press('right')
        time.sleep(1)
        pgui.press('right')
        time.sleep(1)
        pgui.press('right')
        time.sleep(1)   
    
    #画像取り込み部分
    print("画像を取り込み始めます")
    end = 0
    dec = 0
    for i in range(1000):
        i = i + 1
        i = i - dec
        #click.click(left, top, right, bottom, 40, 15)
        savename = str(i) + ".png"
        savename1 = os.path.join(dire,savename)
        ImageGrab.grab().save(savename1)
        savefilecheck = str(i-1) + ".png"
        sfcpath =  os.path.join(dire,savefilecheck)
        print("iページ目：",savename1,end)
        imc1 = cv2.imread(os.path.join(savename1))
        imc2 = cv2.imread(os.path.join(sfcpath)) 
        img1 = imc1[y_bigin:y_end, x_bigin:x_end]
        height = img1.shape[0]
        width = img1.shape[1]
        img2 = cv2.resize(img1 , (int(width*1.5), int(height*1.5)))
        savename2 = os.path.join(dire,"re",savename)
        cv2.imwrite(savename2, img2)
        if (np.array_equal(imc1, imc2) == True):
            print("ページ飛びかもしれないのでもう一度実行します")
            end = end + 1
            dec = dec + 1
            os.remove(savename1)
            os.remove(savename2)
        else:
            end = 0
        if (end > 3):    
            print("最終ページに来ました取り込みを終わります。")
            endnum = i - 1
            print("最終ページ:",endnum)
            pgui.press('esc')
            return endnum
            break
        print("前ページと一致しなかったので次のページを取り込みます")
                #ページを一つ送る。
        if (end == 0):
            if (page == 1):
                pgui.press('left')
            else:
                pgui.press('right')
    
    
           