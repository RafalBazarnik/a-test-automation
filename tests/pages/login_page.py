class LoginPage:
    def __init__(self, page):
        self.page = page

    async def open(self) -> None:
        await self.page.goto("/login")

    async def login(self, username: str, password: str) -> None:
        await self.page.fill("#username", username)
        await self.page.fill("#password", password)
        await self.page.click("button[type='submit']")

    async def flash_message(self) -> str:
        message = await self.page.text_content("#flash")
        return (message or "").strip()
