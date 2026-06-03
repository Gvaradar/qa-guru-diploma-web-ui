import allure
from models.user import User
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.epic('UI тестирование')
@allure.feature('Авторизация')
class TestLogin:

    @allure.story('Позитивный сценарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        user = User('standard_user', 'secret_sauce')

        login_page.open()
        login_page.login(user.username, user.password)

        login_page.should_be_on_inventory_page()

    @allure.story('Негативный сценарий')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('negative')
    def test_invalid_login_locked_user(self, driver):
        login_page = LoginPage(driver)
        user = User('locked_out_user', 'secret_sauce')

        login_page.open()
        login_page.login(user.username, user.password)

        login_page.should_have_error('Sorry, this user has been locked out.')

    @allure.story('Негативный сценарий')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('negative')
    def test_invalid_login_wrong_password(self, driver):
        login_page = LoginPage(driver)
        user = User('standard_user', 'wrong_password')

        login_page.open()
        login_page.login(user.username, user.password)

        login_page.should_have_error('Username and password do not match any user in this service')