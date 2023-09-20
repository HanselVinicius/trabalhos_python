def crescente():
        arquivo = open("crescente.txt",'w')
        numero = 0
        while numero != 101:
            arquivo.write(str(numero)+"; \n")
            numero = numero+1
        arquivo.close()

crescente()
