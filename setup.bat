@echo off
echo --- [1/4] Instalando dependencias ---
pip install -r requirements.txt

echo --- [2/4] Aplicando migrations ---
python manage.py migrate

echo --- [3/4] Populando banco de dados (Seeds) ---
python manage.py seed_all

echo --- [4/4] Iniciando servidor ---
python manage.py runserver

pause