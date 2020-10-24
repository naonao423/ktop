# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:42:01 2020

@author: naona
"""

import tkinter as tk
from tkinter import ttk 
#import Kindle_A
import tests
import kindlea

def main():   
    #tkinterの初期設定。
    root = tk.Tk()
    root.configure(background="white")
    root.title("to pdf in Kindle")
    root.geometry("400x400")
    
    def clicked1(event):
        entry1.configure(state='normal')
        #entry1.insert(tk.END,"OK!")
        answer = tests.cal()
        entry1.insert(tk.END,answer)
        entry1.configure(state='readonly')
        
    def clicked2(event):    
        root.destroy()
    
    #今回は機能は簡潔に
    lv1 = tk.Label(root,text="kindleをpdfにするソフト")
    lv1.place(x=30,y=20,width=250,height=30)
    lv1.configure(background='white')

    #エントリー
    entry1 = tk.Entry(root)
    entry1.place(x=25,y=50,width=350,height=30)
    lv1.configure(background='white')
    entry1.configure(state='readonly')
    
    #ボタン設定
    botton1 = tk.Button(root,text="start")
    botton2 = tk.Button(root,text="exit")
    botton1.bind("<Button-1>",clicked1)
    botton2.bind("<Button-1>",clicked2)
    botton1.place(x=25,y=95,width=150,height=30)
    botton2.place(x=200,y=95,width=150,height=30)

    

        
    root.mainloop()
if __name__ == '__main__':
    main()