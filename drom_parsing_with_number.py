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
#phones = []
prices = []
models = []

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
        #print(str2)
        number_of_pages = int(str2[-2][-2])
        for j in range(1, number_of_pages+1):
            search_link1 = search_link + f'/page{j}'
            driver.get(search_link1)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            href = driver.find_element(By.CSS_SELECTOR,
                               "body > div:nth-child(3) > div.css-1iexluz.e1m0rp600 > div.css-1ojz5p3.e1m0rp601 > div.css-0.e1m0rp602 > div.css-1173kvb.eaczv700 > div:nth-child(1) > div:nth-child(2)").find_elements(By.TAG_NAME, 'a')
            for i in href:
                links.append(i.get_attribute('href'))
            marka = driver.find_elements(By.XPATH, "//span[@data-ftid='bull_title']")[:len(links)]
            price = driver.find_elements(By.XPATH, "//span[@data-ftid='bull_price']")[:len(links)]
            for m in marka:
                models.append(m.text)
            for p in price:
                prices.append(p.text)
            # for link in links:
            #     driver.get(link)
            #     price = driver.find_element(By.XPATH, "//div[@class='css-eazmxc e162wx9x0']").text
            #     prices.append(price)
                # try:
                #     time.sleep(3)
                #     not_in_sale = driver.find_element(By.XPATH, "//div[@class='css-1bw6vfx edsrp6u2']")
                #     time.sleep(3)
                #     #phones.append('Авто снято с продажи')
                #     time.sleep(3)
                # except NoSuchElementException:
                #     time.sleep(3)
                #     #phone_click = driver.find_element(By.XPATH, "//button[@data-ftid='open-contacts']")
                #     time.sleep(3)
                #     #phone_click.click()
                #     time.sleep(4)
                #     phone = driver.find_element(By.XPATH, "//div[@class='css-16aq7qo e1i7tubr0']")
                #     #phones.append(phone.text)
    except NoSuchElementException:
        driver.get(search_link)
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        href = driver.find_element(By.CSS_SELECTOR,
                                   "body > div:nth-child(3) > div.css-1iexluz.e1m0rp600 > div.css-1ojz5p3.e1m0rp601 > div.css-0.e1m0rp602 > div.css-1173kvb.eaczv700 > div:nth-child(1) > div:nth-child(2)").find_elements(
            By.TAG_NAME, 'a')
        for i in href:
            links.append(i.get_attribute('href'))
        marka = driver.find_elements(By.XPATH, "//span[@data-ftid='bull_title']")[:len(links)]
        for m in marka:
            models.append(m.text)
        # for link in links:
        #     driver.get(link)
        #     price = driver.find_element(By.XPATH, "//div[@class='css-eazmxc e162wx9x0']").text
        #     prices.append(price)
            # try:
            #     time.sleep(3)
            #     not_in_sale = driver.find_element(By.XPATH, "//div[@class='css-1bw6vfx edsrp6u2']")
            #     time.sleep(3)
            #     #phones.append('Авто снято с продажи')
            #     time.sleep(3)
            # except NoSuchElementException:
            #     time.sleep(3)
            #     phone_click = driver.find_element(By.XPATH, "//button[@data-ftid='open-contacts']")
            #     time.sleep(3)
            #     phone_click.click()
            #     time.sleep(4)
            #     phone = driver.find_element(By.XPATH, "//div[@class='css-16aq7qo e1i7tubr0']")
            #     #phones.append(phone.text)
print(links)
print(models)
print(prices)




with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for i in range(len(models)):
        writer.writerow([
            models[i], prices[i], links[i]])







