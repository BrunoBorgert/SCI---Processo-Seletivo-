# BRUNO GUILHERME BORGERT - PYTHON

print("Seja bem vindo ao Sistema 0.3")

while True:
    nome = input("Digite o nome do aluno: ")
    notas = []

    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno: "))
        notas.append(nota)

    media = sum(notas)/len(notas)

    if media >= 6:
        print(f"O aluno {nome} foi Aprovado com média {media:.2f}.")
    else:
        print(f"O aluno {nome} foi Reprovado com média {media:.2f}.")

    opcao = input("Digite sim para continuar ou não para encerrar o programa: ")

    if opcao == "nao":
        print("Obrigado por utilizar nossos serviços")
        break
