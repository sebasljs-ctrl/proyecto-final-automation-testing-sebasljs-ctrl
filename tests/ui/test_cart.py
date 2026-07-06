import pytest

from pages.cart_page import CartPage
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
def test_agregar_producto_al_carrito(driver):
    login_as_standard_user(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    logger.info("Adding first product to cart")
    product_name = inventory_page.add_first_product_to_cart()

    assert inventory_page.cart_badge_text() == "1"

    inventory_page.open_cart()
    assert cart_page.item_name() == product_name

