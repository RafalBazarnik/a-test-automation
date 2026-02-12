import pytest

from a_test_automation.pages.login_page import LoginPage


@pytest.mark.asyncio
async def test_login_page_on_validation_hit_visual(page, file_regression):
    login_page = LoginPage(page)

    await login_page.open()
    await login_page.submit()

    screenshot = await page.screenshot(full_page=True)
    file_regression.check(screenshot, extension=".png", binary=True)
