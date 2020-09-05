lista = [];
for i in range(3):
    numero_str = input(f"Insira o número ({i + 1} de 3 necessários): ");
    try:
        numero = int(numero_str)
    except:
        print(f'Erro: O valor inserido "{numero_str}" não é um número inteiro! Tente novamente.')
        break
    else:
        lista.append(numero)
if len(lista) == 3:
    igual = all(item == lista[0] for item in lista)
    if igual:
        print(f"Todos são iguais então é vezes: {lista[0]} x {lista[0]} x {lista[0]} = {lista[0]*lista[0]*lista[0]}")
    else:
        print(f"Possuí valor diferente então é soma:{lista[0]} + {lista[1]} + {lista[2]} = {sum(lista)} ")