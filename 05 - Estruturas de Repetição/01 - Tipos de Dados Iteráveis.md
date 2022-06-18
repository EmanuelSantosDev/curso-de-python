# Tipos de Dados Iteráveis


## Strings


Uma String é uma sequência _iterável_ que possui um indice de acesso.

Podemos acessar este indíce da esquerda para a direita e da direita para a esquerda:
````python
nome = 'Emanuel'

print(nome[2])  # a
print(nome[-1])  # l
print(nome[-3])  # u
print(nome[2:-2])  # anu
````


## Listas, Tuplas, Dicionários e Sets


Exemplo de lista:
````python
lista = [1, 2.5, Tru, "Samuel"]
````


## Função range()


O que ela faz?  
É uma função que cria um intervalo de números escolhidos pelo usuário.
````python
numero = range(2, 10)  # cria um intervalo de 2 a 9
print(numero)  # range(2, 10)
````