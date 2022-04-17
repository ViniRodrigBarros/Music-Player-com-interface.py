import pygame
import os
from tkinter import *
cont=0
init=0
os.listdir("../musicas")
lista = []

for i in os.listdir("../musicas"):
    lista.append(i)
def playSong():
    musica = "../musicas/" + lista[cont]
    pygame.init()
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(-1)
    
def pauseSong():
    pygame.mixer.music.pause()

def unpauseSong():
    pygame.mixer.music.unpause()
def nextSong():
    global cont
    if (cont>0):
        pygame.mixer.music.stop()
    cont += 1
    if (cont >= len(lista) - 1):
        cont = len(lista) - 1
    playSong()
def backSong():
    global cont
    if (cont > 0):
        pygame.mixer.music.stop()
    cont = cont - 1
    playSong()
    if (cont < 0):
        cont = 0

master = Tk()
master.title("Music player")
master.geometry("354x460")
master.resizable(width=0,height=0)

img_fundo = PhotoImage(file="../imagens/backgorund.png")
img_play = PhotoImage(file="../imagens/play.png")
img_pause = PhotoImage(file="../imagens/pause.png")
img_dispause = PhotoImage(file="../imagens/despause.png")
img_next = PhotoImage(file="../imagens/next.png")
img_back = PhotoImage(file="../imagens/back.png")
lab_background = Label(master,image=img_fundo)
lab_background.pack()

#botão
bt_play= Button(master,bd=0,bg="#1C1030",image=img_play,command= playSong)
bt_play.place(width=37,height=37,x=163,y=330)

bt_pause= Button(master,bd=0,bg="#1C1030",image=img_pause,command=pauseSong)
bt_pause.place(width=31,height=31,x=224,y=334)


bt_dispause= Button(master,bd=0,bg="#1C1030",image=img_dispause,command=unpauseSong)
bt_dispause.place(width=31,height=31,x=112,y=334)

bt_next= Button(master,bd=0,bg="#1C1030",image=img_next,command=nextSong)
bt_next.place(width=31,height=31,x=276,y=334)

bt_back= Button(master,bd=0,bg="#1C1030",image=img_back,command=backSong)
bt_back.place(width=31,height=31,x=52,y=334)
master.mainloop()
