import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Simulação de dados
data = {
    "Tempo (dias)": np.arange(1, 101),
    "Conteúdo de Água (cm³/cm³)": np.random.rand(100) * 0.4 + 0.1,
}

# Criação do DataFrame
df = pd.DataFrame(data)

# Cálculo da média e desvio padrão
media_agua = np.mean(df["Conteúdo de Água (cm³/cm³)"])
desvio_agua = np.std(df["Conteúdo de Água (cm³/cm³)"])

# Plotando o gráfico com Matplotlib e Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Tempo (dias)", y="Conteúdo de Água (cm³/cm³)", marker="o")
plt.axhline(media_agua, color="r", linestyle="--", label=f"Média = {media_agua:.2f}")
plt.fill_between(
    df["Tempo (dias)"],
    media_agua - desvio_agua,
    media_agua + desvio_agua,
    color="r",
    alpha=0.2,
    label=f"Desvio Padrão = {desvio_agua:.2f}",
)
plt.title("Distribuição do Conteúdo de Água no Solo")
plt.xlabel("Tempo (dias)")
plt.ylabel("Conteúdo de Água (cm³/cm³)")
plt.legend()
plt.show()
