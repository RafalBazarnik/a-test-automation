from pathlib import Path

import pytest

from a_test_automation.pages.login_page import LoginPage
from a_test_automation.visual_assertions import assert_page_matches_baseline


@pytest.mark.asyncio
async def test_login_page_on_start_visual(page):
    login_page = LoginPage(page)

    await login_page.open()

    test_dir = Path(__file__).parent
    await assert_page_matches_baseline(
        page,
        baseline_path=test_dir / "snapshots" / "login-page-on-start.png",
        actual_path=test_dir / "artifacts" / "login-page-on-start.actual.png",
    )
