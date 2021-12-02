# Projeto Django Rest Framework - Curso Alura

<h2><b>Principais Bibliotecas</b></h2>

- [Python](https://www.python.org/) - Linguagem de Programação
- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework para construação de APIs da Web

<h2><b>Configuração/Execução do projeto</b></h2>

1. Crie uma pasta com um ambiente virtual
```bash
$ python3 -m venv ./venv
```

2. Ative o ambiente virtual
```bash
$ venv\Scripts\activate.bat
```

3. Instale o Django nesse ambiente virtualizado:
```bash
$ pip install django
```

4. Crie um projeto chamado setup:
```bash
$ django-admin startproject setup
```

5. Instale o postman:
* Acesse o link para instalação: [Postman API Plataform](https://www.postman.com/downloads/)

6. Execute o comando para iniciar o servidor (Por padrão, o comando runserver inicia o servidor de desenvolvimento no IP interno na porta 8000)
```bash
$ python manage.py runserver
```

7. Comando para iniciar uma aplicação:
```bash
$ python manage.py startapp <nome-da-aplicacao>
```

8. Instalação do Django Rest Framework:
* Acesse o link para instalação: [Django Rest Framework](https://www.django-rest-framework.org/)

9. Prossiga a instalação com pip:
```bash
$ pip install djangorestframework
$ pip install --upgrade pip
$ pip install markdown
$ pip install django-filter
```

<h2><b>Migration</b></h2>

1. Criar as migrações
```bash
$ python manage.py makemigrations
```

2. Execute o comando para subir no banco todas as migrações que se tem na aplicação no caso do projeto tem-se no banco de dados uma tabela chamada Aluno e Cursos
```bash
$ python manage.py migrate
```

3. criando usuário Django:
```bash
$ python manage.py createsuperuser
```
* Acesse a rota: [clique aqui](http://localhost:8000/admin/login/?next=/admin/)


