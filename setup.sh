#!/bin/bash

echo "--- Instalando dependências ---"
pip install -r requirements.txt

echo "--- Preparando o Banco de Dados ---"
# O migrate vem primeiro para garantir que as tabelas existam
python manage.py migrate

# O flush é opcional aqui, mas se quiser garantir que o banco esteja limpo antes das seeds:
echo "--- Limpando dados residuais ---"
python manage.py flush --no-input

echo "--- Populando banco de dados (Seeds) ---"
python manage.py seed_all

echo "--- Iniciando o servidor ---"
python manage.py runserver