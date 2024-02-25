#!/usr/bin/env bash

mkvirtualenv django50 --python=/usr/bin/python3.10 && echo "workon django50" >> ~/.bashrc && pip install -r requirements.txt

cd ~ && git clone https://github.com/csev/dj4e-samples samples && cd ~/samples && pip install -r requirements42.txt

python manage.py check && python manage.py makemigrations && python manage.py migrate
    
