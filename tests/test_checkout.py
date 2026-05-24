import allure
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.epic('UI тестирование')
@allure.feature('Оформление заказа')
class TestCheckout:

    @allure.story('Позитивный сценарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag('smoke', 'positive')
    def test_complete_checkout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()
        cart_page.click_checkout()
        checkout_page.fill_checkout_form('Test', 'User', '12345')
        checkout_page.click_continue()
        checkout_page.click_finish()
        checkout_page.should_have_success_message()

    @allure.story('Негативный сценарий')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag('negative')
    def test_checkout_empty_cart(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.open_cart()
        cart_page.click_checkout()

        with allure.step('Проверить сообщение об ошибке'):
            error = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
            assert 'Cart is empty' in error.text

    @allure.story('Отмена оформления')
    @allure.severity(allure.severity_level.MINOR)
    def test_cancel_checkout(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        inventory_page.add_first_item_to_cart()
        inventory_page.open_cart()
        cart_page.click_checkout()

        with allure.step('Нажать Cancel'):
            driver.find_element(By.ID, 'cancel').click()

        with allure.step('Проверить, что вернулись в корзину'):
            assert 'cart.html' in driver.current_url
            cart_page.should_have_items_count(1)