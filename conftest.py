from pathlib import Path

import pytest
from pytest_html import extras

from utils.driver_factory import create_driver
from utils.logger import get_logger


logger = get_logger(__name__)


SCREENSHOT_NAMES = {
    "test_login_valido": "login_valido",
    "test_login_invalido": "login_invalido",
    "test_productos": "productos",
    "test_carrito": "carrito",
    "test_checkout": "checkout",
}


@pytest.fixture
def driver(request):
    driver_instance = create_driver()
    request.node.driver = driver_instance
    logger.info("Browser started for test: %s", request.node.name)
    yield driver_instance
    logger.info("Browser closed for test: %s", request.node.name)
    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    driver_instance = getattr(item, "driver", None)
    if driver_instance is None:
        return

    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    screenshot_name = SCREENSHOT_NAMES.get(item.name, item.name.replace("test_", ""))
    screenshot_path = screenshots_dir / f"{screenshot_name}.png"
    counter = 1

    while screenshot_path.exists():
        screenshot_path = screenshots_dir / f"{screenshot_name}_{counter}.png"
        counter += 1

    driver_instance.save_screenshot(str(screenshot_path))
    logger.error("Screenshot saved after failure: %s", screenshot_path)

    html_plugin = item.config.pluginmanager.getplugin("html")
    if html_plugin:
        report_extras = getattr(report, "extras", [])
        report_extras.append(extras.image(str(screenshot_path)))
        report.extras = report_extras
