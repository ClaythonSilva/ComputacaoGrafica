import numpy as np

def transposta(A):
    linhas = A.shape[0]
    colunas = A.shape[1]

    transposta = np.zeros((colunas, linhas))

    for i in range(linhas):
        for j in range(colunas):
            transposta[j][i] = A[i][j] 

    return transposta

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print("Matriz original A:")
print(A)

A_transposta = transposta(A)

print("\nMatriz transposta de A:")
print(A_transposta)
