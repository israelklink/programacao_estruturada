"""
Programação Estruturada

"""

"""
Condições 

- if <condicao> :
  else - se a condição do if for negada

"""

idade=20

if idade >=18:
    print("Maior de idade")
else:
    print("Menor de idade")

if idade >=18:
    if idade >=60:
        print("idoso")
    else:
        print("adulto")
else:
    print("menor de idade")

# Exemplo de entrada de opção
opcao=int(input("entre com a opcao:"))

if opcao ==1:
    preco=15
    print("preco",preco)
elif opcao==2:
    preco=20
    print("opcao",preco)
elif opcao>3:
    preco=40
    print("opcao",preco)

