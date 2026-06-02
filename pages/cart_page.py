from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    REMOVE_BUTTON = (By.XPATH, '//button[text()="Remove"]')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')

    @allure.step('Нажать кнопку Checkout')
    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        return self

    @allure.step('Проверить, что в корзине {expected_count} товар(ов)')
    def should_have_items_count(self, expected_count: int):
        items = self.driver.find_elements(*self.CART_ITEM)
        assert len(items) == expected_count
        return self

    @allure.step("Проверить, что счетчик корзины показывает {expected_count}")
    def should_have_cart_count(self, expected_count: str):
        cart_count = self.driver.find_element(*self.CART_BADGE)
        assert cart_count.text == expected_count

    @allure.step("Проверить, что корзина пуста")
    def should_be_empty(self):
        cart_items = self.driver.find_elements(*self.CART_ITEM)
        assert len(cart_items) == 0

    @allure.step("Удалить первый товар из корзины")
    def remove_first_item(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()

    @allure.step("Нажать Continue Shopping")
    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()

    @allure.step("Проверить, что открыта страница каталога")
    def should_be_on_inventory_page(self):
        assert 'inventory.html' in self.driver.current_url