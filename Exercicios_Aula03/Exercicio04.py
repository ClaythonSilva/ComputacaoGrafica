import numpy as np
import matplotlib.pyplot as plt
# Função para calcular a translação dos pontos
def rotação(pontos, angulo_rad):
  pontos_rotacionados = []
  for ponto in pontos:
    x0, y0=ponto
    xu = x0 * np.cos(angulo_rad) - y0 * np.sin(angulo_rad)
    yu = x0 * np.cos(angulo_rad) + y0 * np.sin(angulo_rad)
    pontos_rotacionados.append((xu, yu))
  return pontos_rotacionados

# Pontos originais
p1 = (2, 2)
p2 = (4, 4)

# Angulo de rotação
angulo = 45
angulo_rad = np.radians(angulo)


# Calcular a translação dos pontos
pontos_rotacionados = rotação([p1, p2], angulo_rad)

# Plotar os pontos originais e os pontos transladados
plt.plot([p1[0], p2[0], p1[0]], [p1[1], p2[1], p1[1]], 'bo-', label='Pontos originais')

plt.plot([ponto[0] for ponto in pontos_rotacionados], [ponto[1] for ponto in pontos_rotacionados],'ro-', label='Pontos rotacionados')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Rotação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()