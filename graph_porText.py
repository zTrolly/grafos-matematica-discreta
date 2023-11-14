import networkx as nx
import matplotlib.pyplot as plt
import sys

def sequencia_para_matriz_incidencia(numeros, N, M):
    if len(numeros) != N * M:
        raise ValueError("A quantidade de números não corresponde às dimensões NxM")
    return [numeros[i:i + M] for i in range(0, len(numeros), M)]

def sequencia_para_matriz_adjacencia(numeros, N, M):
    if len(numeros) != N * M:
        raise ValueError("A quantidade de números não corresponde às dimensões NxM")
   
    matriz_adjacencia = [[int(num) for num in linha] for linha in sequencia_para_matriz_incidencia(numeros, N, M)]
   
    return matriz_adjacencia

def calcular_grau(matriz_incidencia, vertice):
    grau = 0
    for linha in matriz_incidencia:
        if linha[vertice] == 1:
            grau += 1
    return grau

def imprimir_conjuntos(matriz_adjacencia):
    vertices = set(range(len(matriz_adjacencia)))
    arestas = set()

    for i, linha in enumerate(matriz_adjacencia):
        for j, valor in enumerate(linha):
            if valor == 1:
                arestas.add((i, j))

    print(f"Vértices: {vertices}")
    print(f"Arestas: {arestas}")

def mostrar_grafo(matriz_adjacencia):
    G = nx.Graph()

    for i, linha in enumerate(matriz_adjacencia):
        for j, valor in enumerate(linha):
            if valor == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    plt.show()


def main(file_path):
    with open(file_path, 'r') as file:
        numeros = [int(num) for line in file for num in line.split()]

    N = int(len(numeros) ** 0.5)
    M = N

    matriz_incidencia = sequencia_para_matriz_incidencia(numeros, N, M)
    matriz_adjacencia = sequencia_para_matriz_adjacencia(numeros, N, M)
    imprimir_conjuntos(matriz_adjacencia)

    vertice = int(input("Digite o vértice: "))
    print(f"Grau do vértice: {calcular_grau(matriz_incidencia, vertice)}")
    mostrar_grafo(matriz_adjacencia)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_script.py <caminho_do_arquivo>")
    else:
        file_path = sys.argv[1]
        main(file_path)
