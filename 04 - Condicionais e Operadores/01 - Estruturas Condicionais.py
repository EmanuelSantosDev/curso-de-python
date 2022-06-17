# -------------------------------------------------------------------

# ESTRUTURAS CONDICIONAIS

# if
# else
# elif

# -------------------------------------------------------------------

# if...else

nota = float(input('Digite a sua nota: '))

if nota > 6.9:
    print('Você foi APROVADO')
else:
    print('Você foi REPROVADO')

# ----------------------------------------------------------------------

# if...elif...else

nota = float(input('Digite a sua nota: '))

if nota >= 7.0:
    print('Você foi APROVADO')
elif nota >= 5.0:
    print('Você está em RECUPERAÇÃO')
else:
    print('Você foi REPROVADO')

# ----------------------------------------------------------------------

# Utilizando outros tipos de dados

pais = input('Digite um pais: ')

if pais == 'Brasil':
    print('América do Sul')
elif pais == 'México':
    print('América Central')
elif pais == 'Estados Unidos':
    print('América do Norte')
elif pais == 'Inglaterra':
    print('Europa')
elif pais == 'Angola':
    print('África')
elif pais == 'Japão':
    print('Ásia')
else:
    print('Oceania')

# ----------------------------------------------------------------------

# Utilizando variável booleana não precisa utilizar operadores de comparação

login = True

if login:
    print('Acesso Permitido')

# ----------------------------------------------------------------------
