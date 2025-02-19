import numpy as np
import matplotlib.pyplot as plt

def tamanho_vetor(vetor):
    return np.linalg.norm(vetor)

def normalizar_vetor(vetor):
    tamanho = tamanho_vetor(vetor)
    return vetor / tamanho if tamanho != 0 else vetor

def somar_vetores(vetor1, vetor2):
    return vetor1 + vetor2

def subtrair_vetores(vetor1, vetor2):
    return vetor1 - vetor2

def multiplicar_por_escalar(vetor, escalar):
    return vetor * escalar

def dividir_por_escalar(vetor, escalar):
    if escalar != 0:
        return vetor / escalar
    else:
        print("Erro de divisão por zero")
        return vetor

def produto_escalar(vetor1, vetor2):
    return np.dot(vetor1, vetor2)

def plotar_vetores(vetor1, vetor2=None):
    plt.quiver(0, 0, vetor1[0], vetor1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vetor 1')
    if vetor2 is not None:
        plt.quiver(0, 0, vetor2[0], vetor2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vetor 2')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    x = float(input("Digite o valor de x do vetor: "))
    y = float(input("Digite o valor de y do vetor: "))
    z = float(input("Digite o valor de z do vetor: "))
    vetor1 = np.array([x, y, z])

    while True:
        print("\nEscolha uma opção:")
        print("a) Calcular o tamanho do vetor")
        print("b) Normalizar o vetor")
        print("c) Adicionar outro vetor")
        print("d) Subtrair outro vetor")
        print("e) Multiplicar o vetor por um escalar")
        print("f) Dividir o vetor por um escalar")
        print("g) Calcular o produto escalar entre os vetores")
        print("h) Plotar os vetores")
        print("i) Sair")

        opcao = input("Escolha uma opção(letra): ")

        if opcao == 'a':
            print(f"O tamanho do vetor é: {tamanho_vetor(vetor1)}")

        elif opcao == 'b':
            vetor_normalizado = normalizar_vetor(vetor1)
            print(f"Vetor normalizado: {vetor_normalizado}")

        elif opcao == 'c':
            x2 = float(input("Digite o valor de x do segundo vetor: "))
            y2 = float(input("Digite o valor de y do segundo vetor: "))
            z2 = float(input("Digite o valor de z do segundo vetor: "))
            vetor2 = np.array([x2, y2, z2])
            vetor_resultante = somar_vetores(vetor1, vetor2)
            print(f"Resultado da soma: {vetor_resultante}")

        elif opcao == 'd':
            x2 = float(input("Digite o valor de x do segundo vetor: "))
            y2 = float(input("Digite o valor de y do segundo vetor: "))
            z2 = float(input("Digite o valor de z do segundo vetor: "))
            vetor2 = np.array([x2, y2, z2])
            vetor_resultante = subtrair_vetores(vetor1, vetor2)
            print(f"Resultado da subtração: {vetor_resultante}")

        elif opcao == 'e':
            escalar = float(input("Digite o valor do escalar: "))
            vetor_resultante = multiplicar_por_escalar(vetor1, escalar)
            print(f"Resultado da multiplicação: {vetor_resultante}")

        elif opcao == 'f':
            escalar = float(input("Digite o valor do escalar: "))
            vetor_resultante = dividir_por_escalar(vetor1, escalar)
            print(f"Resultado da divisão: {vetor_resultante}")

        elif opcao == 'g':
            x2 = float(input("Digite o valor de x do segundo vetor: "))
            y2 = float(input("Digite o valor de y do segundo vetor: "))
            z2 = float(input("Digite o valor de z do segundo vetor: "))
            vetor2 = np.array([x2, y2, z2])
            resultado_produto = produto_escalar(vetor1, vetor2)
            print(f"Resultado do produto escalar: {resultado_produto}")

        elif opcao == 'h':
            plotar_vetores(vetor1)

        elif opcao == 'i':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()