"""
Programação Estruturada

"""

"""
Repetições - executa várias em uma parte de um programa 

Estruturas de Repetição 
- while - quando não sabemos quantas vezes executar a repetição, ou seja, enquanto a repetição for verdadeira.
- for - quando queremos acessar todos os elementos de uma coleção de dados.

"""

cont=1
while cont <= 10:
    cont +=1     #cont+1
    print(cont)



cont=1
while cont <= 100:
    if cont %2 ==0:
        print(cont, end=" ")
    cont +=1

# Exercicio Tabuada
tabuada=1
while tabuada <= 10:
    numero =1 
    while numero <= 10:
        print('%d x%d=%d' % (tabuada, numero, tabuada*numero) )
        numero +=1
    tabuada +=1



