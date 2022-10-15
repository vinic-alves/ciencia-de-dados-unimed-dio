# Conhecendo os métodos de string em python

#Exemplos

curso = "pYtHon"

print(curso.upper()) #muda a string para uppercase, maíúscula
# resultado >>> Python

print(curso.lower()) # coloca em letra minuscula
# resultado >>> python
print(curso.title()) # coloca a primeira em maiúsculo apenas
# resultado >>> Python

#Eliminando espaçõs
curso = "  Python"
print(curso.strip()) #Elimina espaços
print(curso.lstrip()) # remove o espaço da esquerda
print(curso.rstrip) # remove o espaço da direita

# Junções e centralização

curso = "Python"

print(curso.center(10, '#'))
# >>> "##Python##"

print(".".join(curso))
# >>> "P.y.t.h.o.n"




