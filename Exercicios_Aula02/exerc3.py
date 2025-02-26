import numpy as np

def verificarIdent(A):
    if A.shape[0] != A.shape[1]:
        return False

    for i in range(A.shape[0]):  
        for j in range(A.shape[1]): 
            if (i == j and A[i, j] != 1) or (i != j and A[i, j] != 0):
                return False  
    return True

A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

if verificarIdent(A):
    print("A primeira matriz é identidade.")
else:
    print("A primeira matriz NÃO é identidade.")

B = np.array([[1, 0, 0],
              [0, 1, 1],
              [0, 0, 1]])

if verificarIdent(B):
    print("A segunda matriz é identidade.")
else:
    print("A segunda matriz NÃO é identidade.")	
