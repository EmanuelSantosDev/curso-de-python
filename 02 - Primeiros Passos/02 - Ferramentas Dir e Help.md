# Ferramenta dir()


Apresenta no terminal uma lista de funções e métodos que podem ser utilizados em algum tipo de dado.

Sintaxe: 
````python
dir(valor/tipo de dado)
````

Se rodar diretamente no interpretador Python, via terminal, ela vai mostrar todos os pacotes de funções disponíveis para o arquivo:

````
input: python
input: >>> dir()
output: ['__annotations__', '__builtins__', '__doc__'__loader__', '__name__', '__package__', '__spec__']
input: >>> dir(__builtins__)
````

Em um arquivo _.py_:
````python
print(dir('urso'))
print(dir(18))
print(dir(float))
````


# Ferramenta help()


Apresenta as instruções de utilização das funções e métodos disponíveis para determinado tipo de dado.

Sintaxe: 
````python
help(funcao)
help(valor/tipo_de_dado.método/função) 
````

Não utilizar os 'parênteses' ao final do nome da função, pois não estamos à invocando:
  
````python
print(help('dudu'.title))
print(help(str.upper))
````