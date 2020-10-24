# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:43:46 2020

@author: shiba
"""
import time
import win32gui
import win32process
import win32api

MOUSEEVENTF_LEFTDOWN = 0x2
MOUSEEVENTF_LEFTUP = 0x4

def click(left, top, right, bottom, l, t):
    win32api.SetCursorPos((left + l, top + t))
    time.sleep(0.1)
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)