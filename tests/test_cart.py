import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.epic('UI тестирование')
@allure.feature('Корзина')
class TestCart:

    @allure.story('Добавление товара')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_add_item_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()

        cart_page.should_have_cart_count('1')

    @allure.story('Удаление товара')
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_item_from_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()

        cart_page.remove_first_item()
        cart_page.should_be_empty()

    @allure.story('Продолжение покупок')
    @allure.severity(allure.severity_level.MINOR)
    def test_continue_shopping(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()

        cart_page.click_continue_shopping()
        cart_page.should_be_on_inventory_page()