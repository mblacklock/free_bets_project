import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = 'git@github.com:mblacklock/free_bets_project.git'  

def deploy():
    if 'mblacklock' in env.host:
        dev = True
        virtualenv = 'free-bets-project-dev'
    else:
        dev = False
        virtualenv = 'free-bets-project-prod'
    _update_virtualenv(dev, virtualenv)
    run(f'workon '+virtualenv)
    
    site_folder = f'/home/{env.user}/{env.host}'
    run(f'mkdir -p {site_folder}')  
    with cd(site_folder):  
        _get_latest_source()
        _create_or_update_dotenv()
        #_update_static_files()
        _update_database()

def _get_latest_source():
    if exists('.git'):  
        run('git fetch')  
    else:
        run(f'git clone {REPO_URL} .')  
    current_commit = local("git log -n 1 --format=%H", capture=True)  
    run(f'git reset --hard {current_commit}')

def _update_virtualenv(dev, virtualenv):
    if not exists('.virtualenv/'+virtualenv+'/bin/pip'):  
        run(f'mkvirtualenv '+virtualenv+' --python=/usr/bin/python3.6')
    run('.virtualenv/'+virtualenv+'/bin/pip install -r requirements.txt') 

def _create_or_update_dotenv():
    append('.env', 'DJANGO_DEBUG_FALSE=y')  
    append('.env', f'SITENAME={env.host}')
    current_contents = run('cat .env')  
    if 'DJANGO_SECRET_KEY' not in current_contents:  
        new_secret = ''.join(random.SystemRandom().choices(  
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', f'DJANGO_SECRET_KEY={new_secret}')

def _update_database():
    run('python manage.py migrate --noinput')
