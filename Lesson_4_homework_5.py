from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
import time
import random


browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")
# browser.maximize_window()
browser.implicitly_wait(2)
random_goods_list = list()                          # список случайных порядковых номеров товаров для выборочного теста
page_goods = list()                                 # список      найденных товаров на текущей странице
page_goods_amount = 0                               # количество  найденных товаров на текущей странице
append_token = False                                # токен добавления случайного номера товара в список
global_goods_count = 0                              # счетчит нахождения товаров (должен пробежаться по всем товарам)
final_token = 0                                     # счетчик товаров, которые уже нашлись и добавились в корзину
page_count = 0                                      # счетчик количества страниц

try:
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/catalogue/']").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/basket/']").click()
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/']").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/catalogue/']").click()

    goods_amount = int(browser.find_element(By.CSS_SELECTOR, ".form-horizontal strong:nth-child(2)").text)
    print("Всего товаров в базе: ", goods_amount)

    # kostyl_srochno_ispravit = [25, 128, 199, 200, 201] # номера товаров которые нельзя добавить в корзину
    # for i in range(3):                              # подбираем набор случайных порядковых номеров товаров
    #     while not append_token:                     # номера товаров не должны повторяться
    #         temp = random.randint(1, goods_amount)
    #         if temp not in random_goods_list and temp not in kostyl_srochno_ispravit:
    #             random_goods_list.append(temp)
    #             append_token = True                 # номер товара добавился, можно подбирать следующее число
    #     append_token = False                        # сбрасываем токен добавления случайного номера
    # random_goods_list.sort()                        # сортируем номера товаров в списке по возрастанию

    random_goods_list = [17, 108, 187]                #
    print("Три случайных номера товаров", random_goods_list)



    while True:                                       # листаем все страницы с товарами и добавляем в корзину искомые
        page_count += 1
        page_goods = browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-4.col-md-3.col-lg-3 .btn")
        page_goods_amount = len(browser.find_elements(By.CSS_SELECTOR, ".col-xs-6.col-sm-4.col-md-3.col-lg-3"))
        for i in range(page_goods_amount):            # перебираем все товары на странице
            global_goods_count += 1
            if global_goods_count == random_goods_list[final_token]:
                # global_goods_count += 1
                final_token += 1
                time.sleep(2)
                page_goods[i].click()                 # добавляем в корзину искомый случайный товар
                print(f"Добавился товар #{final_token} со страницы {page_count} с номером {global_goods_count}")
                if final_token > 2:
                   break
        if final_token > 2:
            break

        try:
            link = browser.find_element(By.CSS_SELECTOR, "li.next a")
            browser.execute_script("return arguments[0].scrollIntoView(true);", link)
            browser.find_element(By.CSS_SELECTOR, "li.next a").click()
        except NoSuchElementException:
            print("Последняя страница с товарами, выходим")
            print("Почему-то в корзину добавились не все товары")
            break
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "[href='/ru/basket/']").click()

    assert len(browser.find_elements(By.CSS_SELECTOR, ".basket-items")) == 3

finally:
    time.sleep(5)
    # input("pause")
    browser.quit()
