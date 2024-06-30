"""
Programação Estruturada

"""

"""
Tupla - é um objeto imutável, o seu estado é congelado na inicialização.
Lista é mutável. 

Tupla é entre (), exemplo: tupla=(1,2,3); tupla2=('aaa',1,2,'bbb')
Lista é entre []

"""

tupla=('teste',1,2,3)
print(tupla)

# A tupla é imutável, observe que vai dar um erro na tentativ de mudar o elemento.
#tupla[0]='teste02' 

#acessando elementos nas tuplas
print(tupla[1]) # acessando o segundo elemento na tupla. 
print(tupla[1:2]) # fatiamento
print("")
#print(help(tuple)) # para acessar os métodos das tuplas

tupla_2=(1,2,3,4,4,4,4,4,5)
print("quantas vezes aparece o número 4:",tupla_2.count(4))