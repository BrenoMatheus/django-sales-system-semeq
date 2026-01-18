#!/bin/bash

echo " Resetando banco..."
python manage.py flush --no-input

echo " Aplicando migrations..."
python manage.py migrate

echo " Rodando seeds..."
python manage.py seed_all

echo " Iniciando servidor..."
python manage.py runserver
