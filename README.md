# Projeto Django Rest Framework - Consumindo API escola

<h2><b>Configuração</b></h2>

1. Crie uma pasta com um ambiente virtual
> python3 -m venv ./venv

2. Ative o ambiente virtual
> venv\Scripts\activate.bat

3. Instale o Django nesse ambiente virtualizado:
> pip install django

4. Crie um projeto chamado setup:
> django-admin startproject setup .

5. Instale o postman:
* Acesse o link para instalação: [Postman API Plataform](https://www.postman.com/downloads/)

6. Execute o comando para iniciar o servidor (Por padrão, o comando runserver inicia o servidor de desenvolvimento no IP interno na porta 8000)
> python manage.py runserver

7. Comando para iniciar uma aplicação:
> python manage.py startapp <nome-da-aplicacao>

8. Instalação do Django Rest Framework:
* Acesse o link para instalação: [Django Rest Framework](https://www.django-rest-framework.org/)

9. Prossiga a instalação com pip:

> pip install djangorestframework <br>
> pip install --upgrade pip <br>
> pip install markdown <br>
> pip install django-filter

<h2><b>Migration</b></h2>

1. Criar as migrações
> python manage.py makemigrations

2. Execute o comando para subir no banco todas as migrações que se tem na aplicação no caso do projeto tem-se no banco de dados uma tabela chamada Aluno e Cursos

> python manage.py migrate

3. criando usuário Django:

> python manage.py createsuperuser
* Acesse a rota: [clique aqui](http://localhost:8000/admin/login/?next=/admin/)


