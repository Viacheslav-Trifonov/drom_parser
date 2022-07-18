from selenium.common import NoSuchElementException
from config import *

create_table()

login_on_site()

print(f'Введите регион поиска (число, в соответствии с {codes_of_the_subjects}:')
codes_of_the_subjects_number = input() + '/'
print('Введите марку авто:')
marka_avto = input() + '/'
print('Введите модель авто:')
model_avto = input()
print('Идёт сбор данных...')
search_link = drom_link + codes_of_the_subjects_number + marka_avto + model_avto

links = []
prices = []
models = []

def parse():
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    href = driver.find_element(By.CSS_SELECTOR,
                               "body > div:nth-child(3) > div.css-1iexluz.e1m0rp600 > div.css-1ojz5p3.e1m0rp601 > div.css-0.e1m0rp602 > div.css-1173kvb.eaczv700 > div:nth-child(1) > div:nth-child(2)").find_elements(
        By.TAG_NAME, 'a')
    for i in href:
        links.append(i.get_attribute('href'))
    marka = driver.find_elements(By.XPATH, "//span[@data-ftid='bull_title']")[:len(href)]
    price = driver.find_elements(By.XPATH, "//span[@data-ftid='bull_price']")[:len(href)]
    for m in marka:
        models.append(m.text)
    for p in price:
        prices.append(p.text)

try:
    driver.get(search_link)
    time.sleep(3)
    not_found = driver.find_element(By.XPATH, "//div[@class='b-media-cont b-text_size_l']")
    print('Такой страницы не существует')
except NoSuchElementException:
    try:
        driver.get(search_link)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        str2 = []
        str1 = driver.find_element(By.XPATH, "//div[@class='css-14wh0pm e1lm3vns0']").find_elements(By.TAG_NAME, 'a')
        for i in str1:
            str2.append(i.get_attribute('href'))
        number_of_pages = int(str2[-2][-2])
        for j in range(1, number_of_pages+1):
            search_link1 = search_link + f'/page{j}'
            driver.get(search_link1)
            parse()
    except NoSuchElementException:
        driver.get(search_link)
        parse()

finally:
    driver.quit()
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for i in range(len(prices)):
            writer.writerow([models[i], prices[i], links[i]])
    print('Отчёт сформирован')













