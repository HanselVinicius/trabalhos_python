from tkinter import *

def abrir(): print ('abrir')
def salvar(): print ('salvar')
def ajuda() : print ('ajuda')

root = Tk()
menuBar = Menu(root)
arquivo = Menu(menuBar)
arquivo.add_command(label='Abrir', command=abrir)
arquivo.add_command(label='Salvar', command=salvar)
menuBar.add_cascade(label='Arquivo', menu=arquivo)
menuBar.add_command(label='Ajuda', command=ajuda)
root.config(menu=menuBar)
root.mainloop()