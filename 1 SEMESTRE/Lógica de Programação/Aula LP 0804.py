from operator import truediv

from unicodedata import numeric

x=1
while x<=5:
    print(x)
    x=x+1

fim=int(input("Digite o último número a imprimir"))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
#
pontos = 0
questão = 1
while questão <=3:
    resposta = input("Resposta da questão %d:"% questão )
    if questão == 1 and resposta == "b":
        pontos = pontos + 1
    if questão == 2 and resposta =="a":
        pontos = pontos +1
    if questão == 3 and resposta == "d":
        pontos = pontos + 1
        questão +=1
        print("O aluno ")

#
n= 1
soma = 0
while n<=10:
    x=int(input("Digite o %d numero:"%n))
    soma = soma + x
    n = n + 1
print("Soma:%d"%soma)
#
n= 1
soma = 0
while n<=5 :
    n=int(input("%d Digite o numero"% x))
    soma = soma + n
    x = x + 1
    print("Média : %5.2f"%(soma/5))
#
 s= 0
 while true:
     v=int(input("DIGITE UM NUMERO A SOMAR OU 0 PARA SAIR"))
     if v == 0
         break
         s=s+v(print(s))
#
valor = int(input("Digite o valor a pagar"))
cédulas = 0
atual = 50
apagar=valor
while true:
    if atual <= apagar:
        apagar==atual
        cédulas+=1
else:print("%d cédula(s) de R$%d"% (cédulas,atual))
if apagar == 0
    break
if atual==50:
    atual=20
elif atual == 20:
    atual = 10
elif atual ==10:
    atual = 5
elif atual == 5 :
    atual = 1
    cédulas = 0

#
tabuada = 1
while tabuada<=10:
numero = 1
while numero <=10:
    print("%d x %d = %d" % (tabuada,numero,tabuada*numero))
    numero+=1
    tabuada+
