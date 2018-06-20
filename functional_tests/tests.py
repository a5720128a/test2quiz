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
        url_table = self.browser.find_element_by_id('id_quiz_table')  
        url = url_table.find_element_by_link_text('maner')
        url.send_keys(Keys.ENTER)
        
        # Kan add the question "กินเรียบร้อย" to "maner" quiz
        # "กินเรียบร้อย" as an item in a quiz list table
        time.sleep(1)
        inputbox2 = self.browser.find_element_by_id('id_new_question')
        inputbox2.send_keys('กินเรียบร้อย')
        inputbox2.send_keys(Keys.ENTER)
        time.sleep(1)
        question_text_ = self.browser.find_element_by_id('question 1')
        self.assertEqual(question_text_.text,'กินเรียบร้อย')
        
        # Kan add second question "รวบช้อนส้อมหลังกินเสร็จ"

        # "รวบช้อนส้อมหลังกินเสร็จ" as an item in a quiz list table
        time.sleep(1)
        inputbox2 = self.browser.find_element_by_id('id_new_question')
        inputbox2.send_keys('รวบช้อนส้อมหลังกินเสร็จ')
        inputbox2.send_keys(Keys.ENTER)
        time.sleep(1)
        question_text_ = self.browser.find_element_by_id('question 2')
        self.assertEqual(question_text_.text,'รวบช้อนส้อมหลังกินเสร็จ')
        
        # Kan choose first question checkblock as true.
        checkbox = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='1']").click

        # Kan choose second checkblock as true.
        checkbox2 = self.browser.find_element_by_xpath(".//input[@type='radio' and @value='1']").click

        # Kan fill his name in user name text box "Kan"
        # Kan submit.
        inputbox3 = self.browser.find_element_by_id('id_new_user')
        inputbox3.send_keys('Kan')
        inputbox3.send_keys(Keys.ENTER)
        
        time.sleep(1)

        # Kan see global stat, got 2 point, see all correct,  on result page.
        global_stat1 = self.browser.find_element_by_id('stat 1').text
        self.assertIn('กินเรียบร้อย -- true correct    global stats   correct 1  incorrect 0', global_stat1)

        global_stat2 = self.browser.find_element_by_id('stat 2').text
        self.assertIn('รวบช้อนส้อมหลังกินเสร็จ -- true correct    global stats   correct 1  incorrect 0', global_stat2)

        correct1 = self.browser.find_element_by_id('point 1').text
        self.assertIn('1 : กินเรียบร้อย --> correct', correct1)
        correct2 = self.browser.find_element_by_id('point 2').text
        self.assertIn('2 : รวบช้อนส้อมหลังกินเสร็จ --> correct', correct2)
        kan_point = self.browser.find_element_by_id('result_point').text
        self.assertIn('your point = 2', kan_point)
        
        # Kan close browser and turn off pc then go to sleep.
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')
