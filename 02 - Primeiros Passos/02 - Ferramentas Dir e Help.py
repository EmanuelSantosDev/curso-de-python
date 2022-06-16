"""
Dir

  - Apresenta no terminal uma lista de funções e métodos que podem ser
    utilziados em algum tipo de dado

  - Sintaxe: dir(valor/tipo de dado)

  - Se rodar diretamente no interpretador Python, via terminal, ele vai mostrar
    todos os pacotes de funções disponíveis para o arquivo:

    terminal: python
    terminal: >>> dir()
    output: ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
    terminal: >>> dir(__builtins__)
"""


print(dir('urso'))
print(dir(18))
print(dir(float))


"""
Help 

  - Apresenta as instruções de utilização das funções e métodos disponíveis
    para determinado tipo de dado 

  - Sintaxe: help(funcao) ou help(valor/tipo_de_dado.método/função) 
"""


print(help('dudu'.title))
print(help(str.upper))
