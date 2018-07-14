from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

from functional_tests.base import FunctionalTest

class NewVisitorAccountSummaryTest(FunctionalTest):

    def test_can_view_edit_and_retrieve_summary(self):
        # Edith has heard about a cool new online free bets app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention free bets
        self.assertIn('Free Bets', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Free Bets', header_text)

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
        select_box = self.findElement('1', 'status')
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        self.assertNotEqual(len(options),0)

        # She selects one of the options and the status changes
        select_box.find_element_by_css_selector('option[value="initial"]').click()
        self.assertEqual(Select(select_box).first_selected_option.text, "Initial Bet")

        # Edith then notices balance and profit input boxes.        
        # She notes they work the same as the username box
        self.enterInput('1', 'balance', '20.57')
        self.clickEdit('1', 'balance', '18.67')
        self.enterInput('1', 'profit', '-12.90')
        self.clickEdit('1', 'profit', '1.45')
        # There is also a checkbox labelled banked

        # Edith clicks it and all boxes are greyed out (except the checkbox)

        # She goes to sleep, delighted

        

       

