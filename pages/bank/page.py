from playwright.sync_api import Page

from pages.base_page import BasePage


class BankPage(BasePage):
    PATH = "/bank/"

    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)
