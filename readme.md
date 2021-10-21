## Ambiente virtual python
```
    pip install virtualenv
    virtualenv vpython
    vpython\Scripts\activate 
```

## install django e criação de projeto
```
    python -m pip install Django
    django-admin startproject app
    python app/manage.py migrate
    python app/manage.py runserver
```


## Criando usuario
```
    python app/manage.py createsuperuser (veni@veni.com/veni)
```