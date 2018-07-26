from django.test import TestCase

# Create your tests here.

from bets.models import Affiliate

class NewMarketViewIntegratedTest(TestCase):
    
    def test_can_save_a_POST_request(self):     
        response = self.client.post('/market/create_new', follow=True)    
        self.assertTemplateUsed(response, 'market/market.html')

class ManualMarketTest(TestCase):

    def test_affiliate_list_is_sent_to_template(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
        
        response = self.client.get('/market/market_manual/')
        
        self.assertContains(response, 'value="aff2"')

