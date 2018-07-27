from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver

import time

from functional_tests.base import FunctionalTest

class NewMarketTest(FunctionalTest):

    def test_can_start_market_and_enter_details(self):
        self.initiateDatabase()
        # Edith has heard about a cool new online free bets app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She sees a create market button and clicks it
        self.browser.find_element_by_name('new_market').click()
        
        # She notices the page title and header mention a market
        self.assertIn('Market', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('Market', header_text)

        # There is a select box titled 'Bookie'
        # There are several options
        bookie_select = self.getSelectBox(self.browser.find_element_by_id('bookie'))

        # Edith changes the bookie and the option updates
        self.changeSelectBox(bookie_select, 'aff2')

        # There is a select box titled 'bet type'
        # There are two options
        bet_type_select = self.getSelectBox(self.browser.find_element_by_id('bet_type'))

        # Edith changes the bet type to 'free bet' and the option updates
        self.changeSelectBox(bet_type_select, 'free')
        
        # There is an input box titled 'bet stake'
        # Edith enters a value and it updates
        stake = self.browser.find_element_by_id('stake')
        stake.find_element_by_class_name('input').clear()
        stake.find_element_by_class_name('input').send_keys('10')

        # There is a dropdown for number of market items
        # Edith selects the number and the option updates
        runners_select = self.getSelectBox(self.browser.find_element_by_id('runners'))
        self.changeSelectBox(runners_select, '10')
        
        # She notices a list of market items appears
        # and has the same number of items as selected
        market_list = self.browser.find_element_by_id('market')
        items = market_list.find_elements_by_tag_name("li")
        self.assertEqual(
            len(items),
            10
        )

        # Edith notices an input box for the bookie odds for the first runner. She enters a decimal

        # She sees there are input boxes for the lay price of each runner
        # As she is typing, the page updates, and the profit/loss value updates.
        
        # This does not effect the other runners

        # Edith enters the odds for the second runner and it updates the P/L value

        # The runner with the highest P/L is highlighted
        
        # Edith goes to sleep, delighted     

       

