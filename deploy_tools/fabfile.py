import os
import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

from dotenv import read_dotenv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPO_URL = 'https://github.com/mblacklock/free_bets_project.git'

def deploy(VERSION):
    if VERSION == 'dev':
        print('Deploying development site...')
        SITENAME = 'mblacklock.pythonanywhere.com'
        WSGI_FILE = 'mblacklock_pythonanywhere_com_wsgi.py'
    elif VERSION == 'prod':
        print('Deploying production site...')
        SITENAME = 'mblacklock.pythonanywhere.com'
        WSGI_FILE = 'mblacklock_pythonanywhere_com_wsgi.py'
        
    read_dotenv(os.path.join(BASE_DIR, '.env'))
    
    virtualenv = 'free-bets-project-' + VERSION
    virtualenv_path = '/home/mblacklock/.virtualenvs/' + virtualenv
    site_folder = f'/home/mblacklock/free_bets_project_' + VERSION + '/'
    
    run(f'mkdir -p {site_folder}')  
    with cd(site_folder):  
        _get_latest_source()
        _update_virtualenv(virtualenv, virtualenv_path)
        _create_or_update_dotenv(SITENAME)
        #_update_static_files()
        _update_database(virtualenv, virtualenv_path)
    run(f'touch /var/www/' + WSGI_FILE)

def _get_latest_source():
    if exists('.git'):  
        run('git fetch')  
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)  
    run(f'git reset --hard {current_commit}')
    run('git checkout blog_only')

def _update_virtualenv(virtualenv, virtualenv_path):
    if not exists(virtualenv_path + '/bin/pip'):  
        run(f'mkvirtualenv '+virtualenv+' --python=/usr/bin/python3.6')
    run(virtualenv_path + '/bin/pip install -r requirements.txt') 

def _create_or_update_dotenv(SITENAME):
    append('.env', 'DJANGO_DEBUG_FALSE=Y')  
    append('.env', 'SITENAME=' + SITENAME)
    append('.env', 'EMAIL_PASSWORD=' + os.environ['EMAIL_PASSWORD'])  
    current_contents = run('cat .env')  
    if 'DJANGO_SECRET_KEY' not in current_contents:  
        new_secret = ''.join(random.SystemRandom().choices(  
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_database(virtualenv, virtualenv_path):
    run(virtualenv_path + '/bin/python manage.py migrate --noinput')
