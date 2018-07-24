import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'free_bets_project.settings')

import django
django.setup()

from datetime import datetime

from bets.models import Affiliate

def populate():
    affiliate = [
        {"name": "Bet365", 'url': 'http://www.bet365.com', 'freebet': '10'},
        {"name": "Victor Chandler", 'url': 'http://www.vcbet.com', 'freebet': '50'},
        {"name": "Ladbrokes", 'url': 'http://www.ladbrokes.com', 'freebet': '15'},
        {"name": "Coral", 'url': 'http://www.coral.com', 'freebet': '25'},
        {"name": "Betfred", 'url': 'http://www.betfred.com', 'freebet': '5'},
        {"name": "Sportsbet", 'url': 'http://www.sportsbet.com', 'freebet': '100'}]

    for a in affiliate:
        p = add_aff(a["name"])
        print("- " + str(p.name))

def add_aff(name):
    p = Affiliate.objects.get_or_create(name=name)[0]
    return p

if __name__ == '__main__':
    print('Starting population script...')
    populate()
