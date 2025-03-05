import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a translação dos pontos
def translacao(pontos, Tx, Ty):
    pontos_translados = []
    for ponto in pontos:
        x_u = ponto[0] + Tx
        y_u = ponto[1] + Ty
        pontos_translados.append((x_u, y_u))
    return pontos_translados

# Pontos originais
p1 = (6, 8)
p2 = (4, 5)
p3 = (8, 5)

# Vetor de translação
Tx = 3
Ty = -4

# Calcular a translação dos pontos
pontos_originais = [p1, p2, p3, p1]  # Adiciona p1 novamente para fechar o triângulo
pontos_translados = translacao(pontos_originais, Tx, Ty)

# Plotar os pontos originais e os pontos transladados
plt.plot([p[0] for p in pontos_originais], [p[1] for p in pontos_originais], 'bo-', label='Pontos originais')
plt.plot([p[0] for p in pontos_translados], [p[1] for p in pontos_translados], 'ro-', label='Pontos transladados')

# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Translação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()
