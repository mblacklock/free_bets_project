from django.test import TestCase

from django.contrib.auth import get_user_model
User = get_user_model()

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

    def test_action_redirects_to_affiliate_when_signup_or_deposit(self):
        aff1 = Affiliate.objects.create(name='Aff1', url='https://example.com/')
        aff2 = Affiliate.objects.create(name='Aff2')
        self.client.post('/summary/create_new')
        item = Item.objects.first()

        response = self.client.post(f'/summary/action/{item.id}', {'action' : 'signup'})
    
        self.assertRedirects(response, aff1.url, fetch_redirect_response=False)

    def test_summary_owner_is_saved_if_user_is_authenticated(self):
        user = User.objects.create(email='a@b.com')
        self.client.force_login(user)  
        self.client.post('/summary/create_new')
        summary = Summary.objects.first()
        self.assertEqual(summary.owner, user)        

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

    def test_update_banked_updates_db(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
        self.client.post('/summary/create_new')
        summary = Summary.objects.first()
   
        self.client.get(f'/summary/update/banked', {'summary_id': summary.id, 'affiliate_name': 'Aff1', 'value': True})
        
        self.assertEqual(Item.objects.get(affiliate=aff1).banked, True)

    def test_update_summary_name_updates_summary_name(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
        self.client.post('/summary/create_new')
        summary = Summary.objects.first()
   
        self.client.get(f'/summary/update/summary_name', {'summary_id': summary.id, 'affiliate_name': 'summary_name', 'value': 'test'})
        
        self.assertEqual(Summary.objects.first().name, 'test')

class MyListsTest(TestCase):

    def test_my_lists_url_renders_my_lists_template(self):
        User.objects.create(email='a@b.com')
        response = self.client.get('/summary/users/a@b.com/')
        self.assertTemplateUsed(response, 'bets/my_summaries.html')

    def test_passes_correct_owner_to_template(self):
        User.objects.create(email='wrong@owner.com')
        correct_user = User.objects.create(email='a@b.com')
        response = self.client.get('/summary/users/a@b.com/')
        self.assertEqual(response.context['owner'], correct_user)
