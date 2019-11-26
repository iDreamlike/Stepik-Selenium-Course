from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element(By.ID, "login_link").click()

    time.sleep(1)
    browser.find_element(By.ID, "id_registration-email").send_keys("login_11@mail.ru")
    browser.find_element(By.ID, "id_registration-password1").send_keys("Qq111111Qq")
    browser.find_element(By.ID, "id_registration-password2").send_keys("Qq111111Qq")
    browser.find_element(By.NAME, "registration_submit").click()

    assert "Спасибо за регистрацию!" == browser.find_element_by_css_selector("#messages div div").text, "Регистрация \
                                                                                                         не прошла"
finally:
    time.sleep(1)
    browser.quit()

