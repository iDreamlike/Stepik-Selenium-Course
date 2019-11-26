# Предусловия: добавляем через API тестовый товар - книга под названием "Google Hacking"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element_by_id("id_q").clear()
    browser.find_element_by_id("id_q").send_keys("Google")
    browser.find_element_by_css_selector("[value='Найти']").click()

    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".product_pod h3 a"))
    )
    result_of_seek = browser.find_element_by_css_selector(".product_pod h3 a").get_attribute("title")
    assert "Google" in result_of_seek, "Нашлось что-то не то"

finally:
    browser.quit()


# Если получаем исключение NoSuchElementException - значит не нашлось вообще ничего, а должно.
# Если получаем AssertionError: "Нашлось что-то не то" - значит поиск выдает неверные результаты.

# Постусловия: удаляем через API тестовый товар "Google Hacking".
