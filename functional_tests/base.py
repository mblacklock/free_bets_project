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
        aff1 = Affiliate.objects.create(name='Aff1', url='http://www.aff1.com/')
        aff2 = Affiliate.objects.create(name='Aff2', url='http://www.aff2.com/')

    ###### GET ELEMENTS ######

    @wait
    def findRow(self, rowID):
        return self.browser.find_element_by_css_selector('tr[data-id="'+rowID+'"]')

    @wait
    def getSelectBox(self, parent):
        select_box = parent.find_element_by_class_name('select')
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        self.assertNotEqual(len(options),0)
        return select_box

    ##### CHECK ELEMENTS #####
  
    @wait
    def checkIsDisplayed(self, element, item, state):
        self.assertEqual(
            element.find_element_by_class_name(item).is_displayed()
            , state
        )

    @wait
    def checkIsChecked(self, element, state):
        self.assertEqual(
            element.is_selected()
            , state
        )

    @wait
    def checkElemsAreEnabled(self, parent, item, state):
        elements = parent.find_elements_by_class_name(item)
        [self.assertEqual(element.is_enabled(), state) for element in elements]

    @wait
    def checkIsEnabled(self, element, item, state):
        self.assertEqual(
            element.find_element_by_class_name(item).is_enabled()
            , state
        )

    @wait
    def checkRunnerValues(self, runner, lay_stake, profit_loss):
        self.assertEqual(runner.find_element_by_class_name('lay_stake').text,
                         lay_stake
                         )
        self.assertEqual(runner.find_element_by_class_name('profit_loss').text,
                         profit_loss
                         )

    @wait
    def check_logged_in(self, email):
        self.browser.find_element_by_link_text('Log Out')
        login_section = self.browser.find_element_by_css_selector('.login')
        self.assertIn(email, login_section.text)

    @wait
    def check_logged_out(self, email):
        self.browser.find_element_by_name('email')
        login_section = self.browser.find_element_by_css_selector('.login')
        self.assertNotIn(email, login_section.text)
        
    ##### CHANGE ELEMENTS#####
    
    @wait
    def enterInput(self, element, text, check=True):
        item = element.find_element_by_class_name('input')
        item.clear()
        item.send_keys(text)
        item.send_keys(Keys.ENTER)
        
        if check:
            self.checkIsEnabled(element, 'input', False)
            self.checkIsDisplayed(element, 'edit', True)
        self.assertEqual(
           item.get_attribute('value')
               , text
        )

    @wait
    def clickEdit(self, element, text):
        element.find_element_by_class_name('edit').click()

        self.checkIsDisplayed(element, 'edit', False)
        self.checkIsEnabled(element, 'input', True)
        self.assertEqual(
            element.find_element_by_class_name('input').get_attribute('value')
            ,text
        )

    @wait
    def clickBanked(self, row):
        check = row.find_element_by_id('banked').find_element_by_class_name('banked')
        check.send_keys(Keys.SPACE)

        self.checkIsChecked(check, True)
        self.checkElemsAreEnabled(row, 'input', False)
        self.checkElemsAreEnabled(row, 'edit', False)
        self.checkElemsAreEnabled(row, 'status', False)
        self.checkElemsAreEnabled(row, 'action', False) 

    @wait
    def unclickBanked(self, row):
        check = row.find_element_by_id('banked').find_element_by_class_name('banked')
        check.send_keys(Keys.SPACE)

        self.checkIsChecked(check, False)        
        self.checkElemsAreEnabled(row, 'edit', True)
        self.checkElemsAreEnabled(row, 'status', True)

    @wait
    def changeSelectBox(self, select_box, option):
        select_box.find_element_by_css_selector('option[value="'+option+'"]').click()
        self.assertEqual(Select(select_box).first_selected_option.get_attribute("value") , option)

    @wait
    def changeSelectInRow(self, row, option):
        el = row.find_element_by_id('status')
        select_box = self.getSelectBox(el)
        self.changeSelectBox(select_box, option)
        
