from datetime import datetime
from pathlib import Path
import re

import pytest
from pytest_html import extras

from utils.driver_factory import create_driver
from utils.logger import get_logger


logger = get_logger(__name__)


def safe_filename(value):
    return re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_").lower()


@pytest.fixture
def driver(request):
    driver_instance = create_driver()
    request.node.driver = driver_instance
    logger.info("Se abrió el navegador para la prueba: %s", request.node.name)
    yield driver_instance
    logger.info("Se cerró el navegador para la prueba: %s", request.node.name)
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
    test_name = safe_filename(item.name)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{test_name}_{timestamp}"
    screenshot_path = screenshots_dir / f"{screenshot_name}.png"
    counter = 1

    while screenshot_path.exists():
        screenshot_path = screenshots_dir / f"{screenshot_name}_{counter}.png"
        counter += 1

    driver_instance.save_screenshot(str(screenshot_path))
    logger.error("Se guardó una captura por el fallo: %s", screenshot_path)

    html_plugin = item.config.pluginmanager.getplugin("html")
    if html_plugin:
        report_extras = getattr(report, "extras", [])
        report_extras.append(extras.image(str(screenshot_path)))
        report.extras = report_extras
