import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Dados originais
x = np.arange(0, 10)
y = np.exp(-x / 3.0)

# Interpolação
f = interp1d(x, y)

# Novos dados para a interpolação
x_new = np.arange(0, 9, 0.1)
y_new = f(x_new)

# Plotando os gráficos
plt.plot(x, y, "o", label="Dados Originais")
plt.plot(x_new, y_new, "-", label="Interpolação Linear")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Interpolação Linear")
plt.legend()
plt.show()
