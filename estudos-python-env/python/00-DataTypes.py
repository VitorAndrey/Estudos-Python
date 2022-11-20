# Definindo input como Numero inteiro ('int')
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
soma = num1 + num2

# Nova maneira de usar 'Print'
print('A adicao entre {} e {} vale: {}'.format(num1, num2, soma))


#-------------------------------------------------#

# Definindo input como Numero "com virgula" ('float')
num3 = float(input('Digite um valor decimal: '))
num4 = float(input('Digite outro valor decimal: '))
sub = num3 - num4

# Nova maneira de usar 'Print'
print('A subtracao entre {} e {} vale: {}'.format(num3, num4, sub))

#-------------------------------------------------#

# Definindo input como Texto ('str')
txt1 = str(input('Digite seu primeiro nome: '))
txt2 = str(input('Digite seu sobrenome: '))

# Nova maneira de usar 'Print'
print('Ola {}{}, seja bem vindo!'.format(txt1,txt2))

#-------------------------------------------------#