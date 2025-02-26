import numpy as np

def multiplicarEscalar(A, x):
    linhas = A.shape[0]
    colunas = A.shape[1]

    resultado = np.zeros((linhas, colunas))

    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = A[i][j] * x 

    return resultado

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

x = 3

print("Matriz original A:")
print(A)

resultado = multiplicarEscalar(A, x)

print("\nMatriz A multiplicada por", x, ":")
print(resultado)
