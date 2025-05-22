import random
matriz = []
posicoes = [0,0]
maior = 0
for i in range(4):
    linha = []
    for j in range(4):
        var = random.randint(1, 20)
        linha.append(var)
        if maior < var:
            maior = var
            posicoes[0] = j
            posicoes[1] = i
    matriz.append(linha)

for linha in matriz:
    print(linha)

print(f"o maior numero foi na posicao {posicoes} e foi o numero {max(max(matriz))}")