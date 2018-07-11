from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import os, time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewVisitorAccountSummaryTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

        self.staging_server = os.environ.get('STAGING_SERVER')
        if self.staging_server:
            self.live_server_url = 'http://' + self.staging_server
            reset_database(self.staging_server)
            
    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()
        super().tearDown()

    ###################################################################

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

        # Edith notices an input box for her username for one of the bookies. She enters her username
        # When she hits enter, the page updates, and now the page lists her username
        self.browser.find_element_by_css_selector('input[name="bet365-username"]').send_keys('edith66')
        self.browser.find_element_by_css_selector('input[name="bet365-username"]').send_keys(Keys.ENTER)
        time.sleep(3)
        self.assertEqual(self.browser.find_element_by_css_selector('input[name="bet365-username"]').is_displayed(), False)
        self.assertEqual(self.browser.find_element_by_id('bet365-username-text').is_displayed(), True)
        self.assertEqual(self.browser.find_element_by_id('bet365-username-text').text, 'edith66')

        # The input text box is replaced by an edit button

        # Edith clicks on it and the label is replaced by an input box, prepopulated with her username

        # She changes her username and it updates
        
        # Edith then notices a status box, it has several options

        # She selects one of the options and the status changes

        # Edith then notices balance and profit input boxes.
        # She notes they work the same as the username box

        # There is also a checkbox labelled banked

        # Edith clicks it and all boxes are greyed out (except the checkbox)

        # She goes to sleep, delighted

        

       

