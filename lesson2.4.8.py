from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

def calc(xtext):
  return str(math.log(abs(12*math.sin(int(xtext)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    xtext = x_element.text
    y = calc(xtext)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:

    time.sleep(10)

    browser.quit()
