# E-Kart

This is a E-Commerce website created using Django

## Installation

Clone the repository and create a virtual environment.

```bash
git clone https://github.com/sudeepsudhevan/E-kart.git
cd E-kart
python -m venv env
source env/bin/activate
```

## Installing dependencies

```bash
pip install -r requirements.txt
```

## Running the server

```bash
python manage.py runserver
```

## Create .env file and use python decouple to store the secret key

```bash
pip install python-decouple
```

- Create a .env file in the root directory

```bash
touch .env
```

- Then add the following line to the.env file
  `SECRET_KEY = "your_secret_key"` in the settings.py

- In settings.py add the following line
  `from decouple import config`

  `SECRET_KEY = config('SECRET_KEY')`
