import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada dos dados
arquivo = "Lista 2.csv"
dados_originais = pd.read_csv(arquivo, header = 1, delimiter = ";")
dados = dados_originais.to_dict('list')

tamanho = len(dados['Resistencia (kgf)'])
contador = range(tamanho)

area = []

tensao = []
for i in contador:
    diametro = dados['Diametro (mm)'][i]
    raio = diametro/2.0
    area = np.pi*raio*raio
    num = dados['Resistencia (kgf)'][i]
    den = area
    resultado = num/den
    tensao.append(resultado)

plt.boxplot(tensao)
plt.title("Tensão")
plt.show()