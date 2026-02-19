# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada dos dados
arquivo = "Lista 2.csv"
dados_originais = pd.read_csv(arquivo, header = 1, delimiter = ";")
dados = dados_originais.to_dict('list')

# (3) Processamento dos dados

media_d = np.mean(dados['Densidade (g/mm^2)'])
mediana_d = np.median(dados['Densidade (g/mm^2)'])
sigma_d = np.std(dados['Densidade (g/mm^2)'])

# Cálculos para o boxplot

Q1_d = np.percentile(dados['Densidade (g/mm^2)'], 25, method='averaged_inverted_cdf')
Q2_d = np.percentile(dados['Densidade (g/mm^2)'], 50, method='averaged_inverted_cdf')
Q3_d = np.percentile(dados['Densidade (g/mm^2)'], 75, method='averaged_inverted_cdf')

dq_d = Q3_d-Q1_d
menor_valor_d = min(dados['Densidade (g/mm^2)'])
maior_valor_d = max(dados['Densidade (g/mm^2)'])

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

plt.boxplot(dados['Densidade (g/mm^2)'])
plt.title("Densidade")
plt.show()

