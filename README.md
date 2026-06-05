# QA Guru Diploma — Web UI автотесты

Автотесты интернет-магазина [SauceDemo](https://www.saucedemo.com) для дипломного проекта QA Guru.

## Технологии

- Python 3.13
- Pytest
- Selenium WebDriver
- Allure Reports
- WebDriver Manager
- python-dotenv

## Установка и запуск

### 1. Клонировать репозиторий

git clone https://github.com/Gvaradar/qa-guru-diploma-web-ui.git
cd qa-guru-diploma-web-ui

### 2. Создать виртуальное окружение

python -m venv venv
source venv/bin/activate # Linux/Mac

venv\Scripts\activate # Windows

### 3. Установить зависимости

pip install -r requirements.txt

### 4. Настроить переменные окружения

Создать файл `.env` в корне проекта:

BASE_URL=https://www.saucedemo.com

### 5. Запустить тесты

pytest tests/ -v --alluredir=allure_results

### 6. Посмотреть Allure отчет

allure serve allure_results

## Структура проекта

qa-guru-diploma-web-ui/

├── pages/

├── tests/

├── .env

├── requirements.txt

├── pytest.ini

└── README.md

## Тестовые сценарии

- `test_login.py` — позитивные и негативные тесты авторизации
- `test_cart.py` — тесты корзины
- `test_checkout.py` — тесты оформления заказа

## Примечание

Сайт `saucedemo.com` может быть нестабилен. При ошибках соединения повторите запуск позже.