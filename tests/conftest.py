import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from utils.allure_attachments import attach_screenshot, attach_html

load_dotenv()


@pytest.fixture
def driver(request):
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(60)
    driver.set_page_load_timeout(120)
    driver.base_url = os.getenv('BASE_URL')

    yield driver

    attach_screenshot(driver)
    attach_html(driver)

    driver.quit()