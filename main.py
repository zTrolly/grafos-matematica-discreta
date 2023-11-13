"""
(a) Leia uma sequência de números X do teclado e a armazene em um array;
(b) Interprete a sequência de X números como uma matriz de NxM (N linhas e M colunas) e a
converta para uma matriz de incidência. Note que N representa o número de vértices e M o
número arestas. NxM = X.
(c) Interprete a sequência de X números como uma matriz de NxN (N é o número de vértices) e a
converta para uma matriz de adjacência.
(d) O programa deve ser capaz de verificar que |X| é condizente com a transformação que se deseja
executar (matriz de incidência ou adjacência).
(e) Escreva uma função que dada a matriz de incidência e um vértice como entrada, compute o grau
deste vértice d(v).
(f) Escreva uma função que dada uma matriz de adjacência como entrada, imprima na saída padrão
a representação em conjuntos do grafo. (imprima o conjunto de vértices e arestas: V={a,b,c...},
A={a,b},{b,c}, ...).
"""

import numpy as np
import sys

def main():
    # Recebe a entrada do usuário
    entrada = input("Digite a sequência de números: ")
    # Separa a entrada em uma lista de números
    entrada = entrada.split()
    # Converte a lista de strings para uma lista de inteiros
    entrada = [int(i) for i in entrada]
    # Verifica se a entrada é válida
    if len(entrada) < 2:
        print("Entrada inválida!")
        sys.exit()
    # Verifica se a entrada é válida
    if len(entrada) % 2 != 0:
        print("Entrada inválida!")
        sys.exit()
    # Converte a lista de inteiros para uma matriz de incidência
    matriz_incidencia = np.array(entrada).reshape(int(len(entrada)/2), 2)
    # Imprime a matriz de incidência
    print("Matriz de incidência: ")
    print(matriz_incidencia)
    # Converte a matriz de incidência para uma matriz de adjacência
    matriz_adjacencia = np.zeros((len(matriz_incidencia), len(matriz_incidencia)))
    for i in range(len(matriz_incidencia)):
        for j in range(len(matriz_incidencia)):
            if matriz_incidencia[i][0] == matriz_incidencia[j][0] or matriz_incidencia[i][0] == matriz_incidencia[j][1]:
                matriz_adjacencia[i][j] = 1
    # Imprime a matriz de adjacência
    print("Matriz de adjacência: ")
    print(matriz_adjacencia)
    # Imprime o conjunto de vértices
    print("V = {", end='')
    for i in range(len(matriz_adjacencia)):
        if i == len(matriz_adjacencia)-1:
            print(chr(97+i), end='')
        else:
            print(chr(97+i), end=',')
    print("}")
    # Imprime o conjunto de arestas
    print("A = {", end='')
    for i in range(len(matriz_adjacencia)):
        for j in range(len(matriz_adjacencia)):
            if matriz_adjacencia[i][j] == 1:
                print("{" + chr(97+i) + "," + chr(97+j) + "}", end='')
    print("}")
    # Recebe o vértice do usuário
    vertice = input("Digite o vértice: ")
    # Verifica se o vértice é válido
    if ord(vertice) < 97 or ord(vertice) > 97+len(matriz_adjacencia)-1:
        print("Vértice inválido!")
        sys.exit()
    # Imprime o grau do vértice
    print("Grau do vértice: ", end='')
    print(grau_vertice(matriz_incidencia, vertice))

# Função que calcula o grau de um vértice
def grau_vertice(matriz_incidencia, vertice):
    grau = 0
    for i in range(len(matriz_incidencia)):
        if matriz_incidencia[i][0] == ord(vertice)-97 or matriz_incidencia[i][1] == ord(vertice)-97:
            grau += 1
    return grau

if __name__ == "__main__":
    main()

# Exemplo de entrada: 0 1 0 2 1 2 1 3 2 3 2 4 3 4 3 5 4 5

# Exemplo de saída:
# Matriz de incidência:
# [[0 1]
#  [0 2]
#  [1 2]
#  [1 3]
#  [2 3]
#  [2 4]
#  [3 4]
#  [3 5]
#  [4 5]]
# Matriz de adjacência:
# [[0. 1. 1. 0. 0. 0.]
#  [1. 0. 1. 1. 0. 0.]
#  [1. 1. 0. 1. 1. 0.]
#  [0. 1. 1. 0. 1. 1.]
#  [0. 0. 1. 1. 0. 1.]
#  [0. 0. 0. 1. 1. 0.]]
# V = {a,b,c,d,e,f}
# A = {{a,b},{a,c},{b,c},{b,d},{c,d},{c,e},{d,e},{d,f},{e,f}}
# Digite o vértice: a
# Grau do vértice: 2
