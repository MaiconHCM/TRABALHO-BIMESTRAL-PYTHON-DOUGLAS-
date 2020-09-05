import webbrowser
continuar = True
while continuar:
    print('Escolha uma opção:\n'
          '1-Descobrir se número é par ou impar.\n'
          '2-Sair do programa.')
    opcao_str = input()
    try:
        opcao = int(opcao_str)
    except:
        webbrowser.open('https://pt.wikipedia.org/wiki/N%C3%BAmero_inteiro')
        print(f'Erro: O valor inserido "{opcao_str}" não é um número inteiro! Tente novamente.')
        continue
    if opcao == 1:
        numero_str = input("Insira o número inteiro:\n")
        try:
            numero = int(numero_str)
            if numero%2==0:
                print(f"O número {numero_str} é par")
            else:
                print(f"O número {numero_str} é impar")
        except:
            print(f"A gente fala número e o cara escreve {numero_str}. Se ajude cara.")
            webbrowser.open('https://pt.wikipedia.org/wiki/N%C3%BAmero_inteiro')
    elif opcao == 2:
        print("Programa está encerrando! Salve para os amigos do MEC que estão nos acompanhando.")
        continuar = False
    else:
        print(f'A opção "{opcao_str}" não existe! Tente novamente.')
