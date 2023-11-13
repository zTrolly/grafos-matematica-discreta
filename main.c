#include <stdio.h>
#include <stdlib.h>

// Função para ler a sequência de números do teclado e armazenar em um array
void lerSequencia(int **array, int *tamanho) {
    printf("Digite o tamanho da sequência: ");
    scanf("%d", tamanho);

    *array = (int *)malloc((*tamanho) * sizeof(int));

    printf("Digite a sequência de números:\n");
    for (int i = 0; i < *tamanho; i++) {
        scanf("%d", &(*array)[i]);
    }
}

// Função para converter a sequência em matriz de incidência
int **sequenciaParaMatrizIncidencia(int *sequencia, int tamanho, int *vertices, int *arestas) {
    // Verifica se o tamanho da sequência é consistente com a matriz de incidência
    if (tamanho % 2 != 0) {
        printf("Tamanho da sequência não é válido para matriz de incidência.\n");
        exit(1);
    }

    *vertices = tamanho / 2;
    *arestas = tamanho / 2;

    int **matriz = (int **)malloc((*vertices) * sizeof(int *));
    for (int i = 0; i < *vertices; i++) {
        matriz[i] = (int *)malloc((*arestas) * sizeof(int));
    }

    for (int i = 0; i < *vertices; i++) {
        for (int j = 0; j < *arestas; j++) {
            matriz[i][j] = sequencia[i * (*arestas) + j];
        }
    }

    return matriz;
}

// Função para converter a sequência em matriz de adjacência
int **sequenciaParaMatrizAdjacencia(int *sequencia, int tamanho, int *vertices) {
    // Verifica se o tamanho da sequência é consistente com a matriz de adjacência
    if (tamanho != (*vertices) * (*vertices)) {
        printf("Tamanho da sequência não é válido para matriz de adjacência.\n");
        exit(1);
    }

    int **matriz = (int **)malloc((*vertices) * sizeof(int *));
    for (int i = 0; i < *vertices; i++) {
        matriz[i] = (int *)malloc((*vertices) * sizeof(int));
    }

    for (int i = 0; i < *vertices; i++) {
        for (int j = 0; j < *vertices; j++) {
            matriz[i][j] = sequencia[i * (*vertices) + j];
        }
    }

    return matriz;
}

// Função para calcular o grau de um vértice na matriz de incidência
int grauVerticeMatrizIncidencia(int **matriz, int vertices, int arestas, int vertice) {
    int grau = 0;

    for (int i = 0; i < arestas; i++) {
        if (matriz[vertice][i] == 1) {
            grau++;
        }
    }

    return grau;
}

// Função para imprimir a representação em conjuntos do grafo na matriz de adjacência
void imprimirGrafoMatrizAdjacencia(int **matriz, int vertices) {
    printf("V = {");
    for (int i = 0; i < vertices; i++) {
        printf("%c", 'a' + i);
        if (i < vertices - 1) {
            printf(",");
        }
    }
    printf("}\n");

    printf("A = {");
    for (int i = 0; i < vertices; i++) {
        for (int j = i + 1; j < vertices; j++) {
            if (matriz[i][j] == 1) {
                printf("{%c,%c}", 'a' + i, 'a' + j);
                if (i < vertices - 2 || (i == vertices - 2 && j < vertices - 1)) {
                    printf(",");
                }
            }
        }
    }
    printf("}\n");
}

int main() {
    int *sequencia;
    int tamanho, vertices, arestas;

    lerSequencia(&sequencia, &tamanho);

    int **matrizIncidencia = sequenciaParaMatrizIncidencia(sequencia, tamanho, &vertices, &arestas);
    int **matrizAdjacencia = sequenciaParaMatrizAdjacencia(sequencia, tamanho, &vertices);

    // Exemplo de uso da função para calcular o grau de um vértice na matriz de incidência
    int verticeDesejado = 0;
    int grau = grauVerticeMatrizIncidencia(matrizIncidencia, vertices, arestas, verticeDesejado);
    printf("O grau do vértice %c na matriz de incidência é: %d\n", 'a' + verticeDesejado, grau);

    // Exemplo de uso da função para imprimir a representação em conjuntos do grafo na matriz de adjacência
    imprimirGrafoMatrizAdjacencia(matrizAdjacencia, vertices);

    // Liberar memória alocada
    free(sequencia);
    for (int i = 0; i < vertices; i++) {
        free(matrizIncidencia[i]);
        free(matrizAdjacencia[i]);
    }
    free(matrizIncidencia);
    free(matrizAdjacencia);

    return 0;
}
