L=[8,9,15]
for e in L:
    print (e)

L=[8,9,15]
x=0
while x<len(L):
    e=L[x]
    print(e)
    x+=1

L=[7,9,10,12]
p=int(input("Digite um número a pesquisar"))
for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
else:
    print("Elemento não encontrado.")

for v in range(10):
    print(v)

for v in range(3,10):
    print(v)

for t in range(3,33,3):
    print(t,end="")
    print()

L=list(range(100,1100,50))
print(L)

print("E COM A FUNÇÃO ENUMERATE?")
print("EXEMPLO SEM ENUMERATE")
L=[5,9,13]
x=0
for e in L:
    print("[%d]%d"%(x,e))
    x+=1

print("EXEMPLO COM ENUMERATE")
#L=[5,9,13]
#for x, e in enumerate(L):
#ERRO    print("[%d]%d"% x,e)

#VERIFICAÇÃO DO MAIOR VALOR

#L=[1,7,2,4]
#máximo=[0]
#for e in L:
#    if e> máximo:
#        máximo= e
#        print(máximo)

# CÓPIA DE ELEMENTOS PARA OUTRAS LISTAS
print("CÓPIA DE ELEMENTOS PARA OUTRAS LISTAS")

V=[9,8,7,12,0,13,21]
P=[]
I=[]
for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print("Pares:",P)
print("Impares:",I)

#VAGAS DE ESTACIONAMENTO
print("EXERCICIO VAGAS DE UM ESTACIONAMENTO")
lugares_vagos=[10,2,1,3,0]
while True:
    sala= int(input("Estacionamento (0 sai):"))
    if sala == 0 :
        print("Fim")
        break
    if sala>len(lugares_vagos) or sala<1:
        print("Estacionamento inválido")
    elif lugares_vagos[sala-1]==0:
        print("Desculpe, estacionamento lotado!")
    else:
        lugares=int(input("Quantos lugares você deseja(%d vagas):"% lugares_vagos[sala-1]))
    if lugares > lugares_vagos[sala-1]:
        print("Esse número de lugares não está disponível.")
    elif lugares < 0:
        print("Número inválido")
    else:
        lugares_vagos[sala-1]-=lugares
        print("%d lugares ocupados"% lugares)
print("Utilização dos estacionamentos")
for x,I in enumerate(lugares_vagos):
    print("Sala %d - %d lugar(es) vazio(s)"%(x+1,I))

### LENDO A IMPRIMINDO A LISTA DE COMPRAS
print("LENDO A IMPRIMINDO A LISTA DE COMPRAS")

compras=[]

while True:
    produto=int(input("Produto:"))
    if produto == "fim":
        break
    compras.append(produto)
for h in compras:
    print(h)

L=["maçãs","peras","kiwi"]
for s in L :
    for letra in s:
        print(letra)

#pt2
produto1=["maçã",10,0.30]
produto2=["pera",5,0.75]
produto3=["kiwi",4,0.98]
compras = [produto1,produto2,produto3]
for e in compras:
    print("Produto: %s"% e[0])
    print("Quantidade: %s" % e[1])
    print("Preço: %s" % e[2])














