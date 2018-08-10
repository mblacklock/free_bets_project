from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from unittest import skip

import time

from functional_tests.base import FunctionalTest

class NavbarTest(FunctionalTest):

    def test_navbar_login_works(self):
        # Edith has heard about a cool new online free bets app. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She starts a new summary and notices the navbar
        self.browser.find_element_by_class_name('new_summary').click()
        navbar = self.browser.find_element_by_class_name('navbar')

        # There is a login form
        login = navbar.find_element_by_class_name('login')

        # Edith enters her email and clicks login
        login.find_element_by_name('email').clear()
        login.find_element_by_name('email').send_keys('edith@example.com')
        login.find_element_by_name('email').send_keys(Keys.ENTER)

        # A message appears telling her an email has been sent
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # Satisfied, she goes back to sleep

        

       

