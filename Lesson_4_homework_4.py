from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")
browser.maximize_window()
browser.implicitly_wait(1)
broken_goods = list()


try:
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/catalogue/']").click()

    while True:
        goods = browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-4.col-md-3.col-lg-3 img")
        for product in goods:
            if product.get_attribute("src") == "http://selenium1py.pythonanywhere.com/media/cache/ee/d6" \
                                               "/eed6bcfd8732ca981f2d25a20233226c.jpg":
                broken_goods.append(product.get_attribute("alt"))
        try:
            link = browser.find_element(By.CSS_SELECTOR, "li.next a")
            browser.execute_script("return arguments[0].scrollIntoView(true);", link)
            browser.find_element(By.CSS_SELECTOR, "li.next a").click()
        except NoSuchElementException:
            print("Последняя страница с товарами, выходим")
            break

    if len(broken_goods) > 0:
        print("Товары с битыми изображениями:")
        for product in broken_goods:
            print(product)
    else:
        print("Битых изображений нет")

finally:
    time.sleep(2)
    browser.quit()
