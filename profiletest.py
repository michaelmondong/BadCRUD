import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProfileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        option = webdriver.FirefoxOptions()
        cls.browser = webdriver.Firefox(options=option)
        try:
            cls.url = os.environ['URL']
        except:
            cls.url = "http://localhost"

    def test(self):
        self.login_correct()
        self.profile_page()
        self.profile_picture()

    def login_correct(self):
        login_url = self.url + '/login.php'
        self.browser.get(login_url)

        self.browser.find_element(By.ID, 'inputUsername').send_keys('admin')
        self.browser.find_element(By.ID, 'inputPassword').send_keys('nimda666!')
        self.browser.find_element(By.TAG_NAME, 'button').click()

    def profile_page(self):
        profile_url = self.url + '/profil.php'
        self.browser.get(profile_url)

    def profile_picture(self):
        file_input = self.browser.find_element(By.ID, 'formFile')
        
        image_path = os.path.join(os.getcwd(), 'image.jpg')
        file_input.send_keys(image_path)

        submit_button = self.browser.find_element(By.CSS_SELECTOR, 'button.btn-secondary')
        submit_button.click()

        redirected_url = self.url + '/profil.php'
        self.assertEqual(redirected_url, self.browser.current_url)

        new_profile_picture = self.browser.find_element(By.CSS_SELECTOR, 'img[src="image/profile.jpg"]')
        self.assertIsNotNone(new_profile_picture)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')
