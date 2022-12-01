
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math
import os 

def calc(xtext):
  return str(math.log(abs(12*math.sin(int(xtext)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, "input_value")
    xtext = x_element.text    
    y = calc(xtext)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)	
 
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

finally:
 
    time.sleep(15)
   
    browser.quit()





