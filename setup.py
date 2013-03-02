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
      'HTMLParser',
    ],
    'packages':["django", "demosite", "fields", "transformations", "celery",],
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