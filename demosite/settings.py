import os
import yaml
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, PROJECT_ROOT)


# get settings from db/settings.yaml (if any missing all will default)
# this allows customising the database and web server details after deployment
config = {}
try:
  config_file = os.path.join( 'db', 'settings.yaml' )
  if os.path.exists( config_file ):
    config = yaml.load( file( config_file, 'r' ))
except:
  pass

def get_config( config_yaml, index, default='' ):
  try:
    return config_yaml[ index ]
  except:
    return default

DEBUG = get_config( config, 'debug', False )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "db/sentinel_db.sqlite",
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = get_config( config, 'time_zone', 'Australia/Melbourne' )
LANGUAGE_CODE = get_config( config, 'language_code', 'en-us' )

START_URL = get_config( config, 'start_url', 'http://localhost/admin/' )
WEB_SERVER_PORT = get_config( config, 'web_server_port', 80 )

ADMINS = (
# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'aaaaaasn%1aaaaaaaaaaaaeaagd%1aaaaaa6*(ef()aag$&f$%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'demosite.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
  'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'fields',
    'transformations',
)



PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
MEDIA_URL = '/site_media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip("/"))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
