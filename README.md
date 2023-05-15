# dvs-info-db

> DVS info databse

> The database displays data on automated remote control objects and installed equipment

live version NOT available anymore (Amazon AWS started to charge my plan)
AWS online page login for testing purposes (with full editing permissions)

Username: mc_alfa

Password: testaparole1

### Installation (to run locally)

1. Install dependencies from requirements.txt

requirements are:
```
asgiref==3.3.4
Django==3.2.3
mysqlclient==2.0.3
pytz==2021.1
sqlparse==0.4.1
```

install using pip:
```
pip install -r requirements.txt
```

2. Import "DVS.sql" to your database
```
mysql -u root -p DVS < ..../dvs-info-db/DVS.sql
```

3. Change database username and password in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DVS',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'your_user_name',
        'PASSWORD': 'your_password',
    }
}
```


### Description

* Using mySQL database with 4 tables
* Ability to add, edit or delete new object or equipment which is part of an object
* Analytic graphs, that display specific views of mysql data
* User authentification, group policy and permissions

