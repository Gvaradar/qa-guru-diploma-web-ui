from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, 'checkout')
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    REMOVE_BUTTON = (By.XPATH, '//button[text()="Remove"]')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')

    @allure.step('Нажать кнопку Checkout')
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        return self

    @allure.step('Проверить, что в корзине {expected_count} товар(ов)')
    def should_have_items_count(self, expected_count: int):
        items = self.find_all(self.CART_ITEM)
        assert len(items) == expected_count
        return self

    @allure.step("Проверить, что счетчик корзины показывает {expected_count}")
    def should_have_cart_count(self, expected_count: str):
        cart_count = self.find(self.CART_BADGE)
        assert cart_count.text == expected_count

    @allure.step("Проверить, что корзина пуста")
    def should_be_empty(self):
        cart_items = self.find_all(self.CART_ITEM)
        assert len(cart_items) == 0

    @allure.step("Удалить первый товар из корзины")
    def remove_first_item(self):
        self.click(self.REMOVE_BUTTON)

    @allure.step("Нажать Continue Shopping")
    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    @allure.step("Проверить, что открыта страница каталога")
    def should_be_on_inventory_page(self):
        assert 'inventory.html' in self.driver.current_url