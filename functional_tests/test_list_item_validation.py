from selenium.webdriver.common.keys import Keys

from functional_tests.base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_submit_non_numeric_balance_or_profit(self):
        self.initiateDatabase()
        # Edith goes to the home page and accidentally tries to submit
        # a non-numeric value in balance. She hits Enter input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('new_summary').click()

        el = self.findElement('1', 'balance')
        el.find_element_by_class_name('input').clear()
        el.find_element_by_class_name('input').send_keys('non-numeric')
        el.find_element_by_class_name('input').send_keys(Keys.ENTER)

        # An error message is displayed
        body = self.browser.find_element_by_css_selector('body')
        self.checkIsDisplayed(body, 'has-error', True)
        
        # She corrects the error and resubmits. The error disappears
        # And she can submit it successfully
        
        self.enterInput('1', 'balance', '-10.43')
        self.checkIsDisplayed(body, 'has-error', False)
