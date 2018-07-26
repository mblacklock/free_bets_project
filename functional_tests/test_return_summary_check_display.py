from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver

import time

from functional_tests.base import FunctionalTest

class ReturnVisitorAccountSummaryTest(FunctionalTest):

    def test_return_to_summary_looks_right(self):
        self.initiateDatabase()
        # Edith creates a summary page
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('new_summary').click()
        edith_list_url = self.browser.current_url
        
        name = self.browser.find_element_by_id('summary_name')
        self.enterInput(name, "Edith's Summary")

        row = self.findRow('1')
        el = row.find_element_by_id('username')
        self.enterInput(el, 'edith66')        
        self.changeSelectInRow(row, 'initial')
        el = row.find_element_by_id('balance')
        self.enterInput(el, '20.57')
        el = row.find_element_by_id('profit')
        self.enterInput(el, '-12.90')
        self.clickBanked(row)
        row = self.findRow('2')
        el = row.find_element_by_id('username')
        self.enterInput(el, 'bombedith23')
        el = row.find_element_by_id('balance')
        self.enterInput(el, '6.27')

        # She closes the browser then returns to the page
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(edith_list_url)

        # The summary name input is disabled but the edit button is enabled
        name = self.browser.find_element_by_id('summary_name')
        self.checkIsEnabled(name, 'input', False)
        self.checkIsDisplayed(name, 'edit', True)

        # the first row is disabled
        row = self.findRow('1')
        self.checkElemsAreEnabled(row, 'input', False)
        self.checkElemsAreEnabled(row, 'edit', False)
        self.checkElemsAreEnabled(row, 'status', False)
        
        # the second row is  not
        row = self.findRow('2')
        self.checkElemsAreEnabled(row, 'edit', True)
        self.checkElemsAreEnabled(row, 'status', True)
        
        # In the second row, the username and balance boxes are disabled. The profit is not.
        row = self.findRow('2')
        el = row.find_element_by_id('username')        
        self.checkElemsAreEnabled(el, 'input', False)
        self.checkIsDisplayed(el, 'edit', True)

        el = row.find_element_by_id('balance')        
        self.checkElemsAreEnabled(el, 'input', False)
        self.checkIsDisplayed(el, 'edit', True)

        el = row.find_element_by_id('profit')        
        self.checkElemsAreEnabled(el, 'input', True)
        self.checkIsDisplayed(el, 'edit', False)

        
