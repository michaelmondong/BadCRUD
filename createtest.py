import unittest
import os
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CreateContact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost/4444"
        cls.name_query = ''.join(random.choices(string.ascii_letters, k=10))

    def test(self)
        self.create_contact()

    def create_contact(self):
        create_url = self.url + '/create.php'
        self.browser.get(create_url)

        self.browser.find_element(By.ID, 'name').send_keys(self.name_query)
        self.browser.find_element(By.ID, 'email').send_keys('test@example.com')
        self.browser.find_element(By.ID, 'phone').send_keys('1234567890')
        self.browser.find_element(By.ID, 'title').send_keys('Developer')

        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        index_page_title = "Dashboard"
        actual_title = self.browser.title
        self.assertEqual(index_page_title, actual_title)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
