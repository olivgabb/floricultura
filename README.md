# 🌸 Floricultura

Aplicação web desenvolvida com **Python e Django** para explorar e apresentar informações sobre flores e plantas, incluindo seus nomes, categorias, preços e imagens.

## 📋 Sobre o projeto

O **Floricultura** é um projeto desenvolvido para praticar o desenvolvimento web com Django, trabalhando com organização de aplicações, templates HTML, arquivos estáticos e integração entre dados e interface.

A aplicação tem como objetivo apresentar um catálogo de plantas de forma organizada e facilitar a visualização de informações sobre cada item.

## ✨ Funcionalidades

* 🌱 Listagem de plantas cadastradas.
* 🏷️ Exibição de nomes, preços e categorias.
* 🖼️ Apresentação de imagens das plantas.
* 🔎 Visualização de informações individuais de cada planta.
* 🎨 Interface web construída com templates HTML e CSS.

## 🛠️ Tecnologias utilizadas

* **Python** — linguagem de programação.
* **Django** — framework para desenvolvimento web.
* **HTML5** — estrutura das páginas.
* **CSS3** — estilização da interface.
* **JavaScript** — recursos de interação no frontend.
* **SQLite** — banco de dados padrão do Django, caso não tenha sido configurado outro.

## 🚀 Como executar o projeto

### Pré-requisitos

* Python instalado.
* Git instalado.
* Pip disponível no ambiente Python.

### 1. Clone o repositório

```bash
git clone https://github.com/olivgabb/floricultura.git
```

### 2. Entre na pasta do projeto

```bash
cd floricultura
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Instale as dependências

Caso exista um arquivo `requirements.txt` no projeto:

```bash
pip install -r requirements.txt
```

Se ele não existir, instale o Django:

```bash
pip install django
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

### 8. Acesse a aplicação

Abra o navegador no endereço:

http://127.0.0.1:8000/

## 📁 Estrutura do projeto

```text
floricultura/
├── flores/
│   └── ...
├── floricultura/
│   └── ...
├── manage.py
└── .gitignore
```

* `flores/`: aplicação Django relacionada ao catálogo de flores e plantas.
* `floricultura/`: configurações principais do projeto Django.
* `manage.py`: utilitário para executar comandos administrativos do Django.
* `.gitignore`: define arquivos e diretórios que não devem ser versionados.

## 🎯 Objetivos de aprendizagem

Este projeto permite praticar conceitos importantes do desenvolvimento web, como:

* Criação e organização de projetos Django.
* Modelagem e consulta de dados.
* Renderização de páginas com templates.
* Integração entre backend e frontend.
* Gerenciamento de arquivos estáticos.
* Utilização do Git e GitHub para versionamento de código.

## 👨‍💻 Autor

Desenvolvido por [olivgabb](https://github.com/olivgabb).

Confira o repositório: [github.com/olivgabb/floricultura](https://github.com/olivgabb/floricultura)

---

*Projeto desenvolvido com fins de aprendizado e prática de desenvolvimento web com Python e Django.*
