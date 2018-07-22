from django.test import TestCase

from bets.models import Affiliate, Item, Summary

# Create your tests here.

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class ExistingSummaryPageTest(TestCase):

    def test_uses_existing_summary_template(self):
        summary = Summary.objects.create()
        response = self.client.get(f'/summary/{summary.id}/')
        self.assertTemplateUsed(response, 'bets/summary.html')


class NewSummaryViewIntegratedTest(TestCase):
    
    def test_can_save_a_POST_request(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
        
        self.client.post('/summary/create_new')
        
        self.assertEqual(Item.objects.count(), 2)
        new_item = Item.objects.first()
        self.assertEqual(new_item.affiliate, aff1)

class AjaxViewsTests(TestCase):

    def test_update_username_updates_username(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
        self.client.post('/summary/create_new')
        summary = Summary.objects.first()
   
        self.client.get(f'/summary/update/username', {'summary_id': summary.id, 'affiliate_name': 'Aff1', 'value': 'test'})
        
        self.assertEqual(Item.objects.get(affiliate=aff1).username, 'test')

    def test_update_status_updates_status(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
        self.client.post('/summary/create_new')
        summary = Summary.objects.first()
   
        self.client.get(f'/summary/update/status', {'summary_id': summary.id, 'affiliate_name': 'Aff1', 'value': 'free'})
        
        self.assertEqual(Item.objects.get(affiliate=aff1).status, 'free')

