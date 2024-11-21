num_pessoas = int (input("Informe a quantidade de pessoas: "))
num = 0 

for pessoa in range (num_pessoas):
    genero=input(f"Qual é o genero da {pessoa+1} pessoa (M/m) - Masculino; (F/f) - Feminino: ")
    if genero == "M" or genero == "m":
        num += 1
    else: 
        continue 
print (f"A quantidade de pessoas do sexo masculino são (é) de {num}.")


#Exercício 2


