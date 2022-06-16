"""

Variáveis 
---------

Existem 2 tipos de variaveis:

    1) Variável Global: que pode ser manipulada ao longo de todo o código
    2) Variável Local: que pode ser manipulada apenas em uma determinada parte do programa

Como declarar variáveis?

    nome = dado

"""


idadeJoao = 17
idade_joao = 17
IDADE_JOAO = 17
idadejoao = 17  # errado


"""

Tipos de Dados
--------------

    - 'int'

    - 'float'

    - 'bool'

    - 'str': 

        - para gerar uma string invertida -> [::-1]
        - para 'recortar' uma parte -> [indice_inicial:indice_final]

    - 'complex': Números Complexos. 

        - Normalmente é usado em cálculos geométricos e científicos.
        - Um tipo complexo contem duas partes: a parte 'real' e a parte 'imaginária', 
          sendo que a parte imaginária contem um 'j' no sufixo.

"""

# Inteiro
idade = 17
print(type(idade))  # <class 'int'>

# Flutuante
peso = 76.1
print(type(peso))  # <class 'float'>

# Booleano
var_bool = True
print(type(var_bool))  # <class 'bool'>

# String
nome = "João dos Santos"
print(type(nome))  # <class 'str'>

# String Invertida
print(nome[::-1])  # sotnaS sod oãoJ

# String Recortada
print(nome[9:15])  # Santos

# Número Complexo
num_complexo = 10 - 2j
print(type(num_complexo))  # <class 'complex'>


""" 

Atribuição Múltipla
-------------------

    - declaração de múltiplas variáveis em uma única linha
    
"""


a1, a2, a3, a4, a5 = 1, 2.5, True, 2j, 'sim'

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
# 1
# 2.5
# True
# 2j
# sim