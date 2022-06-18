# Configuração Ambiente Python


## Instalação Python e PIP


- Download via site oficial do Python
- Ao instalar marcar _"Add Python 3.9 to PATH"_  

**Confirmar instalação do Python e do PIP:**

    python --version
    pip --version

**Atualizando o PIP para a versão mais atual:**

    pip install --upgrade pip

**Confirmar atualização do PIP:**

    pip --version


## Instalação VSCode


- Download do VSCode via site oficial
- Criar o diretório do projeto e abrir no VSCode ou realizar o clone via Git/GitHub


## Criando o Ambiente Virtual

Criar ambiente virtual (terminal PowerShell do VSCode):

    python -m venv venv

O PowerShell vem restrito por padrão. Então, é necessário abrí-lo como _Administrador_ e executar o comando abaixo e selecionar a opção `[S]`:

    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Ativar o Ambiente Virtual
- **OBSERVAÇÃO**: A extensão *Python* da Microsoft já ativa automaticamente
- Encerrar e abrir um novo terminal no VSCode 
- Ativar o Ambiente Virtual (navegar até o script de ativação):
```
.\venv\Scripts\activate.ps1
```

**Enquanto o Ambiente Virtual estiver *ativo* tudo o que for instalado irá para o ambiente virtual.**

Desativar um ambiente virtual:

    deactivate


## Extensões VSCode


- Logar com o GitHub para ativar a _Sincronização de Configurações_
- **Python (Microsoft)** - criar um arquivo Python e selecionar o interpretador Python do ambiente virtual (venv) na barra inferior do VSCode 


## Instalando autopep8 no VSCode


- Instalar **autopep8**: rodar o atalho `shift + alt + f` dentro de um arquivo _.py_ o qual irá solicitar automaticamente a instalação do _autopep8_


## Instalando o Linter Pylint

- ``Ctrl + Shift + P``
- Digitar _select linter_
- Selecionar **pylint**
- Clicar em _Instalar_ na janelinha que abrirá. Caso não abra, apenas seguir os passos abaixo que ele solicitará a instalação durante a execução.
- Criar um arquivo Python com erro de código intencional (printar uma variável não declarada)
- ``Ctrl + Shift + P``
- Digitar _run linting_
- Checar se a "sugestão de correção" (mouse sobre o warning) está indicando o _pylint_


## Configurações no VSCode


- _Configurações/format on save_  (no campo de pesquisa)
- _Configurações/auto save_ (no campo de pesquisa)
    - _Files: Auto Save -> afterDelay_
    - _Files: Auto Save Delay -> 1000_


## PIP Freeze

Lista no terminal os pacotes Python instalados no seu ambiente:

    pip freeze

Gerando o _requirements.txt_:

    pip freeze > requirements.txt

Instalando as bibliotecas declaradas no _requirements.txt_:

    pip install -r requirements.txt