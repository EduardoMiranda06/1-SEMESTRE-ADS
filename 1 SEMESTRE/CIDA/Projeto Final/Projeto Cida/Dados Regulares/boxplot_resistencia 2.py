# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada dos dados
arquivo = "Lista.csv"
dados_originais = pd.read_csv(arquivo, header = 1, delimiter = ";")
dados = dados_originais.to_dict('list')

# (3) Processamento dos dados

media = np.mean(dados['Resistencia (kgf)'])
mediana = np.median(dados['Resistencia (kgf)'])
sigma = np.std(dados['Resistencia (kgf)'])

# Cálculos para o boxplot

Q1 = np.percentile(dados['Resistencia (kgf)'], 25, method='averaged_inverted_cdf')
Q2 = np.percentile(dados['Resistencia (kgf)'], 50, method='averaged_inverted_cdf')
Q3 = np.percentile(dados['Resistencia (kgf)'], 75, method='averaged_inverted_cdf')

dq = Q3-Q1
menor_valor = min(dados['Resistencia (kgf)'])
maior_valor = max(dados['Resistencia (kgf)'])

LI = max(menor_valor, Q1 - 1.5 * dq)
LS = min(maior_valor, Q3 + 1.5 * dq)

# (4) Apresentação dos resultados

print("A média dos dados é: ", media)
print("A mediana dos dados é: ", mediana)
print("O desvio-padrão dos dados é: ", sigma)

print("Q1 = ", Q1)
print("Q2 = ", Q2)
print("Q3 = ", Q3)

print("LI = ", LI)
print("LS = ", LS)

plt.boxplot(dados['Resistencia (kgf)'])
plt.title("Resistência")
plt.show()
