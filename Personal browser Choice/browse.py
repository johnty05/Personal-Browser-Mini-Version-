from tkinter import*
import tkinter as tk
import json
import requests
import webbrowser
page = Tk()
page.title("CUSTOM BROWSER")
page.geometry("800x600")

def goog():
    webbrowser.open("www.google.com")
def face():
    webbrowser.open("www.facebook.com")
def ana():
    webbrowser.open("www.anaconda.org")
def you():
    webbrowser.open("www.youtube.com")
def amaz():
    webbrowser.open("www.amazon.com")

googObj = PhotoImage(file="goog.png")
googObj = googObj.zoom(2)
googObj = googObj.subsample(3)
goog = tk.Button(page,image=googObj,command=goog)
goog.grid(row=0,column=0)

faceObj = PhotoImage(file="face.png")
faceObj = faceObj.zoom(2)
faceObj = faceObj.subsample(3)
face = tk.Button(page,image=faceObj,command=face)
face.grid(row=0,column=1)

anaObj = PhotoImage(file="ana.png")
anaObj = anaObj.zoom(2)
anaObj = anaObj.subsample(3)
ana = tk.Button(page,image=anaObj,command=ana)
ana.grid(row=1,column=0)

youObj = PhotoImage(file="you.png")
youObj = youObj.zoom(2)
youObj = youObj.subsample(3)
you = tk.Button(page,image=youObj,command=you)
you.grid(row=1,column=1)

amazObj = PhotoImage(file="amaz.png")
amazObj = amazObj.zoom(2)
amazObj = amazObj.subsample(3)
amaz = tk.Button(page,image=amazObj,command=amaz)
amaz.grid(row=2,column=0)

page.mainloop()