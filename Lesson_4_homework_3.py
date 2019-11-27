from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")
browser.implicitly_wait(1)

try:
    browser.find_element(By.ID, "login_link").click()
    browser.find_element(By.ID, "id_login-username").send_keys("bertest1@mail.ru")
    browser.find_element(By.ID, "id_login-password").send_keys("Qq111111Qq")
    browser.find_element(By.NAME, "login_submit").click()
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/']").click()
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/addresses/']").click()
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/accounts/addresses/add/']").click()
    Select(browser.find_element_by_id("id_title")).select_by_value("Mr")
    browser.find_element(By.ID, "id_first_name").send_keys("Иван")
    browser.find_element(By.ID, "id_last_name").send_keys("Иванов")
    browser.find_element(By.ID, "id_line1").send_keys("Адрес7")
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
    browser.quit()
