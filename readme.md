## Ambiente virtual python
```
    pip install virtualenv
    virtualenv vpython
    vpython\Scripts\activate 
```

## install django e criação de projeto
```
    python -m pip install Django
    
    #cria projeto
    django-admin startproject app
    cd app

    #cria app
    python manage.py startapp app1
    
    adicionar app1 em settings.py
    INSTALLED_APPS = [
    'app1',

    python manage.py migrate
    python manage.py runserver

    
```


## Criando usuario
```
    python manage.py createsuperuser (veni@veni.com/veni)
```


## Criando modelos e atualizando

```
    #alterar ou adicionar modelos
    python manage.py makemigrations
    python manage.py migrate
    #logo apos da pra criar o fixture
    
```

## carregando e descarregando seeds 

```
    python manage.py loaddata fixtures/initial.json

```