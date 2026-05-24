import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure


@pytest.fixture
def driver(request):
    """Фикстура для настройки драйвера"""
    options = Options()
    options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=options)

    # Устанавливаем неявное ожидание (ждём элементы до 20 секунд)
    driver.implicitly_wait(20)

    # Устанавливаем таймаут загрузки страницы (60 секунд)
    driver.set_page_load_timeout(60)

    base_url = 'https://www.saucedemo.com'
    driver.base_url = base_url

    def fin():
        allure.attach(
            driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
        driver.quit()

    request.addfinalizer(fin)
    return driver