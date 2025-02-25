# test_03_shop.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_shop_checkout(driver):
    # Шаг 1: Открываем сайт
    driver.get("https://www.saucedemo.com/")
    
    # Шаг 2: Авторизация как standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Пароль по умолчанию для этого пользователя
    driver.find_element(By.ID, "login-button").click()
    
    # Шаг 3: Добавляем товары в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    
    for item in items_to_add:
        driver.find_element(By.XPATH, f"//div[text()='{item}']/../../..//button[text()='Add to cart']").click()
    
    # Шаг 4: Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # Шаг 5: Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()
    
    # Шаг 6: Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    
    # Шаг 7: Нажимаем Continue
    driver.find_element(By.ID, "continue").click()
    
    # Шаг 8: Читаем итоговую стоимость
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    
    # Шаг 9: Проверяем итоговую сумму
    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Ожидаемая сумма '{expected_total}', но получено '{total_text}'"
