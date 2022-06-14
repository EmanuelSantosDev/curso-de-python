# Configuração Ambiente Python


## Python e PIP


- Download via site oficial do Python
- Ao instalar marcar _"Add Python 3.9 to PATH"_  

**Confirmar instalação do Python e do PIP:**

    python --version
    pip --version

**Atualizando o PIP para a versão mais atual:**

    pip install --upgrade pip

**Confirmar atualização do PIP:**

    pip --version

---

## VSCode


- Download do VSCode via site oficial
- Criar o diretório do projeto e abrir no VSCode
---

## Extensões do VSCode


- Instalar a Extenção **Python** da **Microsoft** 
- Instalar **autopep8**: rodar o atalho `shift + alt + f` dentro de um arquivo _.py_ o qual irá solicitar automaticamente a instação do _autopep8_

---

## Configurações VSCode


- _Configurações/auto save_ (no campo de pesquisa)
    - _Files: Auto Save -> afterDelay_
    - _Files: Auto Save Delay -> 1000_
- _Configurações/format on save_  (no campo de pesquisa)

---

## Ambiente Virtual

Criar ambiente virtual (terminal PowerShell do VSCode):

    python -m venv <nome-do-ambiente-virtual>
    python -m venv venv

O PowerShell vem restrito por padrão. Então, é necessário abrí-lo como _Administrador_ e executar o comando abaixo e selecionar a opção `[S]`:

    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Ativar o Ambiente Virtual
- Encerrar e abrir um novo terminal no VSCode 
- Ativar o Ambiente Virtual (navegar até o script de ativação):
```
.\venv\Scripts\activate.ps1
```

**Enquanto o Ambiente Virtual estiver *ativo* tudo o que for instalado irá para o ambiente virtual.**

Desativar um ambiente virtual:

    deactivate

---

## PIP Freeze

Lista no terminal os pacotes Python instalados no seu ambiente:

    pip freeze

Gerando o _requirements.txt_:

    pip freeze > requirements.txt

Instalando as bibliotecas declaradas no _requirements.txt_:

    pip install -r requirements.txt