from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from unittest import skip

import time

from functional_tests.base import FunctionalTest

class AffiliateClickTest(FunctionalTest):

    def test_can_start_summary_for_single_user(self):
        self.initiateDatabase()
        # Edith starts a new summary and clicks the first bookies sign up button
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_class_name('new_summary').click()
        row = self.findRow('1')
        row.find_element_by_class_name('action').click()

        # She goes to the tracking page
        self.browser.get(self.live_server_url + '/summary/tracking/')

        # Her click is listed
        click = self.browser.find_element_by_class_name('click')
        time.sleep(3)
        self.assertEqual(
            click.find_element_by_class_name('affiliate_name').text,
            'Aff1'
        )

        # Satisfied, they both go back to sleep

        

       

