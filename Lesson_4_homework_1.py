from selenium import webdriver


browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element_by_id("id_q").clear()
    browser.find_element_by_id("id_q").send_keys("Google")
    browser.find_element_by_css_selector("[value='Найти']").click()
    result_of_seek = browser.find_element_by_css_selector(".product_pod h3 a").get_attribute("title")

    assert "Google" in result_of_seek, "Нашлось что-то не то"

finally:
    browser.quit()
