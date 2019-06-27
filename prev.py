import numpy as np


def movingaverage(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas


print('==== PREVISÃO DE DEMANDA COM MACHINE LEARNING ====')

prod = str(input('Digite os valores da da demanda em ordem e separado por ponto e virgula: ')).strip()

x = list(map(int, prod.split(',')))
xm = np.average(x)
xstd = np.std(x)
matriz = np.array(x)

# print(matriz)
# print(type(matriz))

print("A média simples é: \033[1;32m{:.0f}\033[m".format(xm))
print('O desvio padrão da média simples é: \033[1;33m{:.0f}\033[m'.format(xstd))
print('De acordo com o método de média móvel a previsão para o próximo período é de: \033[1;33m{:.0f}\033[m'.format(xm))
print('---' * 20)

# Média móvel de 3 períodos
mmp1 = movingaverage(x, 4)
print('A média móvel de 3 períodos é:')
print(mmp1)
print(type(mmp1))
# print('---' * 20)
# print(stats.describe(p1))
# print('-/-' * 20, '\n')
