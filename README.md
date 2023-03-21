## Ecommerce [Web Dashboard + API's for Mobile Apps] ![Django](https://img.shields.io/badge/Django-yellow.svg) ![Rest API](https://img.shields.io/badge/RestFul%20API-yellow.svg)


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Run](#run)

## General info
- This project is build using Django framework as a backend and Rest API for communication between the mobile app and the backend
- This project has a web dashboard to see all the statistics and orders and to send notifications as well
- You need to enter email stmp cred in order to send emails to customers

## Technologies
Project is created with:
* Django: 3.2
* Django Rest Framework: 3.12
* And other important tools listed in requirements.txt file
	
## Run
To run this project using the regular runserver statement follow these steps:

```
$ pip install requirements.txt
$ python manage.py runserver
```

To run it using Docker follow these steps (Port 80):

```
$ docker-compose up --build -d
```

You also can run this project using Jenkins and it will run on port 80
