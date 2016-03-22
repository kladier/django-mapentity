import os

DIRNAME = os.path.dirname(__file__)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'paperclip',
    'leaflet',
    'djgeojson',
    'compressor',
    'easy_thumbnails',
    'crispy_forms',
    'floppyforms',
    'rest_framework',
    'embed_video',
    'mapentity',
    'demomapentity'
)

DATABASES={
    'default': {
        'ENGINE':  'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(DIRNAME, 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

SECRET_KEY = 'MMMMMMMMMMMMMMMMMMMMMMMMM'


STATIC_ROOT = '.'
STATIC_URL = '/static/'
ROOT_URLCONF = 'demoapp.urls'
MEDIA_URL = '/media/'
MEDIA_URL_SECURE = '/media_secure/'
MEDIA_ROOT = '/tmp/'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'mapentity.middleware.AutoLoginMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS=(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "mapentity.context_processors.settings",
)

SRID = 3857
COMPRESS_ENABLED = False
TEST = True
