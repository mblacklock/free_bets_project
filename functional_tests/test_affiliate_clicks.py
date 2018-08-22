from django.core import mail
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from unittest import skip
import re

import time

from functional_tests.base import FunctionalTest

TEST_EMAIL = 'edith@example.com'

class AffiliateClickTest(FunctionalTest):

    def test_affiliate_click_for_anon_user(self):
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
        self.assertEqual(
            click.find_element_by_class_name('affiliate_name').text,
            'Aff1'
        )

        # Satisfied, she goes back to sleep

    def test_affiliate_click_for_logged_user(self):
        self.initiateDatabase()
        
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))
        email = mail.outbox[0]
        url_search = re.search(r'http://.+/.+$', email.body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')
        url = url_search.group(0)

        self.browser.get(url)

        self.browser.find_element_by_class_name('new_summary').click()
        row = self.findRow('2')
        row.find_element_by_class_name('action').click()

        # She goes to the tracking page
        self.browser.get(self.live_server_url + '/summary/tracking/')

        # Her click is listed
        click = self.browser.find_element_by_class_name('click')
        self.assertEqual(
            click.find_element_by_class_name('affiliate_name').text,
            'Aff2'
        )
        self.assertEqual(
            click.find_element_by_class_name('user').text,
            TEST_EMAIL
        )

