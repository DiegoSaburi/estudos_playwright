from playwright.sync_api import Page


class NewTodoSection:
    def __init__(self, page: Page):
        self.input = page.get_by_role("textbox", name="What needs to be done?")

    def fill(self, text: str = "") -> None:
        self.input.fill(text)

    def submit(self) -> None:
        self.input.press("Enter")
