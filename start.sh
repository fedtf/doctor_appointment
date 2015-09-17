apt-get install python3
apt-get install python3-pip

pip3 install virtualenv
mkdir ~/Envs2
virtualenv -p python3 ~/Envs2/doctor_appointment

~/Envs2/doctor_appointment/bin/pip install -r requirements.txt

~/Envs2/doctor_appointment/bin/python manage.py makemigrations
~/Envs2/doctor_appointment/bin/python manage.py migrate

~/Envs2/doctor_appointment/bin/python manage.py runserver 0.0.0.0:80
