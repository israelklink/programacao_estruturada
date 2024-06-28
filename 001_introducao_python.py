"""
Comentario

"""

# també utilizamos # para comentarios

print("ola mundo") # vai exibir na tela ola mundo

# saida de dados
print("ola, mundo", end="---") #
print("ola mundo")
print("Helena eh linda", sep="--") 

#tipos de dados primitivos
print(4, -3, 2, 8)    # int 
print(2.3, 5.6, 7.8)  # float
print(True, False)    # bool
print("abc", "dce")   # str
print(None)           # None Type

print(2)
print("2")
print(3.0)

# Caractere de escape - escape char (\)
print("olá, \"mundo\"")
print("olá, \'mundo\'")
print('olá, "mundo"')
print("olá,\nmundo")
print("olá,\tmundo")
print("C:\\Projetos")
print("C:\\\\Projetos")

print("""Este é um texto
com múltiplas linhas.""")
print('''Este é um texto
com múltiplas linhas''')

#input - variáveis
nome=input("qual o seu nome?")
print("olá", nome)

#atenção - não existem constantes em python
# precisamos definir
Pi=3.1415