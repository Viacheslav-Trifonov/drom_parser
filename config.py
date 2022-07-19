from selenium.webdriver.common.by import By

link_registration = 'https://my.drom.ru/sign?return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1657863275'
codes_of_the_subjects = 'https://codificator.ru/code/car.html'
drom_link = 'https://auto.drom.ru/region'

login_locator = (By.XPATH, "//input[@name='sign']")
password_locator = (By.XPATH, "//input[@name='password']")
button_locator = (By.XPATH, "//button[@type='submit']")

href_locator = (By.CSS_SELECTOR, "body > div:nth-child(3) > div.css-1iexluz.e1m0rp600 > div.css-1ojz5p3.e1m0rp601 > div.css-0.e1m0rp602 > div.css-1173kvb.eaczv700 > div:nth-child(1) > div:nth-child(2)")
marka_locator = (By.XPATH, "//span[@data-ftid='bull_title']")
price_locator = (By.XPATH, "//span[@data-ftid='bull_price']")

not_found_page_locator = (By.XPATH, "//div[@class='b-media-cont b-text_size_l']")
str1_locator = (By.XPATH, "//div[@class='css-14wh0pm e1lm3vns0']")