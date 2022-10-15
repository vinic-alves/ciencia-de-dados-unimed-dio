nome = "Vinicius"
idade = "27"
profissao = "Programador"
linguagem = "Python"

#exemplo usando o %

print("Olá, meu nome é %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

# método format

print ("Olá, me chamo {3}. E eu tenho {2} anos de idade, trabalho como {1}." .format(
    nome,idade,profissao))