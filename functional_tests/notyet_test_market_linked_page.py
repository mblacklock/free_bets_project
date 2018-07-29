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


       

