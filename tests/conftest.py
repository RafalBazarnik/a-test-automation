import pytest
from playwright.async_api import async_playwright
from a_test_automation.config import get_settings


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--env", action="store", default="dev")
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--device", action="store", default="iPhone 13")
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture(scope="session")
def env_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("--env")


@pytest.fixture(scope="session")
def browser_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def device_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("--device")


@pytest.fixture(scope="session")
def headless(pytestconfig: pytest.Config) -> bool:
    return pytestconfig.getoption("--headless")


@pytest.fixture(scope="session")
def settings(env_name: str):
    return get_settings(env_name)


@pytest.fixture
async def page(settings, browser_name: str, device_name: str, headless: bool):
    async with async_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)
        browser = await browser_type.launch(headless=headless)
        device = playwright.devices.get(device_name)
        if device is None:
            raise ValueError(
                f"Unknown device '{device_name}'. Use a valid Playwright device name."
            )

        context = await browser.new_context(base_url=settings.ui_base_url, **device)
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()
