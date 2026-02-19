#tabela = { "Alface" : 0.45,
 #          "Batata" : 1.20,
  #         "Tomate" : 2.30,
   #        "Feijão" : 1.50}
#while True:
 #   produto=input("Digite o nome do produto, fim para terminar")
  #  if produto == "fim":
   #     break
    #if produto in tabela:
     #   print("Preço %5.2f") % tabela[produto]
    #else:
     #   print("Produto não encontrado")

#del tabela["Tomate"]
#print(tabela)

estoque = { "tomate": [1000,2.30],
            "alface": [500,0.45],
            "batata": [2001,1.20],
            "feijão": [100, 1.50]}
venda = [["tomate",5],["batata",10],["alface",5]]
total=0
print("Vendas:\n")
for operação in venda :


for chave, dados in estoque.items():
    print("Descrição:",chave)
    print("Quantidade:", dados[0])
    print("Preço: %6.2f\n" % dados[1])











#tabela["Cebola"]=1.20
#print(tabela.keys())
#rint(tabela.values())