from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Заполнение обязательных полей с уникальными селекторами
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Ivan")
        
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Petrov")
        
        email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        email.send_keys("test@example.com")
        
        # Отправка формы
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Проверка успешной регистрации
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return "Congratulations! You have successfully registered!" in welcome_text
        
    finally:
        time.sleep(5)
        browser.quit()

# Тест должен пройти
print("Test registration1.html:", test_registration("http://suninjuly.github.io/registration1.html"))

# Тест должен упасть с NoSuchElementException
print("Test registration2.html:", test_registration("http://suninjuly.github.io/registration2.html"))