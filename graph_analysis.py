import networkx as nx
import matplotlib.pyplot as plt

"""
 função sequencia_para_matriz_incidencia(numeros, N, M):
    se o comprimento de 'numeros' não for igual a N * M:
        lançar ValueError("A quantidade de números não corresponde às dimensões NxM")
    
    matriz_incidencia = []
    
    para cada índice i de 0 até o comprimento de 'numeros' com incremento de M:
        adicionar 'numeros[i:i + M]' à 'matriz_incidencia'
    
    retornar 'matriz_incidencia'

"""

def sequencia_para_matriz_incidencia(numeros, N, M):
   if len(numeros) != N * M:
       raise ValueError("A quantidade de números não corresponde às dimensões NxM")
   return [numeros[i:i + M] for i in range(0, len(numeros), M)]


"""
função sequencia_para_matriz_adjacencia(numeros, N, M):
    se o comprimento de 'numeros' não for igual a N * M:
        lançar ValueError("A quantidade de números não corresponde às dimensões NxM")
    
    matriz_adjacencia = []
    
    para cada linha em [numeros[i:i + M] para i de 0 até o comprimento de 'numeros' com incremento de M]:
        adicionar [converter cada 'num' em linha para inteiro] à 'matriz_adjacencia'
    
    retornar 'matriz_adjacencia'

"""
def sequencia_para_matriz_adjacencia(numeros, N, M):
   if len(numeros) != N * M:
       raise ValueError("A quantidade de números não corresponde às dimensões NxM")
   
   matriz_adjacencia = [[int(num) for num in linha] for linha in [numeros[i:i + M] for i in range(0, len(numeros), M)]]
   
   return matriz_adjacencia

"""
função calcular_grau(matriz_incidencia, vertice):
    grau = 0
    
    para cada linha em 'matriz_incidencia':
        se o valor na coluna 'vertice' da 'linha' for igual a '1':
            incrementar 'grau' em 1
    
    retornar 'grau'

"""

def calcular_grau(matriz_incidencia, vertice):
   grau = 0
   for linha in matriz_incidencia:
       if linha[vertice] == '1':
           grau += 1
   return grau


"""
função imprimir_conjuntos(matriz_adjacencia):
    vertices = conjunto de números de 0 até o comprimento da 'matriz_adjacencia'
    arestas = conjunto vazio

    para cada índice i e valor linha em enumerar 'matriz_adjacencia':
        para cada índice j e valor em 'linha':
            se o valor for igual a 1:
                adicionar a aresta (i, j) ao conjunto 'arestas'

    imprimir "Vértices:", vertices
    imprimir "Arestas:", arestas

"""

def imprimir_conjuntos(matriz_adjacencia):
   vertices = set(range(len(matriz_adjacencia)))
   arestas = set()

   for i, linha in enumerate(matriz_adjacencia):
       for j, valor in enumerate(linha):
           if valor == 1:
               arestas.add((i, j))

   print(f"Vértices: {vertices}")
   print(f"Arestas: {arestas}")
   

"""
função mostrar_grafo(matriz_adjacencia):
    G = novo grafo
    
    para cada índice i e valor linha em enumerar 'matriz_adjacencia':
        para cada índice j e valor em 'linha':
            se o valor for igual a 1:
                adicionar uma aresta entre os vértices i e j ao grafo G

    pos = calcular layout usando spring_layout(G)
    desenhar grafo G com rótulos, tamanho de nó, cor de nó, tamanho de fonte e layout definidos
    exibir o gráfico resultante

"""

def mostrar_grafo(matriz_adjacencia):
    G = nx.Graph()

    for i, linha in enumerate(matriz_adjacencia):
        for j, valor in enumerate(linha):
            if valor == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
    plt.show()


def main():
   N = int(input("Digite o número de linhas: "))
   M = int(input("Digite o número de colunas: "))
   numeros = input("Digite a sequência de números: ").split()
   
   matriz_incidencia = sequencia_para_matriz_incidencia(numeros, N, M)
   matriz_adjacencia = sequencia_para_matriz_adjacencia(numeros, N, M)
   imprimir_conjuntos(matriz_adjacencia)
   
   vertice = int(input("Digite o vértice: "))
   print(f"Grau do vértice: {calcular_grau(matriz_incidencia, vertice)}")
   mostrar_grafo(matriz_adjacencia)




if __name__ == "__main__":
   main()
