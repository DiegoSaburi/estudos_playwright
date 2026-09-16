from playwright.sync_api import Page


class TodoListSection:
    def __init__(self, page: Page):
        self.page = page

    def item(self, text: str):
        return self.page.get_by_role("listitem").filter(has_text=text)

    def toggle(self, text: str) -> None:
        self.item(text).get_by_label("Toggle Todo").check()

    def toggle_many(self, texts: list[str]) -> None:
        for text in texts:
            self.toggle(text)
