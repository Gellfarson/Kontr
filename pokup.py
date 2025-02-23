from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
driver = webdriver.Chrome()  # Убедитесь, что chromedriver доступен
driver.maximize_window()

try:
    # Шаг 1: Открываем сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Шаг 2: Авторизуемся как standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ждём загрузки страницы с товарами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    # Шаг 3: Добавляем товары в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items_to_add:
        driver.find_element(By.XPATH, f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button").click()

    # Шаг 4: Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Ждём загрузки корзины
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )

    # Шаг 5: Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()

    # Ждём загрузки формы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    # Шаг 6: Заполняем форму
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    # Шаг 7: Нажимаем Continue
    driver.find_element(By.ID, "continue").click()

    # Ждём загрузки страницы с итогами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    # Шаг 8: Читаем итоговую стоимость
    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    # Шаг 9: Проверяем, что итоговая сумма равна $58.29
    assert total == "Total: $58.29", f"Ожидаемая сумма $58.29, но получено {total}"
    print("Тест пройден успешно: итоговая сумма = $58.29")

except AssertionError as e:
    print(f"Тест не пройден: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Закрываем браузер
    driver.quit()