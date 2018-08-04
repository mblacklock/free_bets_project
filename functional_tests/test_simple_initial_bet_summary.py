from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from unittest import skip

import time

from functional_tests.base import FunctionalTest

class NewVisitorAccountSummaryTest(FunctionalTest):

    def test_can_start_summary_for_single_user(self):
        self.initiateDatabase()
        # Edith has heard about a cool new online free bets app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention free bets
        self.assertIn('Free Bet', self.browser.title)

        # She sees a create account button and clicks it
        self.browser.find_element_by_class_name('new_summary').click()

        # She notices that her account summary has a unique URL
        self.assertRegex(self.browser.current_url, '/summary/.+')
        
        # She notices the header mentions an account summary
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('Summary', header_text)

        # Edith see that the newly created summary has an input box to enter a title
        # She enters a name and hits enter, it updates and is replaced by an edit button
        name = self.browser.find_element_by_id('summary_name')
        self.enterInput(name, "Edith's Summary")
        
        # She clicks edit and is able to change her summary name
        self.clickEdit(name, "Edith's Summary")
        self.enterInput(name, "Bombedith's Summary")
            
        # She notices a table of bookmakers
        table = self.browser.find_element_by_tag_name('table')
        self.assertEqual(
            table.get_attribute('name'),
            'bookie-summary'
        )

        # There is a next action button at the end that says sign up.
        row = self.findRow('1')
        el = row.find_element_by_class_name('action')
        self.assertEqual(
            el.get_attribute('value'),
            'signup'
            )

        # Edith notices an input box for her username for the first bookie. She enters her username
        # When she hits enter, the page updates, and now the page lists her username
        # The input text box is replaced by an edit button
        row = self.findRow('1')
        el = row.find_element_by_id('username')
        self.enterInput(el, 'edith66')

        # Edith clicks on it and the label is replaced by an input box, prepopulated with her username
        self.clickEdit(el, 'edith66')

        # She changes her username and it updates
        self.enterInput(el, 'bombedith21')
        
        # Edith then notices a status dropdown box, it has several options        
        # She selects one of the options and the status changes
        self.changeSelectInRow(row, 'initial')

        # The next action button now says create arbitrage market
        el = row.find_element_by_class_name('action')
        self.assertEqual(
            el.get_attribute('value'),
            'initial'
            )
        self.assertEqual(
            el.text,
            'Create Arb Market'
            )
        
        # Edith then notices balance and profit input boxes.        
        # She notes they work the same as the username box
        el = row.find_element_by_id('balance')
        self.enterInput(el, '20.57')
        self.clickEdit(el, '20.57')
        self.enterInput(el, '18.67')
        
        el = row.find_element_by_id('profit')
        self.enterInput(el, '-12.90')
        self.clickEdit(el, '-12.90')
        self.enterInput(el, '1.45')
        
        # There is also a checkbox labelled banked
        # Edith clicks it and all boxes are greyed out (except the checkbox)
        self.clickBanked(row)
        
        # The other rows are unaffected
        row = self.findRow('2')
        self.checkElemsAreEnabled(row, 'input', True)
        
        # She clicks it again and all boxes are as before (except the checkbox)
        self.unclickBanked(self.findRow('1'))
        
        # She goes to sleep, delighted

    def test_multiple_users_can_start_and_retrieve_summaries_at_different_urls(self):
        self.initiateDatabase()
        # Edith starts a new summary and edits the first row
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('new_summary').click()

        row = self.findRow('1')
        el = row.find_element_by_id('username')
        self.enterInput(el, 'edith66')
        el = row.find_element_by_id('balance')
        self.enterInput(el, '20.57')
        el = row.find_element_by_id('profit')
        self.enterInput(el, '-12.90')
        self.changeSelectInRow(row, 'initial')
        self.clickBanked(row)

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/summary/.+')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page and starts a new summary.
        # There is no sign of Edith's summary
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('new_summary').click()
        
        input_list = self.browser.find_elements_by_css_selector('.input')
        values = [item.get_attribute("value") for item in input_list]
        self.assertNotIn('edith66', values)
        self.assertNotIn('20.57', values)
        self.assertNotIn('-12.90', values)

        # Francis starts a new summary by filling in the second row.
        row = self.findRow('2')
        el = row.find_element_by_id('username')
        self.enterInput(el, 'francis27')
        el = row.find_element_by_id('balance')
        self.enterInput(el, '11.23')
        el = row.find_element_by_id('profit')
        self.enterInput(el, '8.68')
        self.changeSelectInRow(row, 'deposit')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/summary/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        input_list = self.browser.find_elements_by_css_selector('.input')
        values = [item.get_attribute("value") for item in input_list]
        self.assertNotIn('edith66', values)
        self.assertNotIn('20.57', values)
        self.assertNotIn('-12.90', values)

        # Francis shuts down his browser
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Edith cannot overcome the urge to visit her list again
        self.browser.get(edith_list_url)

        # It is as she left it
        input_list = self.browser.find_elements_by_css_selector('.input')
        values = [item.get_attribute("value") for item in input_list]
        self.assertIn('edith66', values)
        self.assertIn('20.57', values)
        self.assertIn('-12.90', values) 

        # and does not contain any of Francis' list
        self.assertNotIn('francis27', values)
        self.assertNotIn('11.23', values)
        self.assertNotIn('8.68', values)

        # Edith shuts down her browser
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis too, is weak
        self.browser.get(francis_list_url)

        # It is as he left it
        input_list = self.browser.find_elements_by_css_selector('.input')
        values = [item.get_attribute("value") for item in input_list]
        self.assertIn('francis27', values)
        self.assertIn('11.23', values)
        self.assertIn('8.68', values)

        # and does not contain any of Edith's' list
        self.assertNotIn('edith66', values)
        self.assertNotIn('20.57', values)
        self.assertNotIn('-12.90', values)

        # Satisfied, they both go back to sleep

        

       

