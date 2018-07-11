from django.test import TestCase

# Create your tests here.

class SummaryPageTest(TestCase):

    def test_uses_summary_template(self):
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'bets/summary.html')

    def test_uses_summary_template2(self):
        response = self.client.get('/summary/') 
        self.assertTemplateUsed(response, 'bets/summary.html')
