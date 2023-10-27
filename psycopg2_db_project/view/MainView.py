import tkinter as tk
from tkinter import ttk

class MainView:

    def __init__(self,win):
        #labels
        self.lblNome = tk.Label(win,text="Nome do Aluno")
        self.lblNota = tk.Label(win,text="Nota 1")
        self.lbNota2 = tk.Label(win,text="Nota 2")
        self.lblMedia = tk.Label(win,text="Media")
        
        #Entrys
        self.entryNome = tk.Entry(bd=3)
        self.entryNota1 = tk.Entry()
        self.entryNota2 = tk.Entry()

        #Buttons
        self.btnCalcular = tk.Button(win,text="Calcular",command=self.calcular)

        #treeView
        self.dadosColunas = ("Aluno","Nota 1","Nota 2","Media","Situação")
        
        self.treeMedias = ttk.Treeview(win,columns=self.dadosColunas,selectmode='browse')

        self.verscrollbar = ttk.Scrollbar(win,orient="vertical",command=self.treeMedias.yview)
        
        self.verscrollbar.pack(side='right',fill='x')

        self.treeMedias.configure(yscrollcommand=self.verscrollbar.set)

        self.treeMedias.heading("Aluno",text="Aluno")
        self.treeMedias.heading("Nota 1",text="Nota 1")
        self.treeMedias.heading("Nota 2",text="Nota 2")
        self.treeMedias.heading("Media",text="Media")
        self.treeMedias.heading("Situação",text="Situação")

        self.treeMedias.column("Aluno",minwidth=0,width=100)
        self.treeMedias.column("Nota 1",minwidth=0,width=100)
        self.treeMedias.column("Nota 2",minwidth=0,width=100)
        self.treeMedias.column("Media",minwidth=0,width=100)
        self.treeMedias.column("Situação",minwidth=0,width=100)

        self.treeMedias.pack(padx=10,pady=10)

        #Posicionamento
        self.lblNome.place(x=100,y=50)
        self.entryNome.place(x=200,y=50)

        self.lblNota.place(x=100,y=100)
        self.entryNota1.place(x=200,y=100)

        self.lbNota2.place(x=100,y=150)
        self.entryNota2.place(x=200,y=150)

        self.btnCalcular.place(x=100,y=200)
        
        self.treeMedias.place(x=100,y=300)
        self.verscrollbar.place(x=805,y=300,height=225)

        self.loadData()

    def calcular(self):
        return 0


    def loadData(self):
        #acessa o banco e pega os dados
        #controller.getAll()
        pass