from selenium.webdriver.common.keys import Keys
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from django.core import mail
from .base import FunctionalTest
User = get_user_model()

import time
import re

TEST_EMAIL = 'edith@example.com'


class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk 
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()
        ## to set a cookie we need to first visit the domain.
        ## 404 pages load the quickest!
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key, 
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        self.create_pre_authenticated_session('edith@example.com')

        # She goes to the home page and creates a new summary
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('new_summary').click()
        name = self.browser.find_element_by_id('summary_name')
        self.enterInput(name, "Edith's Summary")

        # She notices a "My Accounts" link, for the first time.
        self.browser.find_element_by_link_text('My Account Summaries').click()

        # She sees that her summary is in there, named accordingly
        self.wait_for(
            lambda: self.browser.find_element_by_link_text("Edith's Summary")
        )

        # She decides to start another summary, just to see
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('new_summary').click()
        name = self.browser.find_element_by_id('summary_name')
        self.enterInput(name, "Edith's Second Summary")
        second_list_url = self.browser.current_url

        # Under "my lists", her new list appears
        self.browser.find_element_by_link_text('My Account Summaries').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text("Edith's Second Summary")
        )
        self.browser.find_element_by_link_text("Edith's Second Summary").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # She logs out.  The "My lists" option disappears
        self.browser.find_element_by_link_text('Log Out').click()
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_elements_by_link_text('My Account Summaries'),
            []
        ))

    def test_login_saves_user_as_current_summary_owner(self):
        # Edith goes to the home page and creates a new summary
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('new_summary').click()
        name = self.browser.find_element_by_id('summary_name')
        self.enterInput(name, "Edith's Summary")
        
        # She then clicks the login liink
        self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))
        email = mail.outbox[0]
        url_search = re.search(r'http://.+/.+$', email.body)
        url = url_search.group(0)
        self.browser.get(url)

        # She clicks the "My Accounts" link.
        self.browser.find_element_by_link_text('My Account Summaries').click()

        # She sees that her summary is in there, named accordingly
        self.wait_for(
            lambda: self.browser.find_element_by_link_text("Edith's Summary")
        )

        
