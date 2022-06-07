n = int(input())

total = 0

totalC = 0
totalR = 0
totalS = 0

for i in range(n):
    numero, tipo = input().split()
    numero = int(numero)
    tipo = str(tipo)

    total += numero

    if tipo == "C":
        totalC += numero   

    elif tipo == "R":
        totalR += numero        

    elif tipo == "S":
        totalS += numero
        
    percentualC = (100 / total) * totalC
    percentualR = (100 / total) * totalR
    percentualS = (100 / total) * totalS

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {totalC}")
print(f"Total de ratos: {totalR}")
print(f"Total de sapos: {totalS}")
print(f"Percentual de coelhos: {percentualC:.2f} %")
print(f"Percentual de ratos: {percentualR:.2f} %")
print(f"Percentual de sapos: {percentualS:.2f} %")
