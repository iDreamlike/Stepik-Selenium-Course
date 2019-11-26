from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element(By.ID, "login_link").click()

    time.sleep(1)
    browser.find_element(By.ID, "id_login-username").send_keys("bertest1@mail.ru")
    browser.find_element(By.ID, "id_login-password").send_keys("Qq111111Qq")
    browser.find_element(By.NAME, "login_submit").click()


    # WebDriverWait(browser, 2).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/ru/accounts/']"))
    # )
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/']").click()

    time.sleep(1)
    # WebDriverWait(browser, 2).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "[href='/ru/accounts/addresses/']"))
    # )
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/addresses/']").click()

    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/addresses/add/']").click()
    time.sleep(1)
    Select(browser.find_element_by_id("id_title")).select_by_value("Mr")

    browser.find_element(By.ID, "id_first_name").send_keys("Иван")
    browser.find_element(By.ID, "id_last_name").send_keys("Иванов")
    browser.find_element(By.ID, "id_line1").send_keys("Адрес5")
    browser.find_element(By.ID, "id_line2").send_keys("Адрес2")
    browser.find_element(By.ID, "id_line3").send_keys("Адрес3")
    browser.find_element(By.ID, "id_line4").send_keys("Город")
    browser.find_element(By.ID, "id_state").send_keys("Область")
    browser.find_element(By.ID, "id_postcode").send_keys("190000")
    Select(browser.find_element_by_id("id_country")).select_by_value("RU")
    browser.find_element(By.ID, "id_phone_number").send_keys("8123270000")
    browser.find_element(By.ID, "id_notes").send_keys("Тестовые инструкции")
    browser.find_element(By.CSS_SELECTOR, ".col-sm-offset-4 button").click()

    assert "добавлен" in browser.find_element_by_css_selector("#messages div div").text, "Адрес не добавлен"

    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/logout/']").click()

finally:
    time.sleep(5)
    browser.quit()
