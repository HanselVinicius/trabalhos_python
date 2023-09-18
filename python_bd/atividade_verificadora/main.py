from db import DbUtils

def main():
    #todo
    db = DbUtils()
    db.insert_aluno('2','vinicius','ccp',None)
    alunos = db.select_alunos()    
    notas = db.select_notas()

    for aluno in alunos:
        print(aluno.to_string())

    for nota in notas:
        print(nota.to_string())    

    db.updateAluno('henrique','bio','2')
    db.updateAluno('prova1','100','2')
    alunos = db.select_alunos()    
    notas = db.select_notas()

    for aluno in alunos:
        print(aluno.to_string())
        
    for nota in notas:
        print(nota.to_string())  

main()