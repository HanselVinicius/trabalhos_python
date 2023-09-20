from ManipuladorDeArquivo import ManipuladorDeArquivo
from Aluno import Aluno

def main():
    numero = 0
    while numero != 100:
        try:
            numero = int(input(" 1- cadastra aluno \n 2- Lista alunos \n 3- Busca Certo Aluno \n 100- fechar : "))
            if(numero == 1):
                aluno = Aluno(str(input("Digite o nome do aluno: ")),str(input("Digite o email do aluno: ")),str(input("Digite o curso do aluno: ")),str(input("Digite a matricula do aluno: ")))
                aluno.salvaAluno()
            elif(numero == 2):
                Aluno.listaAlunos()
            elif(numero == 3):
                Aluno.buscaAluno(str(input("Digite o nome do aluno que deseja buscar: ")))
        except ValueError as e:
            print(e)

    






main()