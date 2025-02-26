import numpy as np

A = np.array([[1, 3, 2], [4, 7, 6]])  
B = np.array([[2, 8], [3, 1], [5, 9]])  

resultado = np.zeros((A.shape[0], B.shape[1]))


print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

for i in range(A.shape[0]):  
    for j in range(B.shape[1]):  
        for k in range(A.shape[1]):  
            resultado[i, j] += A[i, k] * B[k, j]

print("\nResultado da multiplicação de A e B:")
print(resultado)
