FROM python:3.8.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
    
RUN pip install --upgrade pip

RUN mkdir /app

COPY ./ecommerce/requirements.txt .

RUN pip install -r requirements.txt

COPY ./ecommerce /app

WORKDIR /app

COPY ./entrypoint.sh /

ENTRYPOINT [ "sh", "/entrypoint.sh" ]