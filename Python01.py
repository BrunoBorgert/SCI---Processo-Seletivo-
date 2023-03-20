# BRUNO GUILHERME BORGERT - PYTHON

numeros = []
soma = 0

print("Seja bem vindo ao Sistema 0.1")
for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    soma += num

media = soma / len(numeros)
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números ímpares:", impares)
print("Média geral:", media)
print("Muito obrigado por utilizar nossos serviços.")
