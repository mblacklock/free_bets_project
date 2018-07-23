from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver

import time

from functional_tests.base import FunctionalTest

class NewVisitorAccountSummaryTest(FunctionalTest):

    def test_can_start_summary_for_single_user(self):
        self.initiateDatabase()
        # Edith has heard about a cool new online free bets app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She sees a create account button and clicks it
        self.browser.find_element_by_name('new_summary').click()

        # She notices that her account summary has a unique URL
        self.assertRegex(self.browser.current_url, '/summary/.+')
        
        # She notices the page title and header mention free bets
        self.assertIn('Free Bets', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Free Bets', header_text)

        # Edith see that the newly created summary has an input box to enter a title
        # She enters a name and hits enter, it updates and is replaced by an edit button
        self.enterSummaryName("Edith's Summary")
        
        # She clicks edit and is able to change her summary name
        self.clickEditSummaryName("Edith's Summary")
        self.enterSummaryName("Bombedith's Summary")
            
        # She notices a table of bookmakers
        table = self.browser.find_element_by_tag_name('table')
        self.assertEqual(
            table.get_attribute('name'),
            'bookie-summary'
        )

        # Edith notices an input box for her username for the first bookie. She enters her username
        # When she hits enter, the page updates, and now the page lists her username
        # The input text box is replaced by an edit button
        self.enterInput('1', 'username', 'edith66')        

        # Edith clicks on it and the label is replaced by an input box, prepopulated with her username
        self.clickEdit('1', 'username', 'edith66')

        # She changes her username and it updates
        self.enterInput('1', 'username', 'bombedith21')
        
        # Edith then notices a status dropdown box, it has several options
        select_box = self.findElement('1', 'status').find_element_by_class_name('status')
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        self.assertNotEqual(len(options),0)

        # She selects one of the options and the status changes
        self.changeStatus('1', 'initial', 'Initial Bet')

        # Edith then notices balance and profit input boxes.        
        # She notes they work the same as the username box
        self.enterInput('1', 'balance', '20.57')
        self.clickEdit('1', 'balance', '20.57')
        self.enterInput('1', 'balance', '18.67')
        
        self.enterInput('1', 'profit', '-12.90')
        self.clickEdit('1', 'profit', '-12.90')
        self.enterInput('1', 'profit', '1.45')
        
        # There is also a checkbox labelled banked
        # Edith clicks it and all boxes are greyed out (except the checkbox)
        self.clickCheckbox('1')
        
        # The other rows are unaffected
        row = self.browser.find_element_by_css_selector('tr[data-id="2"]')
        elements = row.find_elements_by_class_name('input')
        [self.assertEqual(element.is_enabled(), True) for element in elements]
        
        # She clicks it again and all boxes are as before (except the checkbox)
        self.unclickCheckbox('1')
        
        # She goes to sleep, delighted

    def test_multiple_users_can_start_and_retrieve_summaries_at_different_urls(self):

        self.initiateDatabase()
        # Edith starts a new summary and edits the first row
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('new_summary').click()
        
        self.enterInput('1', 'username', 'edith66')
        self.enterInput('1', 'balance', '20.57')
        self.enterInput('1', 'profit', '-12.90')
        self.changeStatus('1', 'initial', 'Initial Bet')
        self.clickCheckbox('1')

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
        self.browser.find_element_by_name('new_summary').click()
        
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('edith66', page_text)
        self.assertNotIn('20.57', page_text)
        self.assertNotIn('-12.90', page_text)

        # Francis starts a new summary by filling in the second row.
        self.enterInput('2', 'username', 'francis27')
        self.enterInput('2', 'balance', '11.23')
        self.enterInput('2', 'profit', '8.68')
        self.changeStatus('2', 'deposit', 'Deposit')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/summary/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('edith66', page_text)
        self.assertNotIn('20.57', page_text)
        self.assertNotIn('-12.90', page_text)

        # Francis shuts down his browser
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Edith cannot overcome the urge to visit her list again
        self.browser.get(edith_list_url)

        # It is as she left it
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('edith66', page_text)
        self.assertIn('20.57', page_text)
        self.assertIn('-12.90', page_text)

        # and does not contain any of Francis' list
        self.assertNotIn('francis27', page_text)
        self.assertNotIn('11.23', page_text)
        self.assertNotIn('8.68', page_text)

        # Edith shuts down her browser
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis too, is weak
        self.browser.get(francis_list_url)

        # It is as he left it
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('francis27', page_text)
        self.assertIn('11.23', page_text)
        self.assertIn('8.68', page_text)

        # and does not contain any of Edith's' list
        self.assertNotIn('edith66', page_text)
        self.assertNotIn('20.57', page_text)
        self.assertNotIn('-12.90', page_text)

        # Satisfied, they both go back to sleep

        

       

