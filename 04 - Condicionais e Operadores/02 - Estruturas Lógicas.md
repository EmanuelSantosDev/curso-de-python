# Estruturas Lógicas

- ``and`` : é ``True`` apenas se todas as condições forem ``True``
- ``or``  : é ``True`` quando pelo menos uma condição for ``True``
- ``not`` : inverte o resultado, retorna ``False`` se ``True`` e vice-versa


# Operador 'and'


````python
comida = True
agua = True

if comida and agua:
    print('Cachorro Feliz')
````

## Operador 'or'


````python
ganhou = False
empatou = True

if ganhou or empatou:
    print('O importante é não perder')
````

## Operador 'not'


````python
login = False

if not login:
    print('deslogado')
else:
    print('logado')

# Output: deslogado
# login, de False se torna True, o que o validou para entrar no bloco 'if'
````