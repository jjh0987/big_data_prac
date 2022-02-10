source tensorflow_macos_venv/bin/activate

cd desktop/main/mySite/Investar#

make app : python manage.py startapp <appName>
python manage.py migrate

python manage.py runserver

http://localhost:8000
admin,index