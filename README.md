## Простые тесты для сайта Author.Today
[Author.Today] (https://author.today/)
---
>Любовь к чтению сопровождает человека с раннего возраста до глубокой старости. Кому-то по нраву наслаждаться изящными словесными оборотами авторов классики мировой литературы, кто-то находит ответы на волнующие вопросы в книгах нон-фикшн, а для кого-то чтение — это возможность развлечься лихо закрученными сюжетами хороших детективов, любовных романов и фантастических произведений. (c) Описание с сайта.
<img src="pictures/logo_main_1.jpg" width="5000">

Проверки, проведенные в ходе тестов:
- Открытие главной страницы
- Проверка отработки кнопки поиска и поля текстового ввода
- Позитивный поиск результатов
- Негативный поиск результатов
- Пролистывание вкладок, группирующих авторов, произведения и иллюстрации на основе поиска

---
В проекте использовались следующие инструменты:
<img src="pictures/allure_report_1.png" width="50"> <img src="pictures/pytest_1.png" width="50">  <img src="pictures/python_1.svg" width="50"> <img src="pictures/selene_1.png" width="50"> <img src="pictures/selenoid_1.png" width="50"> <img src="pictures/tg_1.png" width="50"> 

- Язык программирования `Python`
- Фреймворк для написания UI тестов `Selene` с использованием `Selenium WebDriver`
- Фреймворк модульного тестирования `Pytest`
- Выполнение удаленного запуска тестов с помощью `Jenkins` с использованием `Selenoid`
- Фреймворки для сбора отчетности и хранения файлов тестирования `Allure Report`
- Краткие отчеты в `Telegram` отправляет `Telegram Bot`

---

### Локальный запуск
Перед запуском в корне проекта создать файл .env с содержимым:
```
SELENOID_LOGIN=user1
SELENOID_PASS=1234
SELENOID_URL=selenoid.autotests.cloud
```

Для локального запуска необходимо выполнить:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### Удаленный запуск тестов выполняется в Jenkins
Посмотреть и запустить можно на странице проекта в [Jenkins](https://jenkins.autotests.cloud/job/C18-Dee_and_Linux_the_Cat-unit14_3/1/)

Для запуска тестов необходимо:
1. Перейти на [проект](https://jenkins.autotests.cloud/job/C18-Dee_and_Linux_the_Cat-unit14_3/)
2. Нажать на кнопку `Build now`
3. Дождаться окончания тестирования
4. Нажать на кнопку `Allure Report`

### Отчет о результатах тестирования в Telegram
Отчеты приходят в канал [Report channel](https://t.me/ErmilovaDV_test_reports_bot)
