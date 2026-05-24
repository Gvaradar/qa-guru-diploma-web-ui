import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage  # создадим чуть позже


@allure.epic('UI тестирование')
@allure.feature('Авторизация')
class TestLogin:

    @allure.story('Позитивный сценарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')

        with allure.step('Проверить, что вход выполнен успешно'):
            assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    @allure.story('Негативный сценарий')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('negative')
    def test_invalid_login_locked_user(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login('locked_out_user', 'secret_sauce')

        with allure.step('Проверить сообщение о блокировке'):
            login_page.should_have_error(
                'Sorry, this user has been locked out.'
            )

    @allure.story('Негативный сценарий')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('negative')
    def test_invalid_login_wrong_password(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login('standard_user', 'wrong_password')

        with allure.step('Проверить сообщение об ошибке'):
            login_page.should_have_error(
                'Username and password do not match any user in this service'
            )