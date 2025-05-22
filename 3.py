import random
matriz = []
somaprovas = 0
maior = 0
somatrabalhos = 0
for i in range(5):
    linha = []
    for j in range(4):
        if j == 0:
            ##numero da matricula
            matricula = random.randint(0,10)
            linha.append(matricula)
        elif j == 1:
            ##media das provas
            provas = random.randint(0,10)
            somaprovas += provas
            mediaprovas = somaprovas /5
            linha.append(provas)
        elif j == 2:
            ##media dos trabalhos
            trabalhos = random.randint(0,10)
            somatrabalhos += trabalhos
            mediatrabalhos = somatrabalhos /5
            linha.append(trabalhos)
        elif j == 3:
            ## nota final
            media = sum(linha) / 3
            if maior < media:
                maior = media
                posicao = i
            linha.append(media)
    matriz.append(linha)
for linhas in matriz:
    print(f"o aluno tirou as seguintes notas {linhas[0], linhas[1],linhas[2]}")
notaFinal = mediaprovas + mediatrabalhos
print(notaFinal)
print(f"o aluno de matricula {matriz[posicao][0]} teve a maior media sendo ela {matriz[posicao][3]}")