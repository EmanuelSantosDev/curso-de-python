# Estruturas Condicionais


## If...Else


````python
nota = float(input('Digite a sua nota: '))

if nota > 6.9:
    print('Você foi APROVADO')
else:
    print('Você foi REPROVADO')
````


## If...Elif...Else


````python
nota = float(input('Digite a sua nota: '))

if nota >= 7.0:
    print('Você foi APROVADO')
elif nota >= 5.0:
    print('Você está em RECUPERAÇÃO')
else:
    print('Você foi REPROVADO')
````


## Utilizando Variável Booleana

Utilizando uma Variável Booleana não precisa utilizar operadores de comparação:


````python
login = True

if login:
    print('Acesso Permitido')
````