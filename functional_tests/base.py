from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time, os

MAX_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

        staging_server = os.environ.get('STAGING_SERVER')  
        if staging_server:
            self.live_server_url = 'http://' + staging_server
            reset_database(self.staging_server)

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()
        super().tearDown()

    ##########  HELPER FUNCTIONS #########
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
                
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    ######################################
    def findElement(self, rowID, element):
        row = self.browser.find_element_by_css_selector('tr[data-id="'+rowID+'"]')
        return row.find_element_by_id(element)
  
    def checkIsDisplayed(self, element, item, state):
        self.wait_for(lambda: self.assertEqual(
            element.find_element_by_class_name(item).is_displayed()
            , state
        ))

    def enterInput(self, rowID, element, text):
        el = self.findElement(rowID, element)
        el.find_element_by_class_name('input').clear()
        el.find_element_by_class_name('input').send_keys(text)
        el.find_element_by_class_name('input').send_keys(Keys.ENTER)
        
        self.checkIsDisplayed(el, 'input', False)
        self.checkIsDisplayed(el, 'text', True)
        self.checkIsDisplayed(el, 'edit', True)
        self.wait_for(lambda: self.assertEqual(
           el.find_element_by_class_name('text').text
               , text
        ))

    def clickEdit(self, rowID, element, text):
        el = self.findElement(rowID, element)
        el.find_element_by_class_name('edit').click()

        self.checkIsDisplayed(el, 'edit', False)
        self.checkIsDisplayed(el, 'text', False)
        self.checkIsDisplayed(el, 'input', True)
        self.wait_for(lambda: self.assertEqual(
            el.find_element_by_class_name('input').get_attribute('placeholder')
            ,text
        ))
        
