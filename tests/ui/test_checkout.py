import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json
from utils.logger import get_logger


logger = get_logger(__name__)


def login_as_standard_user(driver):
    users = read_json("users.json")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(
        users["valid_user"]["username"],
        users["valid_user"]["password"],
    )


@pytest.mark.ui
def test_checkout_completo(driver):
    checkout_data = read_json("checkout_data.json")["customer"]
    login_as_standard_user(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    logger.info("Completing checkout flow")
    inventory_page.add_first_product_to_cart()
    inventory_page.open_cart()
    cart_page.go_to_checkout()
    checkout_page.complete_information(
        checkout_data["first_name"],
        checkout_data["last_name"],
        checkout_data["postal_code"],
    )
    checkout_page.finish_purchase()

    assert checkout_page.confirmation_message() == "Thank you for your order!"

