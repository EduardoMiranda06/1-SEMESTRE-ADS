import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados
valores = np.array([53.0,70.2,84.3,69.5,77.8,87.5,
                    53.5,64.3,82.7,78.5,55.7,69.1,
                    72.3,59.5,55.3,73.0,52.4,50.7])

# Criando o boxplot
plt.boxplot(valores)
plt.title("Boxplot da Dureza das Peças de Alumínio")
plt.xlabel("Dureza")
plt.show()

# Identificando outliers
q1, q3 = np.percentile(valores, [25, 75])
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Filtrando os outliers
outliers = valores[(valores < limite_inferior) | (valores > limite_superior)]

# Exibindo resultados
print(f"Valores originais: {valores}")
print(f"Outliers identificados: {outliers}")
53.4,82.5,67.3,54.1,70.5,71.4,
                    95.4,51.1,74.4,55.7,63.5,85.8,

