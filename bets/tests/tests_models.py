from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

from decimal import *

from bets.models import Affiliate, Click, Item, Summary

# Create your tests here.

class AffiliateAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        summary = Summary.objects.create()
        
        first_aff = Affiliate.objects.create(name = 'Bet365')       
        first_item = Item.objects.create(affiliate=first_aff, summary=summary)

        second_aff = Affiliate.objects.create(name = 'Fun88')
        second_item = Item.objects.create(affiliate=second_aff, summary=summary)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.affiliate, first_aff)
        self.assertEqual(second_saved_item.affiliate, second_aff)

    def test_item_is_related_to_summary(self):
        summary = Summary.objects.create()
        affiliate = Affiliate.objects.create(name = 'Bet365')
        
        item = Item(affiliate=affiliate, summary=summary)
        item.summary = summary
        item.save()
        self.assertIn(item, summary.item_set.all())

    def test_duplicate_items_are_invalid(self):
        summary = Summary.objects.create()
        affiliate = Affiliate.objects.create(name = 'Bet365')
        
        Item.objects.create(affiliate=affiliate, summary=summary)
        with self.assertRaises(ValidationError):
            item = Item(affiliate=affiliate, summary=summary)
            item.full_clean()
        
    def test_CAN_save_same_item_to_different_summaries(self):
        summary1 = Summary.objects.create()
        summary2 = Summary.objects.create() 
        affiliate = Affiliate()
        affiliate.name = 'Bet365'
        affiliate.save()
        
        Item.objects.create(affiliate=affiliate, summary=summary1)
        item = Item(affiliate=affiliate, summary=summary2)
        item.full_clean()  # should not raise

    def test_balance_cannot_be_negative(self):
        summary = Summary.objects.create()
        affiliate = Affiliate.objects.create(name = 'Bet365')
        
        with self.assertRaises(ValidationError):
            item = Item(affiliate=affiliate, summary=summary)
            item.balance = Decimal('-1.00')
            item.full_clean()

    def test_affiliate_slug_created(self):
        affiliate = Affiliate.objects.create(name = 'Random Affiliate Name')
        self.assertEqual(affiliate.slug, 'random-affiliate-name')

class SummaryModelTest(TestCase):

    def test_get_absolute_url(self):
        summary = Summary.objects.create()
        self.assertEqual(summary.get_absolute_url(), f'/summary/{summary.id}/')

    def test_create_new_creates_summary_with_all_affiliates_as_items(self):
        aff1 = Affiliate.objects.create(name = 'Aff1')
        aff2 = Affiliate.objects.create(name = 'Aff2')
        aff3 = Affiliate.objects.create(name = 'Aff3')
        
        Summary.create_new()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 3)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.affiliate, aff1)
        self.assertEqual(second_saved_item.affiliate, aff2)

    def test_summaries_can_have_owners(self):
        user = User.objects.create(email='a@b.com')
        summary = Summary.objects.create(owner=user)
        self.assertIn(summary, user.summary_set.all())

    def test_summary_owner_is_optional(self):
        Summary.objects.create()  # should not raise

class ClickModelTest(TestCase):
    
    def test_click_can_have_owners(self):
        aff1 = Affiliate.objects.create(name = 'Aff1')
        user = User.objects.create(email='a@b.com')
        click = Click.objects.create(affiliate=aff1, user=user)
        self.assertIn(click, user.click_set.all())

    def test_summary_owner_is_optional(self):
        aff1 = Affiliate.objects.create(name = 'Aff1')
        Click.objects.create(affiliate=aff1)  # should not raise
    
