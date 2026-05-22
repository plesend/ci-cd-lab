from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_page_title(driver):
    assert "Форма обратной связи" in driver.title


def test_form_elements_present(driver):
    name_field = driver.find_element(By.ID, "name")
    email_field = driver.find_element(By.ID, "email")
    message_field = driver.find_element(By.ID, "message")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    assert name_field.is_displayed()
    assert email_field.is_displayed()
    assert message_field.is_displayed()
    assert submit_button.is_displayed()


def test_form_submission_shows_success(driver):
    driver.find_element(By.ID, "name").send_keys("Иван Иванов")
    driver.find_element(By.ID, "email").send_keys("ivan@example.com")
    driver.find_element(By.ID, "message").send_keys("Тестовое сообщение")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    success = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "success-message"))
    )
    assert success.is_displayed()
    assert "Спасибо" in success.text


def test_form_required_fields(driver):
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    time.sleep(0.5)

    # Проверяем, что форма не скрыта (валидация браузера не пропустила пустую форму)
    form = driver.find_element(By.ID, "contact-form")
    assert form.is_displayed()
    success = driver.find_element(By.ID, "success-message")
    assert not success.is_displayed()
