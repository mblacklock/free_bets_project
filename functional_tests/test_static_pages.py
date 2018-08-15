from .base import FunctionalTest

import time


class StaticPagesTest(FunctionalTest):

     def test_privacy_policy_exists(self):
        # Edith visits the homepage and clicks on the privacy policy link
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('privacy').click()

        # The pages displays the privacy policy
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('Privacy', header_text)

        # Neat, she goes to sleep.
