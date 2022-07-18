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

driver.get(search_link)
try:
    not_found = driver.find_element(By.XPATH, "//div[@class='b-media-cont b-text_size_l']")
    print('Такой страницы не не существует')
except NoSuchElementException:
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    href = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div.css-1iexluz.e1m0rp600 > div.css-1ojz5p3.e1m0rp601 > div.css-0.e1m0rp602 > div.css-1173kvb.eaczv700 > div:nth-child(1) > div:nth-child(2)").find_elements(By.TAG_NAME, 'a')
    links = []
    phones = []
    prices = []
    models = []
    for i in href:
        links.append(i.get_attribute('href'))
    marka = driver.find_elements(By.XPATH, "//span[@data-ftid='bull_title']")[:len(links)]
    for m in marka:
        models.append(m.text)
    for link in links:
        driver.get(link)
        price = driver.find_element(By.XPATH, "//div[@class='css-eazmxc e162wx9x0']").text
        prices.append(price)
        try:
            time.sleep(3)
            not_in_sale = driver.find_element(By.XPATH, "//div[@class='css-1bw6vfx edsrp6u2']")
            time.sleep(3)
            phones.append('Авто снято с продажи')
            time.sleep(3)
        except NoSuchElementException:
            time.sleep(3)
            phone_click = driver.find_element(By.XPATH, "//button[@data-ftid='open-contacts']")
            time.sleep(3)
            phone_click.click()
            time.sleep(4)
            phone = driver.find_element(By.XPATH, "//div[@class='css-16aq7qo e1i7tubr0']")
            phones.append(phone.text)

    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for i in range(len(models)):
            writer.writerow([
                models[i], prices[i], phones[i], links[i]])

finally:
    driver.quit()





