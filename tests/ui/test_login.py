import pytest
from tests.pages.login_page import LoginPage


@pytest.mark.asyncio
async def test_login(page, settings):
    login_page = LoginPage(page)
    await login_page.open()
    await login_page.login(settings.login_user, settings.login_password)
    message = await login_page.flash_message()
    assert "You logged into a secure area" in message
