# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada dos dados
arquivo = "Lista 2.csv"
dados_originais = pd.read_csv(arquivo, header = 1, delimiter = ";")
dados = dados_originais.to_dict('list')

# (3) Processamento dos dados

media_d = np.mean(dados['Resistencia (kgf)'])
mediana_d = np.median(dados['Resistencia (kgf)'])
sigma_d = np.std(dados['Resistencia (kgf)'])

# Cálculos para o boxplot

Q1_d = np.percentile(dados['Resistencia (kgf)'], 25, method='averaged_inverted_cdf')
Q2_d = np.percentile(dados['Resistencia (kgf)'], 50, method='averaged_inverted_cdf')
Q3_d = np.percentile(dados['Resistencia (kgf)'], 75, method='averaged_inverted_cdf')

dq_d = Q3_d-Q1_d
menor_valor_d = min(dados['Resistencia (kgf)'])
maior_valor_d = max(dados['Resistencia (kgf)'])

LI = max(menor_valor_d, Q1_d - 1.5 * dq_d)
LS = min(maior_valor_d, Q3_d + 1.5 * dq_d)

# (4) Apresentação dos resultados

print("A média dos dados é: ", media_d)
print("A mediana dos dados é: ", mediana_d)
print("O desvio-padrão dos dados é: ", sigma_d)

print("Q1 = ", Q1_d)
print("Q2 = ", Q2_d)
print("Q3 = ", Q3_d)

print("LI = ", LI)
print("LS = ", LS)

plt.boxplot(dados['Resistencia (kgf)'])
plt.title("Resistência (kgf) com outlier")
plt.show()