# Django: Controle de Estoque 
## steps para criação de um projeto
01. Criação do repositório
> mkdir nome_da_pasta

02. acessar o repositório
> cd nome_da_pasta

03. criar o ambiente virtual 
> python -m  venv nome do ambiente virtual

04. acessar o ambiente virtual
> nome_do_ambiente_vitual\Scripts\activate
linux ou mac nome: source nome_ambiente_virtual/bin/activate 

05. instalar o pacotes (django,...)
-instalando um pacote especifico 
> pip install django
- instalando lista de pacotes 
> pip install -r requeriments.txt

06. Criação de projeto
> django-admin startproject nome_projeto .

07. Criação do app
> django-admin startapp nome_app

08.  Criação do model.py [nome_app/models.py] e configuração no arquivo settings.py [nome_projeto/settings.py]
 

09. Realizar a migrações no banco de dados
- fazer as migrações dos models
> python manage.py makemigrations
- Aplicar as migrações no bando de dados
> python manage.py migrate

10. Criação do Super Usuário
> python manage.py createsuperuser 

11. startar servidor de desenvolvimento
> python manage.py runserver 

 