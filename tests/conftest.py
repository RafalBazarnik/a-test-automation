import pytest
from playwright.async_api import async_playwright

from a_test_automation.ai_client import ChatbotClient, ChatbotClientConfig
from a_test_automation.config import get_settings


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--env", action="store", default="dev")
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption(
        "--system-prompt",
        action="store",
        default="",
        help="System prompt used by AI tests. If empty, SYSTEM_PROMPT env var is used.",
    )


@pytest.fixture(scope="session")
def env_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("--env")


@pytest.fixture(scope="session")
def browser_name(pytestconfig: pytest.Config) -> str:
    return pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def headless(pytestconfig: pytest.Config) -> bool:
    return pytestconfig.getoption("--headless")


@pytest.fixture(scope="session")
def settings(env_name: str):
    return get_settings(env_name)


@pytest.fixture(scope="session")
def system_prompt(pytestconfig: pytest.Config) -> str:
    from_env = pytestconfig.getoption("--system-prompt")
    if from_env:
        return from_env

    import os

    return os.getenv("SYSTEM_PROMPT", "")


@pytest.fixture(scope="session")
def ai_client(settings) -> ChatbotClient:
    if not settings.chatbot_api_url:
        pytest.skip("CHATBOT_API_URL is not configured. Configure it in .env.<env>.")

    return ChatbotClient(
        ChatbotClientConfig(
            endpoint=settings.chatbot_api_url,
            api_key=settings.chatbot_api_key,
            api_key_header=settings.chatbot_api_key_header,
            api_key_prefix=settings.chatbot_api_key_prefix,
            system_prompt_field=settings.chatbot_system_prompt_field,
            question_field=settings.chatbot_question_field,
            answer_field=settings.chatbot_answer_field,
        ),
    )


@pytest.fixture
async def page(settings, browser_name: str, headless: bool):
    async with async_playwright() as playwright:
        browser_type = getattr(playwright, browser_name)
        browser = await browser_type.launch(headless=headless)
        context = await browser.new_context(base_url=settings.ui_base_url)
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()
