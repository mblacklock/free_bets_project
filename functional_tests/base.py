from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time, os

from bets.models import Affiliate

MAX_WAIT = 5

def wait(fn):  
    def modified_fn(*args, **kwargs):  
        start_time = time.time()
        while True:  
            try:
                return fn(*args, **kwargs)  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn  

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
    @wait
    def wait_for(self, fn):
        return fn()
    ######################################
    def initiateDatabase(self):
        aff1 = Affiliate.objects.create(name='Aff1')
        aff2 = Affiliate.objects.create(name='Aff2')
    
    def findElement(self, rowID, element):
        row = self.browser.find_element_by_css_selector('tr[data-id="'+rowID+'"]')
        return row.find_element_by_id(element)

    @wait
    def clickCheckbox(self, rowID):
        check = self.findElement(rowID, 'banked')
        check.find_element_by_class_name('banked').click()
        
        row = self.browser.find_element_by_css_selector('tr[data-id="'+rowID+'"]')
        self.checkIsEnabled(row, 'input', False)
        self.checkIsEnabled(row, 'edit', False)
        self.checkIsEnabled(row, 'status', False)

    @wait
    def unclickCheckbox(self, rowID):
        check = self.findElement(rowID, 'banked')
        check.find_element_by_class_name('banked').click()
        
        row = self.browser.find_element_by_css_selector('tr[data-id="'+rowID+'"]')
        self.checkIsEnabled(row, 'input', True)
        self.checkIsEnabled(row, 'edit', True)
        self.checkIsEnabled(row, 'status', True)
  
    @wait
    def checkIsDisplayed(self, element, item, state):
        self.assertEqual(
            element.find_element_by_class_name(item).is_displayed()
            , state
        )

    @wait
    def checkIsChecked(self, item):
        self.assertEqual(
            element.find_elements_by_class_name(item).is_selected()
            , state
        )

    @wait
    def checkIsEnabled(self, row, item, state):
        elements = row.find_elements_by_class_name(item)
        [self.assertEqual(element.is_enabled(), state) for element in elements]

    @wait
    def enterInput(self, rowID, element, text):
        el = self.findElement(rowID, element)
        el.find_element_by_class_name('input').clear()
        el.find_element_by_class_name('input').send_keys(text)
        el.find_element_by_class_name('input').send_keys(Keys.ENTER)
        
        self.checkIsDisplayed(el, 'input', False)
        self.checkIsDisplayed(el, 'text', True)
        self.checkIsDisplayed(el, 'edit', True)
        self.assertEqual(
           el.find_element_by_class_name('text').text
               , text
        )

    @wait
    def clickEdit(self, rowID, element, text):
        el = self.findElement(rowID, element)
        el.find_element_by_class_name('edit').click()

        self.checkIsDisplayed(el, 'edit', False)
        self.checkIsDisplayed(el, 'text', False)
        self.checkIsDisplayed(el, 'input', True)
        self.assertEqual(
            el.find_element_by_class_name('input').get_attribute('placeholder')
            ,text
        )

    @wait
    def changeStatus(self, rowID, status, statusText):
        select_box = self.findElement(rowID, 'status').find_element_by_class_name('status')

        select_box.find_element_by_css_selector('option[value="'+status+'"]').click()
        self.assertEqual(Select(select_box).first_selected_option.text, statusText)
        
