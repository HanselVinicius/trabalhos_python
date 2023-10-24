from tkinter import *

root = Tk()
soma = DoubleVar(root)
parcela = DoubleVar(root)
def aritimetica():
    soma.set(parcela.get() + soma.get())


lSoma = Label(textvariable=soma)
eParcela = Entry(textvariable=parcela)
eParcela.bind('<Return>', lambda e: aritimetica())
lSoma.pack()
eParcela.pack()
mainloop()