#                                                                            AULA DO DIA 22/04/2025
#lista = [19,30,40,50]
from selectors import SelectSelector

from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

#print(lista[0])
#19
#print(lista [1])
#30
#print(lista[2])
#40
#print(lista[3])
#50

# E2----------
#notas=[6,8,10,7,9]
#soma=0
#x=0
#while x<5:
  #        soma += notas[x]
 #         x=x+1
#          print("Média : %5.2f"%(soma/x))

# E3----------
# notas=[0,0,0,0,0]
# soma=0
 #x=0
 #while x <5:
 #notas[x]=float(input("Nota %d:"%x))
 #soma += notas [x]
 #x=x+1
 #x=0
 #while x<5:
  #  print("Nota %d: %6.2f"%(x,notas[x]))
   #       x=x+1
    #print("Média: %5.2f"%(soma/x))

#E4----------
#numeros=[0,0,0,0,0]
#x=0
#while x <5:
    #numeros[x]=int(input("Número %d:"%(x+1)))
   # x+=1
#while True:
#    escolhido=int(input("Qual das posições deseja visualizar?(0->sair)"))
 #   if escolhido == 0:
  #      break
#    print("Número escolhido: %d"%(números[escolhido-1]))

#E5----------
#L=[10,20,30,40,50]
#V=L[:]
#V[0]=60
#L[10,20,30,40,50]
#V[60,20,30,40,50]

#E6----------
#L=[1,2,3,4,5]
#L[0:5]
#[1,2,3,4,5]
#L[:5]
#[1,2,3,4,5]
#L[:-1]
#[1,2,3,4]

#E7----------
#L=[1,2,3,4,5]
#[1:3]
#[2,3]
#L[1:4]
#[2,3,4]
#L[3:]
#[4,5]

#E8----------
#L=[12,9,5]
#len(L)
#3
#v=[]
#len(V)
#0

#E9----------
#L= [1,2,3]
#x=0
#while x < 3:
#    print(L[x])
#    x+=1
#E10----------
#L= [1,2,3]
#x=0
#while x < len(L):
#    print(L[x])
#    x+=1

# E11----------
#L=[]
#L.append("a")
#L
#['a']

#E12----------
#L=[]
#L.append("a,b")
#L
#['a']

#E13----------
#L=[]
#while True:
#    n=int(input("Digite um número(0 sai:"))
#    if n == 0
#        break
#        L.append(n)
#x=0
#while x < len(L):
#    print(L[x])
#    x=x+1

#E14----------
L=[]
L=L+[1]
L
[1]

#E15----------
L+=[3,4,5]
L
[1,2,3,4,5]

#E16----------
L=["a"]
L.append("b")
L
['a','b']
L.extend(["c"])
L['a','b','c']

#S17----------
L.append(["d","e"])
L
['a','b','c',['d','e']]
L.extend(["f","g","h"])
L
['a','b','c',['d','e']"f","g","h"]

#S18----------
L=["a"]
L.append(["b"])
L.append(["c","d"])
len(L)
3
L[1]
['B']

#S19----------
L=["a","b","c"]
del L[1]
L
['a','c']
del L[0]
L
['c']

#S20-----------
L=list(range(101))
L[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29,
30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
del L [1:99]
L
[0,99,100]

#S21-----------
ultimo = 10
fila = list(range(1,ultimo+1))
while True
    print("\nExistem %d clientes na fila"% len(fila))
    print(("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento, S para sair.")
    if operação == "A":
     if(len(fila))>0:
    atendido = fila.pop(0)
    print("Cliente %d atendido"% atendido)
else:
    print("Fila vazia!Ninguém para atender.")
elif operação == "F":
    ultimo +=1 # Incrementa o ticket do novo cliente
    fila.append(ultimo)
elifoperação =="S"
    break
else:
    print("Operação Inválida! Digite apenas F,A ou S!")

#s22----------
prato = 5
pilha = list(range(1,prato+1))
while True
    print("\nExistem %d pratos na pilha" %len(pilha))
    print("Pilha atual:", pilha)
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar, S para Sair.")
    operação= input(("Operação (E,D ou S):"))
if operação == "D":
    if(len(pilha))>0:
        lavado = pilha.pop(-1)
        print("Prato %d lavado" % lavado)
else :
    print("Pilha vazia! Nada para lavar.")
elifoperação == "S":
break
else
print("Operação inválida! Digite apenas E,D ou S!")

#S23----------
L=[15,7,27,39]
p=int(input("Digite o valor a procurar"))
achou=False
x=0
    while x<len(L):
    if L[x]==p:
        achou=True
        break
        x+=1
    if achou:
        print("%d achado na posição %d"%(p,x))
    else:
        print("%d não encontrado"%p)