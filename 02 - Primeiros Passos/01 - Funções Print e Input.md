# Funções print() e input()


```python
print('Digite uma cor:')

cor = input()

# Todos os dados recebidos são do tipo String
```


## Versões da função print()


```python
# Print Versão 2.x

print('Você escolheu a cor %s' % cor)

# Print Versão 3.x até a versão 3.7

print('Você escolheu a cor {0}'.format(cor))

# Print Versões a partir 3.7

print(f'Você escolheu a cor {cor}')
```


## Fusão das funções print() e input() 


```python
cor = input('Digite uma cor: ')
```


## A função print() vai sempre pular a linha por padrão    

  
```python
print('tomate')
print('tomate')
print('tomate')
```

Output:
```
tomate
tomate
tomate
```


## Função print() sem pular linha


O print() padrão é: 
````python
print('tomate', end='\n')
````

Alterando o seu comportamento:
````python
print('tomate', end=' ')
print('tomate', end=' ')
print('tomate', end='\n')
````

Output:
````
tomate tomate tomate
````


## Imprimindo duas ou mais variáveis em um mesmo print()


````python
animal = input('Digite um animal: ')
fruta = input('Digite uma fruta: ')

# Versões 2.x

print('Você escolheu o animal %s e a fruta %s' % (animal, fruta))

# Versão 3.x até a versão 3.7

print('Você escolheu o animal {0} e a fruta {1}'.format(animal, fruta))

# Versões a partir 3.7

print(f'Você escolheu o animal {animal} e a fruta {fruta}')
````


## Operações Matemáticas na Função Print()

Para realizar Operações Matemáticas nas saídas é necessário realizar o 'casting' do dado primeiro:

````python
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(f'A soma é: {num1 + num2}') # Erro - vai gerar uma concatenação de Strings
print(f'A soma é: {int(num1) + int(num2)}')  # Modo correto
````


## Função print() com Múltiplas Linhas

````python
print(f'O personagem tem cabelos na cor {cor_do_cabelo.upper()}\n'
      f'A cor da pele é {cor_da_pele.upper()}\n'
      f'A sua classe é {classe.upper()}\n'
      f'A sua idade é de {idade} anos de idade\n'
      f'Sua altura é de {altura}\n'
      f'Sua habilidade específica é {habilidade_especifica.upper()}')
````