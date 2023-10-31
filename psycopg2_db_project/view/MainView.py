#UI
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
#bd
from controllers.school.SchoolController import SchoolController

#exceptions
from model.exceptions.DbException import DbException
from model.exceptions.ValidationException import ValidationException

#helper
from utils.utils import has_digits

from model.aluno.Aluno import Aluno
class MainView:

    def __init__(self,win):
        self.controller = SchoolController()
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
        self.btnInsert = tk.Button(win,text="Inserir",command=self.insertAluno)
        self.btnUpdate = tk.Button(win,text="Atualizar",command=self.atualizarAluno)
        self.btnDelete = tk.Button(win,text="Deletar",command=self.deletarAluno)

        #treeView
        self.dadosColunas = ("Aluno","Nota 1","Nota 2","Media","Situação")
        
        self.treeMedias = ttk.Treeview(win,columns=self.dadosColunas,selectmode='browse')

        self.verscrollbar = ttk.Scrollbar(win,orient="vertical",command=self.treeMedias.yview)
        
        self.verscrollbar.pack(side='right',fill='x')

        self.treeMedias.configure(yscrollcommand=self.verscrollbar.set)

        self.treeMedias.bind("<ButtonRelease-1>", self.get_selected_data)

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
        self.btnInsert.place(x=200,y=200)
        self.btnUpdate.place(x=300,y=200)
        self.btnDelete.place(x=400,y=200)
        
        self.treeMedias.place(x=100,y=300)
        self.verscrollbar.place(x=805,y=300,height=225)
        
        self.loadData()
        self.selectedItemId = None

    def calcular(self):
        try:
            self.validate()
            media = (float(self.entryNota1.get()) + float(self.entryNota2.get()))/2
            self.show_info_dialog("ALUNOS APLICATION ",f"A MEDIA DO ALUNO É {media}")
        except ValidationException as e:
            self.show_error_dialog("ALUNOS APLICATION ",e)
        except ValueError as e:
            self.show_error_dialog("ALUNOS APLICATION ","POR FAVOR COLOQUE NUMEROS DE 0 A 10 NOS CAMPOS DE NOTAS")


    def loadData(self):
        try:
            listaDeAlunos = self.controller.getAllData()
            self.treeMedias.delete(*self.treeMedias.get_children())
            for aluno in listaDeAlunos:
                self.treeMedias.insert("","end",iid=aluno.getId(),values=(aluno.getNomeAluno(),aluno.getNota1(),aluno.getNota2(),aluno.getMedia(),aluno.getSituacao()))
        except DbException as e:
            self.show_error_dialog("ALUNOS APLICATION ",e.message)
    
    
    def insertAluno(self):
        try:
           self.validate() 
           aluno = Aluno(id=None,nomeAluno=self.entryNome.get(),nota1=float(self.entryNota1.get()),nota2=float(self.entryNota2.get())) 
           listaDeAlunos = self.controller.insert(aluno=aluno)
           self.loadData()
           self.clear_entry()
        except DbException as e:
            self.show_error_dialog("ALUNOS APLICATION ",e.message)
        except ValidationException as e:
            self.show_error_dialog("ALUNOS APLICATION ",e)
        except ValueError as e:
            self.show_error_dialog("ALUNOS APLICATION ","POR FAVOR COLOQUE NUMEROS DE 0 A 10 NOS CAMPOS DE NOTAS")    

    def deletarAluno(self):
        try:
            self.controller.delete(id=self.selectedItemId)
            self.loadData()
            self.clear_entry()
        except DbException as e:
            self.show_error_dialog("ALUNOS APLICATION ",e.message)    

    def atualizarAluno(self):
        try: 
            self.validate()
            aluno = Aluno(id=self.selectedItemId,nomeAluno=self.entryNome.get(),nota1=float(self.entryNota1.get()),nota2=float(self.entryNota2.get()))
            self.controller.update(aluno=aluno)
            self.loadData()
            self.clear_entry()
        except DbException as e:
            self.show_error_dialog("ALUNOS APLICATION ",e.message)    

    def show_error_dialog(self, title, message):
        messagebox.showerror(title, message)


    def show_info_dialog(self, title, message):
        messagebox.showinfo(title, message)

    def get_selected_data(self, event):
        selected_item = self.treeMedias.selection()  

        if selected_item:  
            values = self.treeMedias.item(selected_item, "values")
            if values:
                self.clear_entry()
                self.entryNome.insert(0,values[0])
                self.entryNota1.insert(0,values[1])
                self.entryNota2.insert(0,values[2])
                self.selectedItemId = selected_item[0]
                



    def clear_entry(self):
        self.entryNome.delete(0,tk.END)
        self.entryNota1.delete(0,tk.END)
        self.entryNota2.delete(0,tk.END)

    #gostaria de aplicar um strategy pattern aqui porém talvez seja muito bazuca pra matar barata
    def validate(self):
        if self.entryNome.get() == "" or self.entryNota1.get() == "" or self.entryNota2.get() == "":
            raise ValidationException(message="ENTRADAS INVALIDAS")

        if has_digits(self.entryNome.get()):
            raise ValidationException(message="ENTRADA INVALIDA NO CAMPO NOME")

        if float(self.entryNota1.get()) < float("0") or float(self.entryNota1.get()) > float("10") or float(self.entryNota2.get()) < float("0") or float(self.entryNota2.get()) > float("10"):
            raise ValidationException(message="ENTRADA INVALIDA NO CAMPO NOTA")      