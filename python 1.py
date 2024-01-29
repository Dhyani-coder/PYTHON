# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:59:13 2024

@author: user
"""

from tkinter import *

root=Tk()
root.title=("Ascii")

root.geometry=("400x400")
root.configure(background = 'snow')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "name in ascii  : ", bg+"light yellow", fg="black")

def asciiCoverter():
    input_word=enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        
btn=Button(root,text="show name in Ascii", command=asciiConverter, bg'gold' , fg= 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()        