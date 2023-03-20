# BRUNO GUILHERME BORGERT - PYTHON

print("Sistema Python 05")
matriz = [[0] * 4 for i in range(3)]

medias = []

for i in range(3):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    soma = 0
    for j in range(4):
        nota = float(input("Digite a nota {} do aluno {}: ".format(j+1, nome)))
        soma += nota
        matriz[i][j] = nota
    media = soma / 4
    medias.append(media)
    print("Média do aluno {}: {:.2f}\n".format(nome, media))

maior_media = max(medias)
menor_media = min(medias)
indice_maior_media = medias.index(maior_media)
indice_menor_media = medias.index(menor_media)

# imprimindo os resultados
print("Aluno com maior média: {}".format(input("Digite o nome do aluno {}: ".format(indice_maior_media+1))))
print("Aluno com menor média: {}".format(input("Digite o nome do aluno {}: ".format(indice_menor_media+1))))
