# (1) Carregamento de bibliotecas

import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada de dados

arquivo = "Lista.csv"
dados_originais = pd.read_csv(arquivo, header = 1, delimiter = ";")
dados = dados_originais.to_dict('list')

# (4) Apresentação dos dados

# Resistência x diâmetro
plt.scatter(dados["Diametro (mm)"],dados["Resistencia (kgf)"], c='r', marker='x')
plt.title("Resistência x diâmetro")
plt.xlabel("Diametro (mm)")
plt.ylabel("Resistência (kgf)")
plt.show()

# Resistência x densidade
plt.scatter(dados["Densidade"],dados["Resistencia (kgf)"], c='r', marker='x')
plt.title("Resistência x Densidade")
plt.xlabel("Densidade")
plt.ylabel("Resistência (kgf)")
plt.show()

# Resistência x Área (mm^2)
plt.scatter(dados["Área (mm^2)"],dados["Resistencia (kgf)"], c='r', marker='x')
plt.title("Resistência x Área (mm^2)")
plt.xlabel("Área (mm^2)")
plt.ylabel("Resistência (kgf)")
plt.show()

