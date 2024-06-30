"""
Programação Estruturada

"""

"""
Funções
- Encapsulamento
- evitar parte de códigos duplicados
- organizar o código

"""
# funcao soma
def somar(n1,n2):
    return n1+n2
print(somar(1,2))
print(somar(3,5))


#funcao somente imprimir
def imprimir():
    print('eu sou uma funcao')
    print('aprendendo python')

imprimir()

# funcao para retornar se o valor é par
def par(x):
    return x %2==0
print(par(10))
print(par(11))

# fatorial
def fat(n):
    if n==0 or n==1:
        return 1
    return n*fat(n-1)

print(fat(5))

# somar
def somar(x,y,z,f):
    return x+f(y,z)

def f(n1,n2):
    return n1+n2
print(somar(10,20,30,f))

# Funções lambda
a= lambda x: x*2
print(a(4))


# o " * " nas funções - muito importante, pode receber uma quantidade indefinidad ed enúmeros
def foo(*args):
    return sum (*args)

print(foo([1,2,3,4,5]))