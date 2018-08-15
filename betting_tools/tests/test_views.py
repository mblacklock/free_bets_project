from django.test import TestCase

# Create your tests here.

class OddsConverterPageTest(TestCase):

    def test_uses_converter_template(self):
        response = self.client.get('/betting_tools/odds_converter/')
        self.assertTemplateUsed(response, 'betting_tools/converter.html')
