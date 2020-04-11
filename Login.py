# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:43:45 2020

@author: USER
"""



from tkinter import *


def center_window(width=300, height=200):               #sirve para declarar y obtener que la ventana se habra en el centro de la pantalla
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))



root=Tk()

center_window(600, 650)  #Da indicaciones de donde esta el centro de pantalla


root.title("Globe Environmental Dynamics")
root.config(bg="deepskyblue4")
root.geometry("600x600")
root.resizable(1,1)
root.iconbitmap("logotk.ico")
root.resizable(0,0) 


miFrame=Frame(root, width=600, height=600)
miFrame.config(bg="deepskyblue4")
miFrame.pack()


miImagen=PhotoImage(file="cienciaresize.png")


Label(miFrame,image=miImagen,bg="deepskyblue4").place(x=200,y=225)


miLabel=Label(miFrame,text="By Luis Azabache Loyola",bg="deepskyblue4",fg="white",font=("comic Sans MS",7))
miLabel.place(x=294,y=300)


root.mainloop()

#Agrego para confirmar