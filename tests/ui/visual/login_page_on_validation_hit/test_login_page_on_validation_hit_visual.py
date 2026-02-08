import pytest
from playwright.async_api import expect

from a_test_automation.pages.login_page import LoginPage


@pytest.mark.asyncio
async def test_login_page_on_validation_hit_visual(page):
    login_page = LoginPage(page)

    await login_page.open()
    await login_page.submit()

    await expect(page).to_have_screenshot("login-page-on-validation-hit.png", full_page=True)
