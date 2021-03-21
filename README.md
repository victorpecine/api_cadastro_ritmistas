# API para cadastro de ritmistas

Desenvovlido em Python 3.9.2

## APP instalados

[Django 3.1.7](https://docs.djangoproject.com/en/3.1/topics/install/)
[Django Rest Framework 3.12.2](https://www.django-rest-framework.org/)
[MySQL Connector Python 8.0.23](https://pypi.org/project/mysql-connector-python/)
[MySQL Client 2.0.3](https://pypi.org/project/mysqlclient/)


## Aplicação
* Realizar o cadastro de um novo membro com os campos
    * Nome
    * Curso
    * CPF
    * Telefone
    * Grupo (show, competições e/ou geral)
    * Naipe(instrumento)
    * Data de nascimento
    * Data de entrada
    * Data de saída

* Criar, consultar, editar, e deletar
    * Ritmistas
    * Cursos
    * Naipes
    * Grupos

## Como utilizar a API
* Criar um ambiente virtual
'''
python -m venv ./venv
'''

* Ativar o ambiente virtual (Windows)
'''
 .\Scripts\activate.bar
'''

* Instalar os app
'''
pip install -r requirements.txt
'''

* Fazer as migrações para o banco de dados
'''
python manage.py makemigrations
'''
'''
python manage.py migrate
'''

* Criar um login e senha para o admin
'''
python manage.py createsuperuser
'''

* Iniciar o servidor
'''
python manage.py runserver
'''

* Acessar o localhost e fazer o login como superuser
'''
localhost:8000/admin/
'''