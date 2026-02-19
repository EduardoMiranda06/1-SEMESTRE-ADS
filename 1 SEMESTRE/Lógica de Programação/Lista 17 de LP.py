#LISTA 17
#EXERCÍCIOS APENAS USANDO O WHILE
## Elaborar um programa para pesquisar dois valores em uma lista. Na impressão, indique qual dos dois valores foi achado primeiro.

#1

def encontrar_primeiro(lista, valor1, valor2):
    i = 0
    encontrado = None

    while i < len(lista):
        if lista[i] == valor1:
            encontrado = valor1
            break
        elif lista[i] == valor2:
            encontrado = valor2
            break
        i += 1

    return encontrado

lista = [3, 7, 2, 9, 4, 7, 8]
valor1 = 50
valor2 = 50

resultado = encontrar_primeiro(lista, valor1, valor2)

if resultado:
    print(f"O primeiro valor localizado foi: {resultado}")
else:
    print("Nenhum dos valores foi localizado")

#2

total = 0
contador = 0

while contador < 8:
    nota = float(input(f"Insira a {contador + 1}ª nota: "))
    total += nota
    contador += 1

media = total / 8
print(f"A média das notas é: {media:.2f}")

#3
lista_a = []
lista_b = []
lista_c = []

indice = 0

while indice < 5:
    item = input(f"Insira o {indice + 1}º elemento da primeira lista: ")
    lista_a.append(item)
    indice += 1

indice = 0

while indice < 5:
    item = input(f"Insira o {indice + 1}º elemento da segunda lista: ")
    lista_b.append(item)
    indice += 1

indice = 0

while indice < len(lista_a):
    lista_c.append(lista_a[indice])
    indice += 1

indice = 0

while indice < len(lista_b):
    lista_c.append(lista_b[indice])
    indice += 1

print("Lista da fusão :", lista_c)

#4

def combinar_listas(lista_x, lista_y):
    lista_final = []
    indice_x = 0

    while indice_x < len(lista_x):
        if lista_x[indice_x] not in lista_final:
            lista_final.append(lista_x[indice_x])
        indice_x += 1

    indice_y = 0
    while indice_y < len(lista_y):
        if lista_y[indice_y] not in lista_final:
            lista_final.append(lista_y[indice_y])
        indice_y += 1

    return lista_final

numeros_a = [1, 2, 3, 4, 5]
numeros_b = [4, 5, 6, 7, 8]
resultado = combinar_listas(numeros_a, numeros_b)
print(resultado)

#5
def gerenciar_atendimento():
    fila_prioritaria = []
    fila_comum = []

    while True:
        acao = input("Digite um comando (F: fila prioritária, G: fila comum, A: atender fila prioritária, B: atender fila comum, S: sair): ").strip().upper()

        if acao == "F":
            cliente = input("Nome do cliente para fila prioritária: ")
            fila_prioritaria.append(cliente)

        elif acao == "G":
            cliente = input("Nome do cliente para fila comum: ")
            fila_comum.append(cliente)

        elif acao == "A":
            if fila_prioritaria:
                print(f"Atendendo: {fila_prioritaria.pop(0)} da fila prioritária")
            else:
                print("Fila prioritária vazia.")

        elif acao == "B":
            if fila_comum:
                print(f"Atendendo: {fila_comum.pop(0)} da fila comum")
            else:
                print("Fila comum vazia.")

        elif acao == "S":
            print("Encerrando atendimento...")
            break

        else:
            print("Comando inválido. Use F, G, A, B ou S.")


gerenciar_atendimento()

#6
def localizar_elementos(lista, elemento1, elemento2):
    indice1 = -1
    indice2 = -1
    contador = 0

    while contador < len(lista):
        if lista[contador] == elemento1 and indice1 == -1:
            indice1 = contador

        if lista[contador] == elemento2 and indice2 == -1:
            indice2 = contador

        contador += 1

    return indice1, indice2



dados = [10, 20, 30, 40, 50, 60]
buscar1 = 30
buscar2 = 50
resultados = localizar_elementos(dados, buscar1, buscar2)

print(f"Posição de {buscar1}: {resultados[0]}")
print(f"Posição de {buscar2}: {resultados[1]}")

