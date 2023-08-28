from ManipuladorDeArquivo import ManipuladorDeArquivo
import os


class Aluno:
    def __init__(self,nome,email,curso):
        self.nome = nome
        self.email = email
        self.curso = curso

    def salvaAluno(self):
        ManipuladorDeArquivo.criaArquivoAvulso("aluno_"+self.nome+".txt",self.nome + " " + self.email + " " +self.curso)


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



