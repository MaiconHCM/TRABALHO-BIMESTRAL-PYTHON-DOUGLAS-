numero=int(input("Quantas interações quer realizar?\n"))
anterior = 0
proximo = 0
for i in range(numero):
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo += 1