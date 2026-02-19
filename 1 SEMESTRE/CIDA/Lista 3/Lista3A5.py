import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Entrada de dados
categorias = {
    "vendas": {
        "direito": np.array([9,9,9,9,9,9,9,9,9,9,9]),
        "politica": np.array([7.0,9.0,10.0,5.5,7.0,6.0,6.0,6.0,9.0,6.5,7.0]),
        "estatistica": np.array([8,7,8,9,2,7,7,7,8,9,8,7])
    },
    "tecnica": {
        "direito": np.array([9,9,9,9,9,9,9]),
        "politica": np.array([6.0,9.0,9.0,7.0,5.5,6.0,8.0]),
        "estatistica": np.array([8,9,8,10,7,7,9])
    },
    "pessoal": {
        "direito": np.array([9,9,9,9,9,9,9]),
        "politica": np.array([9.0,6.5,9.0,6.0,6.5,6.5,0.5,9.0]),
        "estatistica": np.array([9,9,8,8,9,10,8])
    }
}

# Loop
for categoria, areas in categorias.items():
    print(f"\nCategoria: {categoria}")
    for area, valores in areas.items():
        media = np.mean(valores)
        mediana = np.median(valores)
        moda = stats.mode(valores, keepdims=False).mode
        desvio_padrao = np.std(valores, ddof=0)

        print(f"  Área: {area}")
        print(f"    Média: {media:.2f}")
        print(f"    Mediana: {mediana}")
        print(f"    Moda: {moda}")
        print(f"    Desvio Padrão: {desvio_padrao:.2f}")

# Criação de Boxplot por disciplina
for disciplina in ["direito", "politica", "estatistica"]:
    plt.figure(figsize=(8, 5))
    plt.boxplot([categorias[categoria][disciplina] for categoria in categorias], labels=categorias.keys())
    plt.title(f"Boxplot da disciplina: {disciplina}")
    plt.xlabel("Categoria")
    plt.ylabel("Notas")
    plt.show()

# Boxplot geral
turma_toda = np.concatenate([categorias["vendas"]["direito"],
                             categorias["vendas"]["politica"],
                             categorias["vendas"]["estatistica"],
                             categorias["tecnica"]["direito"],
                             categorias["tecnica"]["politica"],
                             categorias["tecnica"]["estatistica"],
                             categorias["pessoal"]["direito"],
                             categorias["pessoal"]["politica"],
                             categorias["pessoal"]["estatistica"]])

plt.figure(figsize=(8, 6))
plt.boxplot([categorias["pessoal"]["direito"], categorias["tecnica"]["direito"], categorias["vendas"]["direito"], turma_toda],
            labels=["Pessoal", "Técnica", "Vendas", "Turma Toda"])
plt.title("Comparação do Desempenho por Seção da Empresa")
plt.ylabel("Notas")
plt.show()









#Comentários
#A disciplina Direito mostra uma distribuição estável, indicando pouca variação entre funcionários.

#Política tem maior dispersão, especialmente no grupo Pessoal, sugerindo avaliações inconsistentes entre funcionários.

#statística apresenta uma grande variação nos resultados, principalmente em Vendas, indicando diferenças mais marcantes entre os funcionários dessa área.

#