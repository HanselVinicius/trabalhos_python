class Aluno:
    def __init__(self,id,nomeAluno,nota1,nota2):
        self.id =id
        self.nomeAluno = nomeAluno
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2)/2
        self.situacao = self.isAprovado(self.media)



    def isAprovado(self,media):
        if(media < 6):
            return 'Reprovado'
        return 'Aprovado'

    def getId(self):
        return self.id

    def getNomeAluno(self):
        return self.nomeAluno

    
    def getNota1(self):
        return self.nota1

    
    def getNota2(self):
        return self.nota2


    def getMedia(self):
        return self.media


    def getSituacao(self):
        return self.situacao

    def __str__(self):
        return f'id: {self.id} Aluno: {self.nomeAluno} Nota 1: {self.nota1} Nota 2: {self.nota2} Media: {self.media} Situação: {self.situacao}'