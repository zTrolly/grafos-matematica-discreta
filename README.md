# Graph Analysis in Python
Este é um simples programa em Python para criar, analisar e visualizar grafos. O código utiliza representações de matriz de incidência e matriz de adjacência para representar grafos e oferece funcionalidades como cálculo de grau de vértices e visualização gráfica.

Requisitos
- Python 3.x
- Bibliotecas: networkx, matplotlib
- Você pode instalar as bibliotecas necessárias executando o seguinte comando:

```
pip install networkx matplotlib

```

# Como Usar
- Execute o programa graph_analysis.py.
- Insira o número de linhas (vértices) e colunas (arestas) do seu grafo.
- Insira a sequência de números para representar o grafo.
O programa calculará e imprimirá informações sobre os conjuntos de vértices e arestas, bem como uma representação visual do grafo.

# Funções Principais
- **sequencia_para_matriz_incidencia(numeros, N, M):**
    Converte uma sequência de números em uma matriz de incidência.
- **sequencia_para_matriz_adjacencia(numeros, N, M):**
    Converte uma sequência de números em uma matriz de adjacência.
- **calcular_grau(matriz_incidencia, vertice):**
    Calcula o grau de um vértice na matriz de incidência.
- **imprimir_conjuntos(matriz_adjacencia):**
    Imprime conjuntos de vértices e arestas a partir da matriz de adjacência.
- **mostrar_grafo(matriz_adjacencia):**
    Exibe uma representação visual do grafo utilizando a biblioteca networkx.

# Exemplo de Uso
#### Entrada:
```
Digite o número de linhas: 3
Digite o número de colunas: 3
Digite a sequência de números: 0 1 1 1 0 1 1 1 0
Digite o vértice: 1

```
#### Saída Esperada:
```
Vértices: {0, 1, 2}
Arestas: {(0, 1), (1, 2), (2, 1), (2, 0), (0, 2), (1, 0)}
Grau do vértice: 2

```
<div align="center">
  <img src="https://github.com/zTrolly/grafos-matematica-discreta/assets/61760048/1a8bf3a5-5dd5-4fd1-b20f-f89924865a2d)https://github.com/zTrolly/grafos-matematica-discreta/assets/61760048/1a8bf3a5-5dd5-4fd1-b20f-f89924865a2d" alt="~Grafo Gerado">
</div>



