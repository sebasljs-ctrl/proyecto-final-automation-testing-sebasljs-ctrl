import pytest

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
def test_inventario_muestra_productos_y_filtro(driver):
    login_as_standard_user(driver)
    inventory_page = InventoryPage(driver)

    logger.info("Validating inventory products and sorting control")
    assert inventory_page.title_text() == "Products"
    assert inventory_page.product_count() >= 1
    assert inventory_page.is_sort_visible()

