from .base import FunctionalTest

import time


class NextActionTest(FunctionalTest):

     def test_next_action_button_is_correct(self):
        self.initiateDatabase()
        # Edith creates a new summary
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_class_name('new_summary').click()
        summary_url = self.browser.current_url

        # She notices the next action for the first item says sign up
        row = self.findRow('1')
        button = row.find_element_by_class_name('action')
        self.assertEqual(
            button.get_attribute('value'),
            'signup'
        )
            
        # Edith changes the status to deposit. The action button is unchanged
        self.changeSelectInRow(row, 'deposit')
        self.assertEqual(
            button.get_attribute('value'),
            'deposit'
        )

        # Edith changes the status to initial bet. The action button changes
        # to create arb market.
        self.changeSelectInRow(row, 'initial')
        self.assertEqual(
            button.get_attribute('value'),
            'initial'
        )

        # Edith clicks on it and the page redirects to the market page.
        # Initial bet is selected
        button.click()
        self.wait_for(lambda:
                      self.assertEqual(
            self.getSelectBox(self.browser.find_element_by_id('bet_type')).get_attribute('value'),
            'initial'
            )
        )

        # Edith returns to the summary and changes the status to free bet
        # Clicking it again goes to the market page, but free bet is selected
        self.browser.get(summary_url)
        row = self.findRow('1')
        button = row.find_element_by_class_name('action')
        self.changeSelectInRow(row, 'free')
        self.assertEqual(
            button.get_attribute('value'),
            'free'
        )
        button.click()
        self.wait_for(lambda: self.assertEqual(
            self.getSelectBox(self.browser.find_element_by_id('bet_type')).get_attribute('value'),
            'free'
            )
        )
        
        # Edith returns to the summary and changes the status to complete
        # The next action button disappears
        self.browser.get(summary_url)
        row = self.findRow('1')
        button = row.find_element_by_class_name('action')
        self.changeSelectInRow(row, 'complete')

        self.wait_for(lambda: self.assertEqual(
            button.is_displayed(),
            False
        ))
        
        # Edith changes the status back to initial. The button reappears
        self.browser.get(summary_url)
        row = self.findRow('1')
        button = row.find_element_by_class_name('action')
        self.changeSelectInRow(row, 'initial')

        self.wait_for(lambda: self.assertEqual(
            button.is_displayed(),
            True
        ))

        # She then clicks banked. The button is disabled.
        self.clickBanked(row)
        self.wait_for(lambda: self.assertEqual(
            button.is_displayed(),
            True
        ))
        self.checkElemsAreEnabled(row, 'action', False)

        # All the while, the second bookie is unaffected.
        row = self.findRow('2')
        self.checkElemsAreEnabled(row, 'action', True)
        button = row.find_element_by_class_name('action')
        self.assertEqual(
            button.get_attribute('value'),
            'signup'
        )

        # Neat, she goes to sleep.
