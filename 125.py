from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    # Находим все текстовые поля по тегу input с типом text
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    
    # Заполняем каждое поле коротким текстом
    for element in elements:
        element.send_keys("Data")
    
    # Находим и кликаем кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время скопировать код
    time.sleep(30)
    # Закрываем браузер
    browser.quit()