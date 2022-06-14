# -----------------------------------------------------------------------------------------------

# Funções Print e Input

print('Digite uma cor:')
# Todos os dados recebidos são do tipo String

cor = input()

# -----------------------------------------------------------------------------------------------

# Print Versão 2.x
print('Você escolheu a cor %s' % cor)

# Print Versão 3.x até a versão 3.7
print('Você escolheu a cor {0}'.format(cor))

# Print Versões a partir 3.7
print(f'Você escolheu a cor {cor}')

# -----------------------------------------------------------------------------------------------

# Função 'input' imprimindo a informação para o usuário
cor2 = input('Digite uma cor: ')
print(f'Você escolheu a cor {cor2}')

# -----------------------------------------------------------------------------------------------

# Print vai sempre pular a linha por padrão
print('tomate')
print('tomate')
print('tomate')
# tomate
# tomate
# tomate

# -----------------------------------------------------------------------------------------------

# Print sem pular linha
# o print padrão é: print('tomate', end='\n')
print('tomate', end=' ')
print('tomate', end=' ')
print('tomate', end='\n')
# tomate tomate tomate

# -----------------------------------------------------------------------------------------------

# Imprimindo mais 2 ou mais variáveis

animal = input('Digite um animal: ')
fruta = input('Digite uma fruta: ')

# Versões 2.x
print('Você escolheu o animal %s e a fruta %s' % (animal, fruta))

# Versão 3.x até a versão 3.7
print('Você escolheu o animal {0} e a fruta {1}'.format(animal, fruta))

# Versões a partir 3.7
print(f'Você escolheu o animal {animal} e a fruta {fruta}')

# -----------------------------------------------------------------------------------------------

# Realizar Operações nas saídas
# é necessário realizar o 'casting' do dado primeiro
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
# Erro - vai gerar uma concatenação de Strings
print(f'A soma é: {num1 + num2}')
print(f'A soma é: {int(num1) + int(num2)}')  # Modo correto

# -----------------------------------------------------------------------------------------------
