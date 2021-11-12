# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:20:48 2020

@author: 用户
"""
from tkinter import *

def get_sum(event):
    labelText.set('num1')

root=Tk()
root.title('This is my title')

num1Entry=Entry(root)
num1Entry.pack(side=LEFT)
num1=num1Entry.get()

frame=Frame(root)
labelText=StringVar()
label=Label(frame, textvariable=labelText)
labelText.set('I am a label')
button=Button(frame, text='Click Me')
button.bind("<Button-1>",get_sum)


label.pack()
button.pack()
frame.pack()
root.mainloop() 

