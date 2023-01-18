# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    # EN local 
    # self.driver = webdriver.Firefox ## Installer connecteur entre selenium-webdriver et Firefox
    
    # En distant dans un conteneur
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    self.driver = webdriver.Remote(
        desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
        command_executor='http://localhost:4444/wd/hub',
            options=options
        )
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test2(self):
    self.driver.get("https://www.google.com/")

    assert self.driver.title=='Google'

    self.driver.find_element(By.NAME, "q").click()

    self.driver.find_element(By.NAME, "q").send_keys("ubuntu")
    self.driver.find_element(By.CSS_SELECTOR, "center:nth-child(1) > .gNO89b").click()
    self.driver.find_element(By.CSS_SELECTOR, ".eKjLze a .iUh30").click()
  
