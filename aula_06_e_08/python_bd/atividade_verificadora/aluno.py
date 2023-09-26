class Aluno:
   

    def __init__(self,matricula,nome,curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
    


    def to_string(self):
        print(self.matricula,self.nome,self.curso)