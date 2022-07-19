from config import *
from selenium import webdriver
from selenium_stealth import stealth
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.by import By
import csv

useragent = UserAgent()
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  браузер без интерфеса
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("start-maximized")
options.add_argument(f"user-agent={useragent.random}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
     "source": """
          const newProto = navigator.__proto__
          delete newProto.webdriver
          navigator.__proto__ = newProto
          """
    })

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def create_table():
    with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Марка, Модель', 'Цена', 'Ссылка на объявление'])


def login_on_site():
    driver.get(link_registration)
    time.sleep(10)
    print('Введите логин:')
    login = input()
    login_field = driver.find_element(*login_locator)
    login_field.send_keys(login)
    print('Введите пароль:')
    time.sleep(3)
    password = input()
    password_field = driver.find_element(*password_locator)
    password_field.send_keys(password)
    time.sleep(3)
    enter_site = driver.find_element(*button_locator)
    time.sleep(3)
    enter_site.click()
    time.sleep(3)


links = []
prices = []
models = []


def parse():
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    href = driver.find_element(*href_locator).find_elements(By.TAG_NAME, 'a')
    for i in href:
        links.append(i.get_attribute('href'))
    marka = driver.find_elements(*marka_locator)[:len(href)]
    price = driver.find_elements(*price_locator)[:len(href)]
    for m in marka:
        models.append(m.text)
    for p in price:
        prices.append(p.text)
