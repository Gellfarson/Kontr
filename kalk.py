from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
driver = webdriver.Chrome()  # Убедитесь, что chromedriver доступен
driver.maximize_window()

try:
    # Шаг 1: Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Шаг 2: Вводим значение 45 в поле #delay
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Шаг 3: Нажимаем кнопки 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Шаг 4: Ждём, пока результат станет "15" (максимум 50 секунд)
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Шаг 5: Проверяем, что результат верный
    assert result, "Результат не равен 15 после 45 секунд ожидания"
    assert driver.find_element(By.CLASS_NAME, "screen").text == "15", "Ожидаемый результат '15', но получено что-то другое"
    print("Тест пройден успешно: результат = 15")

except AssertionError as e:
    print(f"Тест не пройден: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Закрываем браузер
    driver.quit()