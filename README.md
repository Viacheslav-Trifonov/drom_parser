# Парсинг объявлений с сайта Drom.ru c помощью Selenium

## Описание
В этом скрипте реализован процесс получения информации об объявлениях автомобилей на сайте Drom.ru.
Процесс автоматизирован при помощи Selenium.
В данном примере парсер собирает информацию по марке, модели, цене, ссылке на объявление и сохраняет результаты в файл res.csv

В файл setup.py вынесены настройки скрытности Selenium. Они позволят мааксимально отсрочить блокировку скрипта от частых запросов.
В частности используется модуль FakeUseragent для автоматического изменения параметра UserAgent при каждом новом запросе.
Также применены библиотеки selenium_stealth и опции для отключения в Selenium обнаружения режима WebDriver.
Ещё в файле setup.py вынесены вспомогательные функции для создания таблицы с отчётом, регистрации на сайте.

В файл config.py вынесены ссылки на сраницы с формой регистрации, ссылкой на главную страницу и информационная ссылка на сайт с кодами регионов, а также локаторы для поиска элементов на страницах.

В файл drom_parsing.py вынесена основная логика парсинга объявлений.


## Установка зависимостей
Для работы парсера потребуется наличие актуального WebDriver для GoogleChrome.
Инструкция по установке Selenium:

- Скачайте с сайта https://sites.google.com/chromium.org/driver/ драйвер для вашей версии браузера. Разархивируйте скачанный файл.

- Создайте на диске C: папку chromedriver и положите разархивированный ранее файл chromedriver.exe в папку C:\chromedriver.

- Добавьте в системную переменную PATH папку C:\chromedriver. Как это сделать в разных версиях Windows, описано здесь: https://www.computerhope.com/issues/ch000549.htm.

Создайте новое виртуальное окружение. Перейдите в директорию своего проекта и выполните команду:

`python -m venv venv`

Далее активируйте новое виртуальное окружение:

`...venv\Scripts\activate.bat`  - для Windows

Для установки зависимостей используйте команду:

`pip install -r requirements.txt`


## Использование

Скрипт запускается командой в консоли `..\drom_parsing.py`.
Сначала он попросит ввести Ваш логин и пароль:

![image](https://user-images.githubusercontent.com/106872149/179449218-1c001309-0f65-4317-b947-2fe72df260ab.png)

Далее необходимо обозначить параметры поиска:
- регион поиска (числовое значение кода региона);
- марку авто;
- модель авто (если необходим поиск только по марке, оставьте модель авто пустой);
Далее запуститься процесс парсинга:

![image](https://user-images.githubusercontent.com/106872149/179449449-cce189ff-c03e-45bd-82a7-546833c13bb7.png)

После окончания парсинга сформирется таблица res.csv с результатами:

![image](https://user-images.githubusercontent.com/106872149/179476685-a2a5c6c6-e68d-487b-8118-1173d86ceabc.png)

В парсер также можно добавить формирование номера телефона из объявления, но это нужно делать очень аккуратно, т.к. при большом количестве нажатий по кнопке "Показать контакты", Дром может начать проверку на робота, и сломает алгоритм.







Данный скрипт работает только с браузером GoogleChrome.
