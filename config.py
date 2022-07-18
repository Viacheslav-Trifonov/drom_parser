from selenium import webdriver
import undetected_chromedriver
from selenium_stealth import stealth
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import csv


useragent = UserAgent()
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
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


link_registration = 'https://my.drom.ru/sign?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1657863275'
codes_of_the_subjects = 'https://codificator.ru/code/car.html'
drom_link = 'https://auto.drom.ru/region'

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
    login_field = driver.find_element(By.XPATH, "//input[@name='sign']").send_keys(login)
    print('Введите пароль:')
    time.sleep(3)
    password = input()
    password_field = driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    time.sleep(3)
    enter_site = driver.find_element(By.XPATH, "//button[@type='submit']")
    time.sleep(3)
    enter_site.click()
    time.sleep(3)
