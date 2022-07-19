from selenium.common import NoSuchElementException
from setup import *
from config import *


def main():
    print(f'Введите регион поиска (число, в соответствии с {codes_of_the_subjects}:')
    codes_of_the_subjects_number = input() + '/'
    print('Введите марку авто:')
    marka_avto = input() + '/'
    print('Введите модель авто:')
    model_avto = input()
    print('Идёт сбор данных...')
    search_link = drom_link + codes_of_the_subjects_number + marka_avto + model_avto
    try:
        driver.get(search_link)
        time.sleep(3)
        driver.find_element(*not_found_page_locator)
        print('Такой страницы не существует')
    except NoSuchElementException:
        try:
            driver.get(search_link)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            str2 = []
            str1 = driver.find_element(*str1_locator).find_elements(By.TAG_NAME, 'a')
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

if __name__ == "__main__":
    create_table()
    login_on_site()
    main()

