import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import read_json
from utils.logger import get_logger


logger = get_logger(__name__)


@pytest.mark.ui
def test_login_valido_redirige_a_inventario(driver):
    users = read_json("users.json")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    logger.info("Opening login page for valid login")
    login_page.open()
    login_page.login(
        users["valid_user"]["username"],
        users["valid_user"]["password"],
    )

    assert "inventory.html" in driver.current_url
    assert inventory_page.title_text() == "Products"


@pytest.mark.ui
@pytest.mark.parametrize("invalid_user", read_json("users.json")["invalid_users"])
def test_login_invalido_muestra_mensaje_de_error(driver, invalid_user):
    login_page = LoginPage(driver)

    logger.info("Opening login page for invalid login")
    login_page.open()
    login_page.login(invalid_user["username"], invalid_user["password"])

    assert "Epic sadface" in login_page.get_error_message()

