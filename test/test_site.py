
from selenium.webdriver.common.by import By
import time
from pages.home_page import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')
    driver.get('https://demoblaze.com')
    galaxy_s6=driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'



def test_two_monitors(driver):
    homepage = HomePage(driver) #обозначаем, что будем юзать функцию в которую добавляли действия

    #вместо driver.get('https://demoblaze.com') пишем
    homepage.open() #ЭТУ ФУНКЦИЮ ОТКРЫТИЯ САЙТА ТАК ЖЕ СОЗДАЛИ

    #вместо monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    #monitor_link.click() пишем
    homepage.click_monitor() # так же создали эту функцию
    time.sleep(2)


    #вместо monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    #assert len(monitors) == 2 пишем
    homepage.check_products_count(2) #так же создилм функцию