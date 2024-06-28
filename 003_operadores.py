"""
Programação Estruturada

"""

"""
Operadores realacionais:
Retornam um booleano (True/False)

- igualdade ==
- maior que >
- menor que < 
- diferente !=
- maior ou igual >=
- menor ou igual <=

"""
n1=10
n2=20
print(n1>n2)
print(n1<n2)
print(n1==n2)
print(n1>=n2)
print(n1==n2/2)

media_aluno= 6.5
media_aprovado=7
resultado=media_aluno>=media_aprovado
print("aluno aprovado:",resultado)

"""
Operadores aritméticos
Quando os operandos são númeors 

- soma 
- subtração
- multiplicação
- divisão
- potência
- divisão inteira
- módulo

"""
x=9.345
y=7.765

print(x-y)
print(x+y)
print(x*y)
print(x/y)
print(x**y)
print(x//y) # divisão interira
print(x%y)  # qual é o resto

print(round(x + y, 2)) #round arredonda o resultado da soma para 2 casas decimais

"""
Operadores lógicos

not  - negação
and  - conjunção - resulta em verdadeiro somente se os dois operadores forem verdadeiros
or   - disjunção

"""
foi_aprovado= True
nao_foi_aprovado= not foi_aprovado
print(nao_foi_aprovado)

print(True and False)
print(True and True)
print(False and False)

print(True or False)
print(False or False)

"""
Operação and
- Se o primeiro operando é True, retorna o segundo operando
- Se o primeiro operando é False, retorna o primeiro operando

Operação or
- Se o primeiro operando é True, retorna o primeiro operando
- Se o primeiro operando é False, retorna o segundo operando
"""

# Exercício:

ap1 = float(input("Informe a nota da AP1: "))
ap2 = float(input("Informe a nota da AP2: "))
ac = float(input("Informe a nota da AC: "))
media = (ap1 + ap2) * 0.4 + ac * 0.2
print("A média é", round(media, 2))

