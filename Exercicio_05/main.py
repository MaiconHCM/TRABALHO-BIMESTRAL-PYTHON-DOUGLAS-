numero=int(input("Quantas palavras você deseja armazenar?\n"))
lista=[]
for i in range(numero):
    lista.append(input(f'Insira uma palavra ({i+1} de {numero})\n'))
maior_string = max(lista, key=len)
print(f'A maior string é {maior_string} com o total de {len(maior_string)} caracteres')