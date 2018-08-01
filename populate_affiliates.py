import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'free_bets_project.settings')

import django
django.setup()

from datetime import datetime

from bets.models import Affiliate

def populate():
    affiliate = [
        {"name": "Bet365", 'url': 'https://example.com/', 'freebet': '10'},
        {"name": "Victor Chandler", 'url': 'https://example.com/', 'freebet': '50'},
        {"name": "Ladbrokes", 'url': 'https://example.com/', 'freebet': '15'},
        {"name": "Coral", 'url': 'https://example.com/', 'freebet': '25'},
        {"name": "Betfred", 'url': 'https://example.com/', 'freebet': '5'},
        {"name": "Sportsbet", 'url': 'https://example.com/', 'freebet': '100'}]

    for a in affiliate:
        p = add_aff(a["name"], a["url"], a["freebet"])
        print("- " + str(p.name))

def add_aff(name, url, freebet):
    p = Affiliate.objects.get_or_create(name=name, url=url, freebet=freebet)[0]
    return p

if __name__ == '__main__':
    print('Starting population script...')
    populate()
