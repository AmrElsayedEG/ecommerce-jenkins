#!/bin/sh
gunicorn ecommerce_backend.wsgi:application --bind=0.0.0.0:8000