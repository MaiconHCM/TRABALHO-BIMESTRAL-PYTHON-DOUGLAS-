vitorias=int(input("Insira o número de vítorias:\n"))
empates=int(input("Insira o número de empates:\n"))
derrotas=int(input("Insira o número de derrotas:\n"))

print("Bom dia pessoal de esporte, hoje apresentamos a pontuação no MaterDei SPORTS:\n")
print("A regra de pontuação é a seguinte:Vitória = 3 pontos\nEmpate = 1\nDerrota = Não pontua")
print("No caso do Time Géri SPORT CLUB, sua pontuação foi de:")
print(f"Vítorias:{vitorias}, Pontos:{vitorias*3}")
print(f"Empates:{empates}, Pontos:{empates*1}")
print(f"Derrotas:{derrotas}")
print(f"======Pontuação final: {(vitorias*3)+(empates*1)}======")

print("Valeu professor por suas aulas, tu é top!\nSalve galera do mec que nos acompanha!\nAluno: Maicon Henrique Cordeiro Machado")