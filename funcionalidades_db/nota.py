class Nota:
   

    def __init__(self,item,valor,matricula):
        self.item = item
        self.valor = valor
        self.matricula = matricula


    def to_string(self):
        print(self.item,self.valor,self.matricula)