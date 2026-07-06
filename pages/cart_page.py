from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    def go_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

