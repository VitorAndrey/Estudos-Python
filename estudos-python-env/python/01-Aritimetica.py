#  Aritimetica ordem de resolucao

#   parenteses == ()

#   exponenciacao == **
#   radiciacao == quadradra == **(1/2) / cubica == **(1/3)

#   multiplicacao == *
#   divisao == /
#   divisao inteira == //
#   resto da divisao

#   adicao == +
#   subtracao == -

5+3*2==11
3*5+4**2==31
3*(5+4)**2==243

#------------------------------------------------------------------------------#

# Operacao com String

m = 'Oi'+'ola'
m = 'Oiola'

n = 'Oi'*5
n = 'OiOiOiOiOi'

#------------------------------------------------------------------------------#

# Print com determinado numero de caracteres e alinhamento.

nome = str(input('Qual o seu nome?'))
apelido = str(input('Qual o seu apelido?'))
idade = int(input('Qual a sua idade?'))
peso = float(input('Qual o seu peso?'))

print('Prazer {:>20}!'.format(nome))
print('Vou te chamar de {:=^20}!'.format(apelido))
print('Velho em ja tem {:^20}!'.format(idade))
print('Tambem peso {:<20}!'.format(peso))