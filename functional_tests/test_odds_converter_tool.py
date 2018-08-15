from .base import FunctionalTest

import time


class OddsConverterTest(FunctionalTest):

     def test_odds_converter_converts(self):
          # Edith visits the blog and clicks on the odds converter tool
          self.browser.get(self.live_server_url+'/market/market_manual/')
          self.browser.find_element_by_class_name('dropdown-toggle').click()
          self.browser.find_element_by_class_name('odds_converter').click()

          # She types in a fractional odd and the decimal and percentage update
          fraction = self.browser.find_element_by_class_name('fraction')
          decimal = self.browser.find_element_by_class_name('decimal')
          percent = self.browser.find_element_by_class_name('percent')

          fraction.clear()
          fraction.send_keys('4/1')
          self.assertEqual(
             decimal.get_attribute("value"),
             '5'
          )
          self.assertEqual(
             percent.get_attribute("value"),
             '20'
          )

          # She then types in a non-fractional by mistake. The others are blank
          fraction.clear()
          fraction.send_keys('5')
          self.assertEqual(
             decimal.get_attribute("value"),
             ''
          )
          self.assertEqual(
             percent.get_attribute("value"),
             ''
          )

          # She types in a decimal, the others update
          decimal.clear()
          decimal.send_keys('7')
          self.assertEqual(
             fraction.get_attribute("value"),
             '6/1'
          )
          self.assertEqual(
             percent.get_attribute("value"),
             '14.3'
          )
        
          # She types in a percentage, the others update
          percent.clear()
          percent.send_keys('25')
          self.assertEqual(
             fraction.get_attribute("value"),
             '3/1'
          )
          self.assertEqual(
             decimal.get_attribute("value"),
             '4'
          )
        
          # Cool, she goes to sleep.
