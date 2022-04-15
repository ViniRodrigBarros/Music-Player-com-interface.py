from tkinter import *

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

#boatão
bt_play= Button(master,bd=0,bg="#1C1030",image=img_play)
bt_play.place(width=37,height=37,x=163,y=330)

bt_pause= Button(master,bd=0,bg="#1C1030",image=img_pause)
bt_pause.place(width=31,height=31,x=224,y=334)


bt_dispause= Button(master,bd=0,bg="#1C1030",image=img_dispause)
bt_dispause.place(width=31,height=31,x=112,y=334)

bt_next= Button(master,bd=0,bg="#1C1030",image=img_next)
bt_next.place(width=31,height=31,x=276,y=334)

bt_back= Button(master,bd=0,bg="#1C1030",image=img_back)
bt_back.place(width=31,height=31,x=52,y=334)

while True:
    master.mainloop()