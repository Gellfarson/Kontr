# test_02_calc.py
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

def test_calculator(driver):
    # Шаг 1: Открываем страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Шаг 2: Вводим значение 45 в поле #delay
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()  # Очищаем поле перед вводом
    delay_input.send_keys("45")
    
    # Шаг 3: Нажимаем кнопки 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    
    # Шаг 4: Ждем 45 секунд и проверяем результат
    wait = WebDriverWait(driver, 50)  # Таймаут чуть больше 45 секунд
    result = wait.until(
        EC.text_to_be_present_in_element((By.ID, "result"), "15"),
        message="Результат должен быть 15 после 45 секунд"
    )
    
    # Проверка результата
    assert result, "Ожидаемый результат '15' не появился после 45 секунд"