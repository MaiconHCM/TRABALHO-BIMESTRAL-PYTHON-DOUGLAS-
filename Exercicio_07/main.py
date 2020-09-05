print("Insira o ano para cálculo da páscoa:")

year=int(input())

a = year % 19
b = year // 100
c = year % 100
d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
mes = f // 31
dia = f % 31 + 1

mes_str=""
if(mes==3):
    mes_str="março"
else:
    mes_str = "abril"

print(f'A páscoa será no dia {dia} do mês de {mes_str}')