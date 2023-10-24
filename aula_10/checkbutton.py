from tkinter import *

root = Tk()
v1 = IntVar(root)
v2 = StringVar(root)

c1 = checkButton(root, text='C1', variable=v1)
c1 = Checkbutton (text="V1", var=v1, command=exibe)
c2 = Checkbutton (text="V2", var=v2, command=exibe, onvalue="Sim", offvalue="Nao")
l = Label()

for w in (c1,c2,l):w.pack()
exibe()

def exibe():
    l.config (text="v1=%d,v2=%s"%(v1.get(),v2.get())) 