# Git e GitHub (Básico)

## Configurando a Identificação no Git

```
git config --global user.name "Seu nome"
git config --global user.email "Seu email de cadastro do Github"

git config --list
```
---

## Mostrar Arquivos Ocultos (Windows)

- *Iniciar -> Opções do explorador de arquivos/Modo de Exibição*
- **DESMARCAR**: "Ocultar as extensões dos tipos de arquivos conhecidos"
- **MARCAR**: "Mostrar arquivos, pastas e unidades ocultas"

---

## Configurar a chave SSH para o GitHub

1. Gerar uma chave SSH no seu computador:
    - [Gerando Chave SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
1. Cadastrar essa chave no seu Github
    - abrir e copiar a *Chave Pública* através do bloco de notas
    - *GitHub/Settings/SSH and GPG keys/SSH keys/New SSH key*
    - dar um "título para o computador" e colar a chave pública

---

## Iniciando um Repositório Git

**Na pasta do projeto:**

```
git init
git add .
git commit -m "Mensagem explicativa"
git branch -M main
```
---

## Criando o Repositório no GitHub

- O próximo passo é criamos um novo repositório VAZIO no GitHub. 
- **IMPORTANTE**: selecionar o link **SSH** na página do GitHub.

---

## Conectando o Repositório Remoto ao Repositório Local e Enviando o Primero Push

```
git remote add origin git@github.com:seuusuario/seurepositorio.git
git push -u origin main
```

---

## Verificando o Status do Repositório

```
git status
```

---

## Salvar um Novo Commit

```
git add .
git commit -m "Mensagem explicativa"
git push
```
---

## Clonar e modificar um projeto de um repositório remoto

No GitHub selecionar _Clone/SSH_.  
Abrir o GitBash no diretório que será salvo o projeto e seguir os passos abaixo:

```
git clone git@github.com:seuusuario/seurepositorio.git
git add .
git commit -m "Mensagem explicativa"
git push
```

---

## Verificando o Histórico de Versões

```
git log
git log --oneline
```

---

## Fases de um Arquivo através do Git

1. Modified, Untracked e Deleted
1. Staged
1. Commited

---

## Git diff

```
git diff
git diff "nome do arquivo"
```

---

## Git checkout

- Permite modificar temporariamente os arquivos do projeto ao estado de um dado commit ou branch
- Cada commit possui um código, que pode ser utilizado para referenciar o commit 
- O último commit do histórico do branch corrente também pode ser referenciado pela palavra ``HEAD``
- É possível referenciar um commit 'N' versões antes de ``HEAD`` usando ``~N``, por exemplo:
    - ``HEAD~1`` (penúltimo commit)
    - ``HEAD~2 ``(antepenúltimo commit)

```
git checkout "código do commit"
git checkout HEAD~1
```

**O Git Bash estará indicando que estamos em outro commit**,

**Retornando para a o 'final' do branch:**

```
git checkout "nome-do-branch"
git checkout main
```

**IMPORTANTE**: antes de fazer o checkout para voltar para HEAD, certifique-se de que não haja mudanças nos arquivos fazendo um `git status`. Se você acidentalmente mudou alguma coisa, desfaça as modificações usando:

```
git reset
git clean -df
git checkout -- .
```

---

## Arquivo .gitignore

- É um arquivo que indica o que NÃO deve ser salvo pelo Git.
- Geralmente o arquivo *.gitignore* fica salvo na pasta principal do repositório. Mas também é possível salvar outros arquivos *.gitignore* em subpastas do repositório, para indicar o que deve ser ignorado por cada subpasta:
    - uma pasta para Frontend
    - uma pasta para Backend
        - cada uma com seu respectivo *.gitignore*

**Casos comuns de arquivos que não devem ser salvos pelo Git:**

- **Arquivos compilados**
    - Linguagens compiladas (C, C++, Java, C#, etc.) geram arquivos de código compilado para executar o programa localmente.
- **Arquivos de bibliotecas externas**
    - Projetos reais utilizam bibliotecas externas.
- **Arquivos de configuração da sua IDE**
    - IDE's podem salvar uma subpasta com arquivos de configuração na pasta do projeto.
- **Arquivos de configuração do seu sistema**
    - Por exemplo, sistemas Mac podem gravar uma subpasta ``.ds_store`` na pasta do projeto

---

## Remover arquivos da área de stage

```
git reset
```

---

## Como desfazer modificações não comitadas

Apaga as alterações e volta o projeto ao estado do último commit. 

*"Fiz algumas modificações, não ficaram boas, quero apagá-las e voltar o projeto ao estado que estava no momento do último commit"*

```
git reset
git clean -df
git checkout -- .
```

---

## O que fazer quando abre o editor VIM

Estas ações podem abrir o editor VIM no terminal:
- Fazer um commit sem mensagem
- Fazer um merge de três vias

**Habilitar o modo de edição:**

```
i
```

**Sair do VIM, salvando as alterações:**

```
<ESC>
:wq
<ENTER>
```

**Sair do VIM, descartando as alterações:**

```
<ESC>
:q!
<ENTER>
```

---

## Como desfazer o último commit

Desfazer último commit (antes de ser enviado para o repositório remoto) sem desfazer as modificações nos arquivos:

```
git reset --soft HEAD~1
```

---

## Como deletar commits e também modificações nos arquivos

Voltar o projeto ao estado de um dado commit (deletar commits e alterações
posteriores a esse commit)

```
git reset --hard <código do commit>
```

Voltar o projeto ao estado do penúltimo commit:

```
git reset --hard HEAD~1
```

---

## Como atualizar o repositório local em relação ao remoto

```
git pull <nome do remote> <nome do branch>
git pull origin main
```

---

## Como resolver push rejeitado

Não é permitido enviar um push se seu repositório local está atrasado em relação ao histórico do repositório remoto! 

**Você tem que atualizar o repositório local:**

```
git pull <nome do remote> <nome do branch>
```

**Abrirá o VIM para edição do texto do commit. Pode manter o texto padrão e executar para sair:**

```
<ESC>
:wq
<ENTER>
```

---

## Resolvendo pull com conflito

Quando dois programadores editam o mesmo arquivo de código:

1. Analise o código fonte (a IDE apontará as diferenças)
1. Faça as edições necessárias
1. Faça um novo commit

---

## Como sobrescrever um histórico do Github

Fiz alterações no repositório local que resolveram meu problema e quero 'forçar' e 'ignorar' o histórico do GitHub.

**ATENÇÃO: ação destrutiva**

```
git push -f
```

---

## Como apontar o projeto para outro repositório remoto

Útil quando desejo "preservar" o histórico do meu projeto original e trabalhar em um novo repositório no GitHub:

1. Criar um novo projeto vazio no GitHub
1. Aplicar o código abaixo no GitBash:

```
git remote set-url origin git@github.com:seuusuario/seurepositorio.git
git push -u origin main
```