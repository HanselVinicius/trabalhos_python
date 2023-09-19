from db import DbUtils
from aluno import Aluno
from nota import Nota
def main():
    #todo
    db = DbUtils()
    aluno = Aluno('2','vinicius','ccp')
    nota = Nota('nota1','5',None) 
    db.insert_aluno(aluno=aluno,nota=nota)
    alunos = db.select_alunos()    
    notas = db.select_notas()

    for aluno in alunos:
        print(aluno.to_string())

    for nota in notas:
        print(nota.to_string())    

    db.updateAluno('henrique','bio',aluno.matricula)
    db.updateNota('prova1','100','2')
    alunos = db.select_alunos()    
    notas = db.select_notas()

    for aluno in alunos:
        print(aluno.to_string())
        
    for nota in notas:
        print(nota.to_string())  

main()