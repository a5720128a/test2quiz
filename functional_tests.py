from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_quiz_and_use_functions(self):
        
        # Kan has heard about a cool new online "quiz" app.
        self.browser.get('http://localhost:8000/')
        # Kan goes to check out its homepage.
        # Kan notices the page title and header mention quiz.
        self.assertIn('quiz', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('quiz', header_text)
        # Kan enter the first quiz in webapp.
        self.fail('Finish the test!')
        # Kan choose first checkblock as true.

        # Kan choose 2 other checkblock as false.

        # Kan click submit.
        
        # Kan has 2 point on result page.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
