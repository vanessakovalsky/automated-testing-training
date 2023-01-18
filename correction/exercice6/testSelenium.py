import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a browser instance."""
        print("Test Execution Started")
        self.browser = webdriver.Remote(
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            command_executor='http://localhost:4444/wd/hub'
        )
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        """Assert that title of page says 'Google'."""
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
    
    def test_search_page_title(self):
        """Assert that Google search returns data for 'Red Hat'."""
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)
        self.browser.save_screenshot('beforecookies.png') # Permet de prendre une capture de l'état du navigateur
        WebDriverWait( self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Tout accepter')]")))
        self.browser.find_elements(By.XPATH, "//*[contains(text(), 'Tout accepter')]")[1].click() 
        self.browser.save_screenshot('aftercookies.png')
        element = self.browser.find_element(By.NAME, "q")
        assert element is not None
        element.send_keys('Red Hat')
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.browser.save_screenshot('result.png')
        assert self.browser.title.startswith('Red Hat')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))