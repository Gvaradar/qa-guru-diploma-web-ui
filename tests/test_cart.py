import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.epic('UI тестирование')
@allure.feature('Корзина')
class TestCart:

    @allure.story('Добавление товара')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_add_item_to_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()

        with allure.step('Проверить, что товар добавлен (счетчик корзины = 1)'):
            cart_count = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
            assert cart_count.text == '1'

    @allure.story('Удаление товара')
    @allure.severity(allure.severity_level.NORMAL)
    def test_remove_item_from_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()

        with allure.step('Удалить товар из корзины'):
            driver.find_element(By.XPATH, '//button[text()="Remove"]').click()

        with allure.step('Проверить, что корзина пуста'):
            cart_items = driver.find_elements(By.CLASS_NAME, 'cart_item')
            assert len(cart_items) == 0

    @allure.story('Продолжение покупок')
    @allure.severity(allure.severity_level.MINOR)
    def test_continue_shopping(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()

        with allure.step('Нажать кнопку Continue Shopping'):
            driver.find_element(By.ID, 'continue-shopping').click()

        with allure.step('Проверить, что вернулись на страницу товаров'):
            assert 'inventory.html' in driver.current_url