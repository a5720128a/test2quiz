from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_quiz_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)

    def test_can_start_quiz_and_use_functions(self):
        
        # Kan has heard about a cool new online "quiz" app.
        self.browser.get(self.live_server_url)
        # Kan goes to check out its homepage.
        # Kan notices the page title and header mention quiz.
        self.assertIn('quiz', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('quiz', header_text)
        # Kan is invited to enter a quiz item straight away
        inputbox = self.browser.find_element_by_id('id_new_quiz')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Add new quiz'
        )
        # Kan types "maner" into a text box
        inputbox.send_keys('maner')
        
        # When Kan hits enter, the page updates, and now the page quiz lists
        # "maner" as an item in a quiz list table
        inputbox.send_keys(Keys.ENTER)  
        self.check_for_row_in_list_table('1: maner')
        
        # Kan enter the first quiz in webapp.
        fisrt_quiz = self.browser.find_element_by_id('quiz 1')
        fisrt_quiz.send_keys('enter')
        
        # Kan choose first checkblock as true.

        # Kan choose 2 other checkblock as false.

        # Kan click submit.
        
        # Kan has 2 point on result page.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
