import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

SECRET_KEY = 'CanIHazS3cret?Meis1337'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'get_data',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'managementapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'managementapp.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'us-cdbr-iron-east-04.cleardb.net',
        'USER': 'bfcd4b322c6a83',
        'NAME': 'heroku_bf0d9aa88fd9c5b',
        'PASSWORD': 'beddbea6',
        'OPTIONS': {'ssl': {'ca':'cleardb-ca.pem', 'cert':'bfcd4b322c6a83-cert.pem', 'key':'cleardb_id-key.pem'},},
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': '/opt/lampp/var/mysql/mysql.sock',
#         'USER': 'root',
#         'NAME': 'project1',
#         'PASSWORD': '',
#         'PORT': '7777',
#     }
# }



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# if os.environ.get('DATABASE_URL', None):
#     import dj_database_url
#     DATABASES['default'] = dj_database_url.config()


# DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True