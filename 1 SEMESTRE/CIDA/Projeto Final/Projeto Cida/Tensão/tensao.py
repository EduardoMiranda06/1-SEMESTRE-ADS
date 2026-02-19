#Boxplot da Tensão

#(1) Carregamento de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.ma.core import left_shift

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

#Boxplot Tensão (Temperados)

# (2) Entrada dos dados
arquivo = "Lista 3.csv"
dados_originais = pd.read_csv(arquivo, header = 1, delimiter = ";")
dados1 = dados_originais.to_dict('list')

tamanho1 = len(dados1['Resistencia (kgf)'])
contador1 = range(tamanho1)

area1 = []

tensao1 = []
for i in contador1:
    diametro1 = dados1['Diametro (mm)'][i]
    raio1 = diametro1/2.0
    area1 = np.pi*raio1*raio1
    num1 = dados1['Resistencia (kgf)'][i]
    den1 = area1
    resultado1 = num1/den1
    tensao1.append(resultado1)

plt.boxplot([tensao, tensao1])
plt.title("Tensão das amostras")
plt.xlabel("(1) Normais (2) Temperados")
plt.show()

#diferença entre eles

media_normais = np.mean(tensao)
media_temperados = np.mean(tensao1)
diferença = (media_temperados/media_normais) * 100.0
print(diferença)

