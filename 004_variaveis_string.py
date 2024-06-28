"""
Programação Estruturada

"""

"""
Variáveis String: armazena uma cadeia de caracteres

- 
- 
- 
- 

"""

nome ="Isra"
sobrenome=" Jr"
print(nome)
print(type(nome))
print(nome[0], nome[1], nome[2], nome[3])
print(len(nome))
print(nome[0:3])
print(nome[1:])
print(nome[-3])
print(3*nome)

nome_completo=nome + sobrenome
print(nome_completo)

idade=20
irma=" Maria"
print('João tem %d anos e a sua namorada se chama %s' % (idade, irma))  #%d e %s é um marcado de posição

media = 3.12141513
print('%.3f' % media)

nome = "Isra"
nome = "Isra N"  # Eu não auterei a string, na verdade, foi criado um novo objeto.
print(nome)