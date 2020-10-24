# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:27:52 2020

@author: shiba
"""

import subprocess
import time
import win32gui
import win32process
import win32api
import ctypes

MOUSEEVENTF_LEFTDOWN = 0x2
MOUSEEVENTF_LEFTUP = 0x4

exceptw = [":" ,"|" ,"/" ,"*",">" ,"<" ,"?"] 

EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
# ??
EnumWindows = ctypes.windll.user32.EnumWindows

global hw1, hw0, tid0, tid1, pid0, pid1

def start():
    title = []
    hw0 = win32gui.GetForegroundWindow()
    (tid0, pid0) = win32process.GetWindowThreadProcessId(hw0)
    print("spyderのハンドル番号；",hw0)
    print("今使っているkindleのウィンドウを最大化にしてアクティブ化してください","\n","10秒待ちます")
    for i in range(3):
        time.sleep(1)
        print(".")
    #kindleのハンドル取得
    hw1 = win32gui.GetForegroundWindow()
    print("kindleのハンドル番号；",hw1)
    (tid1, pid1) = win32process.GetWindowThreadProcessId(hw1)
    #print(win32process.GetWindowThreadProcessId(hw1))


    # タイトル格納用変数

    def foreach_window(hwnd, lparam):
        if ctypes.windll.user32.IsWindowVisible(hwnd):
            length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
            buff = ctypes.create_unicode_buffer(length +1)
            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
            title.append(buff.value)

            return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)
    #print(title)
    #print(len(title))
    for k in title:
        w = "Kindle" in k
        if (w == True):
            moji = k.split('-')[1]
            print("今開いているkindleののタイトルは",moji,"です。")
            for word in exceptw:
                if word in moji:
                    moji = moji.split(word)
            print("切り取られた後のタイトル",moji)
            if (type(moji) == list):
                moji = moji[0]
            break
        
    return hw1, hw0, tid0, tid1, pid0, pid1, moji