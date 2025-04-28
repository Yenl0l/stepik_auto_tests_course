from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    
    # Заполняем форму
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    
    # Находим кнопку Submit по XPath (по тексту на кнопке)
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    # Закрываем браузер
    browser.quit()