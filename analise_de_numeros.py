numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / 5
maior_valor = max(numeros)
menor_valor = min(numeros)

print("Soma dos números:", soma)
print("Média dos números:", media)
print("Maior valor:", maior_valor)
print("Menor valor:", menor_valor)