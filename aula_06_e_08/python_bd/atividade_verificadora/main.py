from db import DbUtils
from aluno import Aluno
from nota import Nota
def main():
    db = DbUtils()

    while True:
        print("Menu:")
        print("1. Inserir um aluno")
        print("2. Buscar aluno por matricula ")
        print("3. Imprimir lista ordenada de todos os alunos e suas notas ")
        print("4. Imprimir alunos de um determinado curso")
        print("5. Sair do menu")
        
        command = input("Digite o comando: ")

        if command == "1":
            matricula = input("Digite a matrícula: ")
            nome = input("Digite o nome: ")
            curso = input("Digite o curso: ")

            aluno = Aluno(matricula, nome, curso)

            item_nota = input("Digite a que item a nota pertence: ")
            valor_nota = input("Digite o valor da nota: ")

            nota = Nota(item_nota, valor_nota, None)

            db.insert_aluno(aluno=aluno, nota=nota)
        elif command == "2":
            matricula = input("Digite a matrícula: ")
            print( db.selectByMatricula(matricula))
        elif command == "3":
            print(db.notaOrderByAlunoName())  
        elif command == "4":
            curso = input("Digite o curso: ")
            print(db.selectByCurso(curso=curso))       
        elif command == "5":
            break
        else:
            print("Comando inválido. Tente novamente.")



    

main()