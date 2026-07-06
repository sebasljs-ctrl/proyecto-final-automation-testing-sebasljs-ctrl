from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    FIRST_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")

    def title_text(self):
        return self.get_text(self.TITLE)

    def product_count(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ITEMS))
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT_NAME)

    def add_first_product_to_cart(self):
        product_name = self.first_product_name()
        self.click(self.FIRST_ADD_BUTTON)
        return product_name

    def cart_badge_text(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)

    def is_sort_visible(self):
        return self.find_visible(self.SORT_SELECT).is_displayed()
