import numpy as np

def verificarDiag(A):
    if A.shape[0] != A.shape[1]:
        return False

    for i in range(A.shape[0]):  
        for j in range(A.shape[1]):  
            if i != j and A[i, j] != 0:
                return False

    return True

# Matriz quadrada (3x3)
A = np.array([[5, 0, 0],
              [0, 3, 0],
              [0, 0, 8]])

# Verificar se a matriz A é diagonal
if verificarDiag(A):
    print("A primeira matriz é diagonal.")
else:
    print("A primeira matriz NÃO é diagonal.")

# Matriz que não é diagonal (3x3)
B = np.array([[5, 2, 0],
              [0, 3, 0],
              [0, 0, 8]])

# Verificar se a matriz B é diagonal
if verificarDiag(B):
    print("A segunda matriz é diagonal.")
else:
    print("A segunda matriz NÃO é diagonal.")

