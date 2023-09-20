from ManipuladorDeArquivo import ManipuladorDeArquivo
import os


class Aluno:
    def __init__(self,nome,email,curso,matricula):
        self.nome = nome
        self.email = email
        self.curso = curso
        self.matricula = matricula
        self.validacoes()

    def validacoes(self):
        if self.nome == '' or self.email == '' or self.curso == '':
            raise ValueError("Nome, email e curso não podem ser vazios")

        if self.nome.isdigit() or not self.matricula.isdigit() :
            raise ValueError("Nome não pode conter digitos e matricula não pode conter caracteres ")




    def salvaAluno(self):
        ManipuladorDeArquivo.criaArquivoAvulso("aluno_"+self.nome+".txt",self.nome + " " + self.email + " " +self.curso + " " +self.matricula)


    def listaAlunos():
       for diret in os.listdir():
        if(diret.endswith('txt')):
            aluno = open(diret,'r')
            print(aluno.read())

    def buscaAluno(nome):
        for diret in os.listdir():
         if(diret.startswith("aluno_"+nome)):
            aluno = open(diret,'r')
            print(aluno.read())



