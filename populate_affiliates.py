import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'free_bets_project.settings')

import django
django.setup()

from datetime import datetime

from bets.models import Affiliate

def populate():
    affiliate = [
        {"name": "Bet365"} ]

    for a in affiliate:
        p = add_aff(a["name"])
        print("- " + str(p.name))

def add_aff(name):
    p = Affiliate.objects.get_or_create(name=name)[0]
    return p

if __name__ == '__main__':
    print('Starting population script...')
    populate()
