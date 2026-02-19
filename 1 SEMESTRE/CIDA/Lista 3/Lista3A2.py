import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dicionário de dados
dados = {
    "futebol": np.array([1,7,7,6,1,2,6,1,7,2,1,3,2,7,5,6,1,7,4,1,5,7,6,3,2,2,15,4]),
    "basquete": np.array([2,2,4,4,7,3,3,2,4,5,2,4,3,5,3,2,4,3,6,5,5,6,4,6,5,0,10,5])
}

# Cálculos estatísticos
for nome, acidentes in dados.items():
    media = np.mean(acidentes)
    mediana = np.median(acidentes)
    moda = stats.mode(acidentes, keepdims=False).mode
    desvio_padrao = np.std(acidentes, ddof=0)

# Criando um boxplot para visualização
    plt.boxplot(dados.values(), labels=dados.keys())
    plt.title("Distribuição de Acidentes por Esporte")
    plt.xlabel("Esporte")
    plt.ylabel("Número de Acidentes")
    plt.show()

#Visualização
    print(f"\nEsporte: {nome}")
    print(f"  Média: {media}")
    print(f"  Mediana: {mediana}")
    print(f"  Moda: {moda}")
    print(f"  Desvio Padrão: {desvio_padrao}")



