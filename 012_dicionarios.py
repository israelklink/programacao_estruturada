"""
Programação Estruturada

"""

"""

Dicionários -  são simulares as listas, porém, com propriedades de acesso diferentes.
            -  é composto por um conjunto de chaves e valores, ou seja, temos uma relação de
               chave com os valores. Se vc quer um valor, perguntamos pela chave.

"""
d={"blockchain":5, "defi":7, "nft":4}
print(d)
print(d['blockchain'])

# Mudando o valor da chave
d["defi"]=10
print(d)

#vendo todos os valores do dicionário

for i in d:
    print(d[i], end=" ")

print("")
print(d.items())
print(d.keys())
print(d.values())