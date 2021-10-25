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
    #cria app
    python app/manage.py startapp app1

    python app/manage.py migrate
    python app/manage.py runserver
```


## Criando usuario
```
    python app/manage.py createsuperuser (veni@veni.com/veni)
```


## Criando modelos

```
    python manage.py makemigrations

```