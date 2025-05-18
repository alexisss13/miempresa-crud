import os
import dj_database_url
from pathlib import Path

# ——————————————————————————————————————————————————————————————
# BASE_DIR
# ——————————————————————————————————————————————————————————————
BASE_DIR = Path(__file__).resolve().parent.parent

# ——————————————————————————————————————————————————————————————
# SECRET_KEY & DEBUG — desde variables de entorno en prod
# ——————————————————————————————————————————————————————————————
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-wah^pg@ra_=xalnkns4_fbz*_=i6a0#@-e6#hcn6w(w#qeo=)@'  # valor por defecto para dev
)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']  # en prod puedes restringir dominios

# ——————————————————————————————————————————————————————————————
# INSTALLED_APPS
# ——————————————————————————————————————————————————————————————
INSTALLED_APPS = [
    'gestion',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# ——————————————————————————————————————————————————————————————
# MIDDLEWARE (inserta WhiteNoise justo después de Security)
# ——————————————————————————————————————————————————————————————
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',            # ← sirve estáticos en prod
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ——————————————————————————————————————————————————————————————
# URL CONF & TEMPLATES
# ——————————————————————————————————————————————————————————————
ROOT_URLCONF = 'miempresa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],            # si quisieras templates globales agregar BASE_DIR/'templates'
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'miempresa.wsgi.application'

# ——————————————————————————————————————————————————————————————
# BASE DE DATOS (MySQL local o DATABASE_URL en prod)
# ——————————————————————————————————————————————————————————————
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=False
    )
}

# ——————————————————————————————————————————————————————————————
# VALIDADORES DE CONTRASEÑA
# ——————————————————————————————————————————————————————————————
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ——————————————————————————————————————————————————————————————
# I18N / TIMEZONE
# ——————————————————————————————————————————————————————————————
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ——————————————————————————————————————————————————————————————
# ESTÁTICOS / MÉDIA
# ——————————————————————————————————————————————————————————————
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'   # donde collectstatic deja los archivos en prod
STATICFILES_DIRS = [ BASE_DIR / 'static' ]  # para desarrollo local

# WhiteNoise storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ——————————————————————————————————————————————————————————————
# DEFAULT AUTO FIELD
# ——————————————————————————————————————————————————————————————
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
