# E-Kart

This is a E-Commerce website created using Django

## Installation

Clone the repository and create a virtual environment.

```bash
git clone https://github.com/sudeepsudhevan/E-kart.git
cd E-kart
python -m venv env
source env/Scripts/activate
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

  `SECRET_KEY = "your_secret_key"`

  We can find your secret key in settings.py

- In settings.py add the following line

  `from decouple import config`

  `SECRET_KEY = config('SECRET_KEY')`

For further information and alternatives of python-decouple check on my gist.

[How to Create Environment Variable](https://gist.github.com/sudeepsudhevan/4ed6a287ef9ba51c97cd5d6eebf14008)

## To Generate Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## To Add static file

Add the static folder to the settings.py

```bash
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

## To Add media file

Add the media folder to the settings.py

```bash
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```

Add the following line to the urls.py

```bash
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
