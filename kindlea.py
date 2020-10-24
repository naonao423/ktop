# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:46:28 2020

@author: shiba
"""

import subprocess
import time
import win32gui
import win32process
import win32api
import os

MOUSEEVENTF_LEFTDOWN = 0x2

MOUSEEVENTF_LEFTUP = 0x4

#mymodule
import getbandle
import takep
import topdf

#save folderの作成。

#フォトフォルダに作成
ct ="C:/Users/shiba/Pictures"

for fnum in range(100):
    dire = os.path.join(ct,str(fnum))
    if (os.path.exists(dire) == True):
        print("すでに",fnum,"のフォルダはあるので次の番号を振り分けます")
    else:
        os.mkdir(dire)
        dire1 = os.path.join(dire,"re")
        os.mkdir(dire1)
        break
print("今回は",dire,"に保存します")

def main():
    #kindleのバンドルを取得するmodule hw1はバンドル番号
    hw1, hw0, tid0, tid1, pid0, pid, title = getbandle.start()
    
    #ページを送りスクリーンショットをとる部分。
    endnum = takep.start(hw1,dire)
    if (endnum < 20):
        print("もしかしたら画像をめくる速さが早いかも？","\n","takep.py内のpress後のsleep値を増やしてみて！")
    win32process.AttachThreadInput(tid0, tid1, True)
    win32gui.BringWindowToTop(hw0)
    win32process.AttachThreadInput(tid0, tid1, False)

    topdf.topdf(endnum,dire,title)
    
    
if __name__ == '__main__':
    main()