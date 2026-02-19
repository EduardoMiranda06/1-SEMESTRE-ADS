import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dicionário de notas
notas = {
    "alunas": np.array([154,109,137,115,152,140,154,178,101,103,126,126,137,165,129,200,148]),
    "alunos": np.array([108,140,114,91,180,115,126,92,169,146,109,132,75,88,113,151,70,115,187,104])
}

# Cálculos estatísticos
for grupo, valores in notas.items():
    media = np.mean(valores)
    mediana = np.median(valores)
    moda = stats.mode(valores, keepdims=False).mode
    desvio_padrao = np.std(valores, ddof=0)
    # Criando um boxplot para visualização
    plt.boxplot(notas.values(), labels=notas.keys())
    plt.title("Distribuição das Notas por Grupo")
    plt.xlabel("Grupo")
    plt.ylabel("Nota")
    plt.show()

#Visualização
print(f"\nGrupo: {grupo}")
print(f"  Média: {media}")
print(f"  Mediana: {mediana}")
print(f"  Moda: {moda}")
print(f"  Desvio Padrão: {desvio_padrao}")
print("A média é maior q a mediana devido a presença de outlier alto")


