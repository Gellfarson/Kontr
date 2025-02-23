from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
driver = webdriver.Chrome()  # Убедитесь, что chromedriver доступен
driver.maximize_window()

try:
    # Шаг 1: Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Шаг 2: Заполняем форму значениями
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").clear()  # Оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Шаг 3: Нажимаем кнопку Submit
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    # Шаг 4: Ждём, пока форма обработается (появление класса is-invalid)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "is-invalid"))
    )

    # Шаг 5: Проверяем, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.NAME, "zip-code")
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"
    print("Поле Zip code подсвечено красным — проверка пройдена")

    # Шаг 6: Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]
    for field_name in fields_to_check:
        field = driver.find_element(By.NAME, field_name)
        assert "is-valid" in field.get_attribute("class"), f"Поле {field_name} не подсвечено зеленым"
    print("Все остальные поля подсвечены зеленым — проверка пройдена")

except AssertionError as e:
    print(f"Тест не пройден: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    # Закрываем браузер
    driver.quit()