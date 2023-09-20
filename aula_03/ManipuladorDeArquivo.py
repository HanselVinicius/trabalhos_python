import os

class ManipuladorDeArquivo:

    def __init__(self,nome):
        self.nome = nome
        self.arquivo =  open(self.nome,'w')
        self.arquivo.close()    


    



    def criaArquivoAvulso(nomeArquivo,conteudo):
        try:
            arq = open(nomeArquivo,'w')
            arq.write(conteudo)
        except Exception as e:
            print("erro ao abrir o arquivo "+e )

  

    def escreveNoArquivo(self,txt):
        try:
            self.arquivo = open(self.nome,'a')
            self.arquivo.write(txt)
            self.arquivo.close()
        except Exception as e:
            print("erro ao escrever no arquivo " +e)

    def leArquivo(self):
        try:
            self.arquivo = open(self.nome,'r')
            conteudo = self.arquivo.read()
            self.arquivo.close()
            return conteudo
        except Exception as e:
            print("erro ao ler o arquivo "+e )

    def crescente(self):
        self.arquivo = open(self.nome,'a')
        numero = 0
        while numero != 101:
            self.arquivo.write(str(numero)+"\n ;")
            numero = numero+1


    def deletaArquivo(self):
        try:

            os.remove(self.nome)
        except Exception as e:
            print("erro ao deletar o arquivo " +e)    


    
