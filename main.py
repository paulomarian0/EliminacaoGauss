import numpy as np
import sys
import random

# N = 3
n = 3

# Criando um array de n x n+1 e inicializando com zero para guardar a matriz
matriz = np.zeros((n, n + 1))

# Criando um array de tamanho n e inicializando com zero para guardar o vetor da solução
x = np.zeros(n)

# Leitura de coeficientes de matriz


#

print("Digite 1 para digitar os valores")
print("Digite 2 gerar valores aleatorios")
print("Digite 3 para usar valores criados pelo próprio programa")
print("Digite 4 para sair do programa")

entrada = input()

for i in range(n):
    for j in range(n + 1):
        if (entrada == '1'):
            matriz[i][j] = float(input('X[' + str(i) + '][' + str(j) + ']='))

        if (entrada == '2'):
            matriz[i][j] = random.randint(-10, 20)

        if (entrada == '3'):
            matriz[0][0] = 3
            matriz[0][1] = 0.1
            matriz[0][2] = -0.2
            matriz[0][3] = 7.85

            matriz[1][0] = 0.1
            matriz[1][1] = 7
            matriz[1][2] = -0.3
            matriz[1][3] = -19.3

            matriz[2][0] = 0.3
            matriz[2][1] = -0.2
            matriz[2][2] = -10
            matriz[2][3] = -71.4

        if (entrada == '4'):
            print("Finalizando o programa")
            sys.exit()
    ###

# Aplicando eliminação de Gauss

###### EXIBIR MATRIZ
for i in range(n):
    for j in range(n + 1):
        print('|', matriz[i][j], '|', '\t\t', end='')
    print("\n")

print("\n")

for i in range(n):
    if matriz[i][i] == 0.0:
        sys.exit('Divisão por zero detectada, impossível de continuar')

    for j in range(i + 1, n):
        ratio = matriz[j][i] / matriz[i][i]

        for k in range(n + 1):
            matriz[j][k] = matriz[j][k] - ratio * matriz[i][k]

# Retrossubstituição
x[n - 1] = matriz[n - 1][n] / matriz[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = matriz[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - matriz[i][j] * x[j]

    x[i] = x[i] / matriz[i][i]

for i in range(n):
    for j in range(n + 1):
        print('|', round(matriz[i][j], 3), '|', '\t\t', end='')
    print("\n")

# Mostrando a solução
print('\nResultado: ')
for i in range(n):
    print('X%d = %0.2f' % (i + 1, x[i]), end='\t\n')
