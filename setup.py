from setuptools import setup
import py2app
import os

def add_path_tree( base_path, path, skip_dirs=[ '.svn', '.git' ]):
  path = os.path.join( base_path, path )
  partial_data_files = []
  for root, dirs, files in os.walk( os.path.join( path )):
    sample_list = []
    for skip_dir in skip_dirs:
      if skip_dir in dirs:
        dirs.remove( skip_dir )
    if files:
      for filename in files:
        sample_list.append( os.path.join( root, filename ))
    if sample_list:
      partial_data_files.append((
        root.replace(
          base_path + os.sep if base_path else '',
          '',
          1
        ),
        sample_list
      ))
  return partial_data_files



APP = ['demosite.py']
DATA_FILES = ['static']
OPTIONS = {'argv_emulation': True, 'packages':["django"]}

py2app_options = {
    'includes': [
      ########
      # demosite imports
      'demosite.settings',
      'fields.models',
      'fields.views',
      #fields.urls
      'transformations.models',
      'transformations.views',
      #transformations.urls
      'demosite.audit',
      'demosite.urls',
      'manage',
      'demosite.settings',
      'demosite.views',
      'celery',
      ########
      # mass django import
      'django.views.generic.list_detail',
      'django.template.loaders.filesystem',
      'django.template.loaders.app_directories',
      'django.middleware.common',
      'django.contrib.sessions.middleware',
      'django.contrib.auth.middleware',
      'django.middleware.common.CommonMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.middleware.doc.XViewMiddleware',
      'django.middleware.doc',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.sessions.backends.db',
      'django.contrib.sites',
      'django.contrib.admin',
      'django.core.cache.backends',
      'django.db.backends.sqlite3.base',
      'django.db.backends.sqlite3.introspection',
      'django.db.backends.sqlite3.creation',
      'django.db.backends.sqlite3.client',
      'django.template.defaulttags',
      'django.template.defaultfilters',
      'django.template.loader_tags',
      'django.contrib.admin.urls',
      'django.contrib.staticfiles',
      'django.conf.urls.defaults',
      'django.contrib.admin.views.main',
      'django.core.context_processors',
      'django.contrib.auth.views',
      'django.contrib.auth.backends',
      'django.views.static',
      'django.contrib.admin.templatetags.adminmedia',
      'django.contrib.admin.templatetags.adminapplist',
      'django.contrib.admin.templatetags.admin_list',
      'django.contrib.admin.templatetags.admin_modify',
      'django.contrib.admin.templatetags.log',
      'django.contrib.admin.views.auth',
      'django.contrib.admin.views.doc',
      'django.contrib.admin.views.template',
      'django.conf.urls.shortcut',
      'django.views.defaults',
      'django.core.cache.backends.locmem',
      'django.templatetags.i18n',
      'django.views.i18n',
      'django.core.handlers.wsgi',
      'django.template.loaders.filesystem.load_template_source',
      'django.template.loaders.app_directories.load_template_source',
      ########
      # also used by django?
      'email.mime.audio',
      'email.mime.base',
      'email.mime.image',
      'email.mime.message',
      'email.mime.multipart',
      'email.mime.nonmultipart',
      'email.mime.text',
      'email.charset',
      'email.encoders',
      'email.errors',
      'email.feedparser',
      'email.generator',
      'email.header',
      'email.iterators',
      'email.message',
      'email.parser',
      'email.utils',
      'email.base64mime',
      'email.quoprimime',
      'htmlentitydefs',
      'html5lib',
      'HTMLParser',
    ],
    'packages':["django",],
}

# Take the first value from the environment variable PYTHON_PATH
python_path = os.environ[ 'PYTHONPATH' ].split( ';' )[ 0 ]

django_admin_path = os.path.normpath( python_path + '/lib/site-packages/django/contrib/admin' )
py2app_data_files = []

# django admin files
py2app_data_files += add_path_tree( django_admin_path, 'templates' )
py2app_data_files += add_path_tree( django_admin_path, 'static' )
# project files
py2app_data_files += add_path_tree( '', 'db' )
py2app_data_files += add_path_tree( '', 'templates' )
py2app_data_files += add_path_tree( '', 'static' )

setup(
    app=APP,
    data_files=py2app_data_files,
    options={'py2app': py2app_options},
    setup_requires=['py2app'],
)