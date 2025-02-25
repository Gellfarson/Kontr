# test_01_form.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    # Отправка формы
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # Проверка Zip code (должен быть красным)
    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Zip code должен быть подсвечен красным"
    
    # Проверка остальных полей (должны быть зелеными)
    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    
    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        assert "is-valid" in field.get_attribute("class"), f"Поле {field_id} должно быть зелёным"