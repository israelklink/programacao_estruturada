"""
Programação Estruturada

"""

"""
listas são mutáveis
listas - tipo de variável que permiter o armazenamento de vários valores, acessados por um indece

listas são definidas por []

"""

#print(help(list)) # para acessar todas as funcionalidades das listas 

lista=[] # lista vazia

listas=[1,2,3,4,5,6,6.7,8.9,"aula", "python", ["blockchain","nft", "defi"]]
print(listas)

# acessando elementos nas listas
print(listas[-1][0])

#listas são mutáveis
listas[1]='1000'
print(listas)


# utliznaod todos os valores de uma lista
lista=[1,2,3,4,5,6,7,8,9,10]
cont=0 #contado
while cont<len(lista):
    print(lista[cont], end=' ')
    cont+=1

print("")

# fatiamento das listas
lista=[1,2,3,4,5,6]
print(lista[0:3])
print(lista[-3:])

# Atenção para Listas. Esse problema é bem comum:

lista1=[1,1,2,3,4,5]
lista2=lista1
lista2[0]=10

print(lista1)  # observe que ele vai mudar o que está em lista1 e não em lista2.
               # Isso acontece pq em python tudo são objetos, então, lista2 está apenas
               # copiando a referência da lista1 e não os seus dados em si.
               #lista2 é um "apelido" de lista1, ou seja, lista2 e lista1 

# Aforma correta de copiar uma lista é:
lista3=[1,2,3,4,5]
lista4=lista3[:]
lista4[0]=15
print(lista4)

#adicionando um elemento ao final da lista
lista=[1,2,3]
lista.append('clockchain')
print(lista)

#concatenar duas listas
l1=[1,2,3]
l2=[4,5,6,2]
l1_l2=l1+l2
print(l1_l2)

#remover elementos 
lista4.remove(2)
print(lista4)