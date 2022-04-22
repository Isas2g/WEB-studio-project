FROM python:3.10.2-bullseye


WORKDIR /server

COPY  requirements.txt .

RUN pip install -r requirements.txt
COPY . .

RUN python manage.py makemigrations users
RUN python manage.py makemigrations board
RUN python manage.py makemigrations projects
