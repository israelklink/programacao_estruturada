"""
Programação Estruturada

"""

"""
Arquivos:

Para abrir o aquivo utilizamos o parâmetro: open
r - leuitura
w - escrita, mas apaga a informação no aquivo caso exista
a - escrita e preserva o conteúdo
b - modo binário

pode combinar, tipo r + b

"""

arq=open("arquivo.txt", "w")
arq.write("blockchain")
arq.close()

arq2=open("arquivo_2.txt", "w")
x=0
for i in range(10):
    x=i+2
    print(x)
    arq2.write(str(x)+'\n')

arq2.close()


with open ("dataset.txt", "r") as arq:
    for linha in arq.readlines():
        print(linha)