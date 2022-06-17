# ----------------------------------------------------------------------

# ESTRUTURAS LÓGICAS

# and : True apenas se todas as condições forem True
# or  : True quando pelo menos uma condição for True
# is  : Comparação entre valores similar ao '=='
# not : Inverte o resultado, retorna False se True e vice-versa

# ----------------------------------------------------------------------

# Operador 'and'

comida = True
agua = True

if comida and agua:
    print('Cachorro Feliz')

# ----------------------------------------------------------------------

# Operador 'or'

ganhou = False
empatou = True

if ganhou or empatou:
    print('O importante é não perder')

# ----------------------------------------------------------------------

# Operador 'not'

login = False

if not login:
    print('deslogado')
else:
    print('logado')

# Output: deslogado
# login, de False se torna True, o que o validou para entrar no bloco 'if'

# ----------------------------------------------------------------------
