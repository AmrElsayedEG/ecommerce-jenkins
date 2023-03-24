## Ecommerce [Web Dashboard + API's for Mobile Apps] ![Django](https://img.shields.io/badge/Django-yellow.svg) ![Rest API](https://img.shields.io/badge/RestFul%20API-yellow.svg) ![Celery](https://img.shields.io/badge/celery-green.svg)


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
* Celery
* Redis Image
* And other important tools listed in requirements.txt file
	
## Run
To run this project using the regular runserver statement follow these steps:

```
$ pip install requirements.txt
$ python manage.py runserver
```

Make sure to run the test cases in cause any feature will be added to maintain the system processes
```
$ python manage.py test
```

To run it using Docker follow these steps (Port 80):

```
$ docker-compose up --build -d
```

You also can run this project using Jenkins and it will run on port 80

To run the test cases using Docker:

```
$ docker-compose -f docker-compose-test.yml build test
$ docker-compose -f docker-compose-test.yml run test
```
