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
