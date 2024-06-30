"""
Programação Estruturada

"""

"""
For - muito parecida com a estrutura While, porém, uitiliza elementos diferentes da lista. OU seja,
      vai até o final da lista. 

"""

lista=[1,2,3,4,5, 10]
for i in lista:
    print(i)

busca=10
for i in lista:
    if i ==10:
        print("Encontrou o elemento:",i)
        break

# Funcao Range - "substitui" a lista;
for i in range (10):
    print(i)

for i in range(1,11):
    print(i, end=' ') # esse end siginifa você está dizendo para o print terminar cada item com um espaço 
                      # em vez de uma nova linha

print("","\n")
for i in range(2,11,2):
    print(i, end=' ')

print("","\n")
nome="blockchain"
for letra in nome:
    print(letra, end= " ")