# Apnea
Log book for freedive training

Installation
------------

### Prerequisites

[Python 2.7.*](https://docs.python.org/2/install/)

[pip](http://pip.readthedocs.org/en/latest/installing.html)

[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

### Steps

    git clone -b develop https://github.com/GotlingSystem/apnea.git
    cd apnea
    mkvirtualenv apnea
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser


Run
--------

    ./manage.py runserver
