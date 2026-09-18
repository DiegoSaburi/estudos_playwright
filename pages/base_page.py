from playwright.sync_api import Page


class BasePage:
    PATH = ""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    @property
    def url(self) -> str:
        return f"{self.base_url}/{self.PATH.lstrip('/')}"

    def open(self) -> None:
        self.page.goto(self.url)
