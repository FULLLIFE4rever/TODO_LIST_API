# Todo list API
![](https://img.shields.io/badge/Python-3.10.0-blue) 
![](https://img.shields.io/badge/Flask-3.0.3-orange)
![](https://img.shields.io/badge/Flask-SQLAlchemy-3.1.1-red)
![](https://img.shields.io/badge/MySQL-8.0-blue)


## Описание
«Записная книжка» 
API является записной книжкой для любого пользователя. Пользователь может создавать, читать, изменять и удалять свои задачи. 


### Как запустить в ручном режиме
Скачать файл на сервер 
```
https://github.com/FULLLIFE4rever/foodgram-project-react/blob/master/infra/docker-compose.yml
```

Создать файл .env в папке с этим файлом

Пример:
```
MYSQL_USER=mysql
MYSQL_PASS=mysql
MYSQL_ADR=localhost
MYSQL_PORT=3306
MYSQL_DBNAME=mysql

SQLALCHEMY_DRIVER=pymysql
SQLALCHEMY_DATABASE=mysql

FLASK_DEBUG=False
FLASK_ENV=development
FLASK_SECRET_KEY=3ddb4672-49b8-477b-8c04-77ca630fac12

FLASK_SQLALCHEMY_DATABASE_URI = ${SQLALCHEMY_DATABASE}+${SQLALCHEMY_DRIVER}://${MYSQL_USER}:${MYSQL_PASS}@${MYSQL_ADR}:${MYSQL_PORT}/${MYSQL_DBNAME}
FLASK_SQLALCHEMY_TRACK_MODIFICATIONS=False
```

Запустить
```
pip install -r requirements.txt
flask create-db
flask run
```




# Примеры запросов

**GET**: http://127.0.0.1:8000/tasks/  
Пример ответа:
```json
{
    "tasks": [
        {
            "created_at": "Tue, 28 May 2024 09:16:35 GMT",
            "description": "description",
            "id": 1,
            "title": "title",
            "updated_at": "Wed, 29 May 2024 13:07:57 GMT"
        }
    ]
}
```

**POST**: http://127.0.0.1:8000/tasks/  
Тело запроса:
```json
{
    "title": "title1",
    "description": "Can be None"
}
```
Пример ответа:
```json
    {
        "created_at": "Tue, 28 May 2024 09:16:35 GMT",
        "description": "Can be None",
        "id": 2,
        "title": "title1",
        "updated_at": "Tue, 28 May 2024 09:16:35 GMT"
    }
```

**GET**: http://127.0.0.1:8000/tasks/2 
Пример ответа:
```json
    {
        "created_at": "Tue, 28 May 2024 09:16:35 GMT",
        "description": "Can be None",
        "id": 2,
        "title": "title1",
        "updated_at": "Tue, 28 May 2024 09:16:35 GMT"
    }
```

**PUT**: http://127.0.0.1:8000/tasks/2
Тело запроса:
```json
{
    "title": "New title",
    "description": "New description"
}
``` 
Пример ответа:
```json
    {
        "created_at": "Tue, 28 May 2024 09:16:35 GMT",
        "description": "New description",
        "id": 2,
        "title": "New title",
        "updated_at": "Wed, 29 May 2024 13:07:57 GMT"
    }
```

### Автор
Александр Зубарев