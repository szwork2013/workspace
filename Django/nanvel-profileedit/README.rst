Profile edit example (Django + AngularJS)
=========================================

Used:

    - Django 1.5
    - Django Rest Framework
    - AngularJS 1.2.13
    - Pure css

Project init:

.. code-block:: bash

    git clone git@bitbucket.org:nanvel/profileedit.git
    cd profileedit
    virtualenv .env --no-site-packages
    source .env/bin/activate
    pip install -r requirements.txt
    python manage.py syncdb --noinput
    python manage.py migrate
    # add user using django shell
    make shell
    # from django.contrib.auth.models import User
    # user = User.objects.create_user(username='user', password='user', email='user@mail.com')
    # user.is_superuser = True
    # user.save()
    # exit()
    make run
    firefox http://127.0.0.1:8000
