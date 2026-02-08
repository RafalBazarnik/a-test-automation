import pytest
from playwright.async_api import expect

from a_test_automation.pages.login_page import LoginPage


@pytest.mark.asyncio
async def test_login_page_on_start_visual(page):
    login_page = LoginPage(page)

    await login_page.open()

    await expect(page).to_have_screenshot("login-page-on-start.png", full_page=True)
