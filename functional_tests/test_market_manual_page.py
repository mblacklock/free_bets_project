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
        
        # There is an input box titled 'bet stake'
        # Edith enters a value and it updates
        stake = self.browser.find_element_by_id('stake')
        self.enterInput(stake, '10', False)

        # There is a dropdown for number of market items
        # Edith selects the number and the option updates
        runners_select = self.getSelectBox(self.browser.find_element_by_id('runners'))
        self.changeSelectBox(runners_select, '10')
        
        # She notices a list of market items appears
        # and has the same number of items as selected
        market_list = self.browser.find_element_by_id('market')
        items = market_list.find_elements_by_tag_name("li.runner")
        self.assertEqual(
            len(items),
            10
        )

        # Edith notices an input box for the bookie odds for the first runner. She enters a decimal
        runner = market_list.find_element_by_id('runner-1')
        bookie_odds = runner.find_element_by_class_name('bookie_odds')
        self.enterInput(bookie_odds, '10.05', False)

        # Oops, an error is thrown about a missing bet type
        self.assertEqual(
            self.browser.find_element_by_class_name('type-error').is_displayed(),
            True
        )
        
        # There is a select box titled 'bet type'
        # There are two options
        bet_type_select = self.getSelectBox(self.browser.find_element_by_id('bet_type'))

        # Edith changes the bet type to 'initial bet' and the option updates
        self.changeSelectBox(bet_type_select, 'initial')

        # The error disappears
        self.assertEqual(
            self.browser.find_element_by_class_name('type-error').is_displayed(),
            False
        )
        
        # She sees there are input boxes for the lay price of each runner
        # As she is typing, the page updates, and the lay stake and profit/loss values updates.
        lay_odds = runner.find_element_by_class_name('lay_odds')
        self.enterInput(lay_odds, '10.00', False)
        self.checkRunnerValues(runner, '10.10', '-0.40')
        
        # This does not effect the other runners
        runner = market_list.find_element_by_id('runner-2')
        self.checkRunnerValues(runner, 'NaN', 'NaN')

        # Edith changes the bet type to 'free bet' and the option updates
        self.changeSelectBox(bet_type_select, 'free')

        # The lay_stake and profit_loss values update
        runner = market_list.find_element_by_id('runner-1')
        self.checkRunnerValues(runner, '9.10', '8.64')

        # Edith enters the odds for the second runner and it updates the P/L value
        runner = market_list.find_element_by_id('runner-2')
        bookie_odds = runner.find_element_by_class_name('bookie_odds')
        self.enterInput(bookie_odds, '12.5', False)
        lay_odds = runner.find_element_by_class_name('lay_odds')
        self.enterInput(lay_odds, '13', False)

        self.checkRunnerValues(runner, '8.88', '8.44')

        # The runner with the highest P/L is highlighted
        highlighted = self.browser.find_element_by_class_name('list-group-item-success').find_element_by_class_name('profit_loss')
        self.assertEqual(highlighted.text, '8.64')
        
        # Edith goes to sleep, delighted     

       

