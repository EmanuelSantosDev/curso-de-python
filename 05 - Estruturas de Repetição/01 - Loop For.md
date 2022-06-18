# Loop For


## Tipos de Dados Iteráveis


### Strings


Uma String é uma sequência _iterável_ que possui um indice de acesso.

Podemos acessar este indíce da esquerda para a direita e da direita para a esquerda:
````python
nome = 'Emanuel'

print(nome[2])  # a
print(nome[-1])  # l
print(nome[-3])  # u
print(nome[2:-2])  # anu
````


### Listas, Tuplas, Dicionários e Sets


Exemplo de lista:
````python
lista = [1, 2.5, Tru, "Samuel"]
````


### Função range()


O que ela faz?  
É uma função que cria um intervalo de números escolhidos pelo usuário.
````python
numero = range(2, 10)  # cria um intervalo de 2 a 9
print(numero)  # range(2, 10)
````


# Loop For na Prática


### Aplicação com String


````python
seriado = 'Todo Mundo Odeia o Chris'

for letra in seriado:
    print(letra)  # Output: imprimirá uma letra por vez
````


### Aplicação com Lista
````python
lista_de_time = ['Grêmio', 'Inter', 'São Paulo', 'Palmeiras', 'Flamengo']

for time in lista_de_time:
    print(time)  # Output: imprimirá o nome de cada um dos times
````


### Aplicação com a Função range()


````python
# Imprime valores de 1 a 100

intervalo_de_numeros = range(1, 101)  

for i in intervalo_de_numeros:
    print(i)

# range() com intervalo padrão (Imprime valores de 0 a 200)

numeros = range(201) 
 
for i in numeros:  
    print(i)

# range() com sequência negativa (Imprime valores de -20 a 299)

numeros = range(-20, 300) 

for i in numeros:   
    print(i)

# range() com Intervalores Pré-Definidos (Criará um intervalo 'de 3 em 3')

numeros = range(3, 19, 3)  

for i in numeros:
    print(i, end=' ')  # 3 6 9 12 15 18

# range() com Intervalores Pré-Definidos + Sequencia Negativa
# Criará um intervalo descrescente
# Output: 18 15 12 9 6 3 0 -3 -6 -9 -12 

numeros = range(18, -15, -3)

for i in numeros:
    print(i, end=' ')  # 3 6 9 12 15 18
````


## Sequência de For Aninhados


````python
fruta = 'abacate'
sequencia = range(1, 4)

for letra in fruta:
    if letra == 'a':
        for num in sequencia:
            print('Achei a letra a')

# Iprimirá 9 vezes a mensagem 'Achei a letra a'
````


## Break


````python
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for letra in alfabeto:
    if letra == 'g':
        break
    print(letra)  # imprimirá de 'a' à 'f'
````


## Continue


````python
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

for letra in alfabeto:
    if letra == 'g' or letra == 'm' or letra == 'v':
        continue
    print(letra)  # imprimirá de 'a' à 'f', pulando as letras 'g', 'm' e 'v'
````


## Método enumerate()


````python
# Adiciona um contador para cada elemento que foi desmembrado na sequência.
# Cria uma relação de 'Índice' e 'Dado'.

heroi = 'Batman'
for valor in enumerate(heroi):
    print(valor)

# (0, 'B')
# (1, 'a')
# (2, 't')
# (3, 'm')
# (4, 'a')
# (5, 'n')

for contador, letra in enumerate(heroi):
    print(f'A {contador + 1}ª letra é: {letra}')

# A 1ª letra é: B
# A 2ª letra é: a
# A 3ª letra é: t
# A 4ª letra é: m
# A 5ª letra é: a
# A 6ª letra é: n

for posicao, valor in enumerate(range(10, 21)):
    print(f'{posicao + 1}º -> {valor}')

# 1º -> 10
# 2º -> 11
# 3º -> 12
# 4º -> 13
# 5º -> 14
# 6º -> 15
# 7º -> 16
# 8º -> 17
# 9º -> 18
# 10º -> 19
# 11º -> 20
````